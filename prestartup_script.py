"""Host-safe prestartup hook for SAM3DObjects.

The original upstream hook used ``comfy_env`` to provision the environment and
copy runtime assets. For pyisolate conversion we keep only the host-safe asset
copy into ``ComfyUI/input`` here and defer viewer population to the child-side
web-copy hook declared in ``__init__.py``.
"""

from __future__ import annotations

from pathlib import Path
import folder_paths


def _copy_assets_best_effort() -> None:
    script_dir = Path(__file__).resolve().parent
    src_root = script_dir / "assets"
    dst_root = Path(folder_paths.get_input_directory())
    if not src_root.exists():
        return
    dst_root.mkdir(parents=True, exist_ok=True)
    for src in src_root.rglob("*"):
        if not src.is_file():
            continue
        rel = src.relative_to(src_root)
        dst = dst_root / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.exists():
            dst.write_bytes(src.read_bytes())


_copy_assets_best_effort()
