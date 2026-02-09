#!/usr/bin/env python3
"""Minimal image -> base64 tool for Copilot usage.

Writes:
 - copied original image (out_dir/<uid>-<safe_name>.<ext>)
 - wrapped base64 text (same name + ".b64.txt") with configurable wrap width (default 1024)
 - metadata JSON (same name + ".meta.json")

Prints a small JSON summary to stdout for callers to parse.

This script has no external dependencies and is KISS.
"""

from __future__ import annotations
import os
import sys
import uuid
import time
import json
import base64
from pathlib import Path

CHUNK = 3 * 1024  # read size (multiple of 3 for base64)

try:
    from PIL import Image, UnidentifiedImageError  # type: ignore

    HAVE_PIL = True
except Exception:
    Image = None  # type: ignore
    UnidentifiedImageError = Exception  # type: ignore
    HAVE_PIL = False


def safe_filename(name: str) -> str:
    return "".join(c if (c.isalnum() or c in ("-", "_", ".")) else "_" for c in name)


def guess_mime(suffix: str) -> str:
    s = suffix.lower().lstrip(".")
    if s in ("png", "jpg", "jpeg", "gif", "bmp", "webp", "tiff", "tif"):
        if s == "jpg":
            s = "jpeg"
        if s in ("tif", "tiff"):
            s = "tiff"
        return f"image/{s}"
    return "application/octet-stream"


def save_original_and_b64(
    src: str,
    out_dir: str = "extracted/images",
    wrap_width: int = 1024,
    data_uri: bool = False,
    max_bytes_mb: int = 20,
    write_raw: bool = False,
    source_input: str | None = None,
    validate: bool = True,
) -> dict:
    src_path = Path(src)
    if not src_path.exists():
        raise SystemExit(f"source file does not exist: {src}")

    out_dir_p = Path(out_dir)
    out_dir_p.mkdir(parents=True, exist_ok=True)

    uid = f"{int(time.time())}-{uuid.uuid4().hex[:8]}"
    name = safe_filename(src_path.name)
    orig_path = out_dir_p / f"{uid}-{name}"

    # preserve suffix
    if src_path.suffix:
        orig_path = Path(str(orig_path) + src_path.suffix)

    # copy original (chunked)
    try:
        with src_path.open("rb") as rf, orig_path.open("wb") as wf:
            while True:
                chunk = rf.read(8192)
                if not chunk:
                    break
                wf.write(chunk)
    except Exception as e:
        raise SystemExit(f"failed copying original: {e}")

    size = orig_path.stat().st_size
    if max_bytes_mb is not None and size > max_bytes_mb * 1024 * 1024:
        orig_path.unlink(missing_ok=True)
        raise SystemExit(f"file too large: {size} bytes (max {max_bytes_mb} MB)")

    # validate image with Pillow if requested
    if validate:
        if not HAVE_PIL:
            orig_path.unlink(missing_ok=True)
            raise SystemExit(
                "Pillow is not available; install pillow or run with --no-validate"
            )
        try:
            with Image.open(orig_path) as im:
                im.verify()
        except UnidentifiedImageError:
            orig_path.unlink(missing_ok=True)
            raise SystemExit("invalid image file: Pillow cannot identify image file")
        except Exception as e:
            orig_path.unlink(missing_ok=True)
            raise SystemExit(f"image validation failed: {e}")

    mime = guess_mime(orig_path.suffix)
    b64_path = Path(str(orig_path) + ".b64.txt")
    meta_path = Path(str(orig_path) + ".meta.json")
    raw_path = Path(str(orig_path) + ".b64.raw.txt") if write_raw else None

    try:
        with orig_path.open("rb") as rf, b64_path.open("w", encoding="ascii") as bf:
            if raw_path:
                rawf = raw_path.open("w", encoding="ascii")
            else:
                rawf = None

            # optionally write data URI prefix
            prefix = f"data:{mime};base64," if data_uri else ""
            if prefix:
                bf.write(prefix)
                if rawf:
                    rawf.write(prefix)

            carry = ""
            while True:
                chunk = rf.read(CHUNK)
                if not chunk:
                    break
                enc = base64.b64encode(chunk).decode("ascii")
                # write raw (no newlines) if requested
                if rawf:
                    rawf.write(enc)

                # accumulate and write wrapped lines
                carry += enc
                while len(carry) >= wrap_width:
                    bf.write(carry[:wrap_width])
                    bf.write("\n")
                    carry = carry[wrap_width:]

            # flush remaining
            if carry:
                bf.write(carry)
                bf.write("\n")
            if rawf:
                rawf.close()
    except Exception as e:
        # cleanup on failure
        b64_path.unlink(missing_ok=True)
        if raw_path:
            raw_path.unlink(missing_ok=True)
        orig_path.unlink(missing_ok=True)
        raise SystemExit(f"failed creating base64 file: {e}")

    meta = {
        "original": str(orig_path),
        "b64_path": str(b64_path),
        "mime": mime,
        "size_bytes": size,
        "created_at": int(time.time()),
    }
    if source_input:
        meta["source_input"] = source_input

    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")

    out = {
        "original": str(orig_path),
        "b64": str(b64_path),
        "meta": str(meta_path),
        "mime": mime,
        "size_bytes": size,
    }
    if raw_path:
        out["b64_raw"] = str(raw_path)
    return out


def _parse_args(argv: list[str]) -> dict:
    import argparse

    p = argparse.ArgumentParser(
        description="Write original image + wrapped base64 text + metadata"
    )
    p.add_argument("image", help="path to source image")
    p.add_argument(
        "--out",
        default="extracted/images",
        help="output directory (default: extracted/images)",
    )
    p.add_argument(
        "--wrap-width",
        type=int,
        default=1024,
        help="wrap width for base64 lines (default 1024)",
    )
    p.add_argument(
        "--data-uri",
        action="store_true",
        help="prefix b64 file with data:<mime>;base64,",
    )
    p.add_argument(
        "--max-bytes", type=int, default=20, help="max file size in MB (default 20)"
    )
    p.add_argument(
        "--raw",
        action="store_true",
        help="also write a single-line raw base64 file (.b64.raw.txt)",
    )
    p.add_argument(
        "--source-input", help="optional source input identifier to store in metadata"
    )
    p.add_argument(
        "--no-validate",
        action="store_true",
        help="skip Pillow validation (useful if Pillow is unavailable)",
    )
    args = p.parse_args(argv)
    return vars(args)


if __name__ == "__main__":
    try:
        opts = _parse_args(sys.argv[1:])
        result = save_original_and_b64(
            opts["image"],
            out_dir=opts["out"],
            wrap_width=opts["wrap_width"],
            data_uri=opts["data_uri"],
            max_bytes_mb=opts["max_bytes"],
            write_raw=opts["raw"],
            source_input=opts.get("source_input"),
            validate=not bool(opts.get("no_validate")),
        )
        # print JSON summary to stdout
        print(json.dumps(result, ensure_ascii=False))
        sys.exit(0)
    except SystemExit as e:
        # argparse uses SystemExit for normal exit; if message present treat as error
        msg = str(e)
        if msg:
            print(msg, file=sys.stderr)
            sys.exit(1)
        raise
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(2)
