import io
import json
from collections.abc import Callable
from pathlib import Path
from typing import Any, Dict

import yaml


def _guard(file_path: str, loader: Callable[[str], ...]):
    try:
        with Path(file_path).open("r") as f:
            return loader(f)
    except FileNotFoundError as e:
        raise FileNotFoundError("Not found config file", e)
    except (yaml.YAMLError, TypeError, Exception) as e:
        raise ValueError(f"[Error][{type(e).__name__}] Reading {file_path}")


def load_yaml(file_path: str) -> Dict[str, Any]:
    return _guard(file_path, yaml.safe_load)


def load_json(file_path: str) -> str:
    return _guard(file_path, json.load)


def load_text(file_path: str):
    return _guard(file_path, io.TextIOWrapper.read)


class InvalidFileFormatError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
