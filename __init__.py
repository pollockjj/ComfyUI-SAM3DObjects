"""ComfyUI-SAM3DObjects root module."""

from __future__ import annotations

from pathlib import Path

from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"


def _PRESTARTUP_WEB_COPY(web_dir_path: str) -> None:
    """Recreate the old comfy_env viewer copy inside the child process."""
    from comfy_3d_viewers import copy_viewer

    copy_viewer("pointcloud_vtk", Path(web_dir_path))


__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
    "_PRESTARTUP_WEB_COPY",
]
