import json
from pathlib import Path

import yaml


def load_yaml(file_path: str):
    file_path = Path(file_path)
    if file_path.suffix not in ["yaml", "yml"]:
        raise InvalidFileFormatError(
            "지원하지 않는 파일 형식입니다.'yaml', 'yml'만 지원합니다.",
            file_path.suffix,
        )
    try:
        with Path.open(file_path) as f:
            raw_config = yaml.safe_load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError("config 파일을 찾을 수 없습니다.", e)
    except yaml.YAMLError as e:
        raise ValueError("YAML 파일 구문 오류") from e
    return raw_config


def load_json(file_path: str) -> str:
    file_path = Path(file_path)
    if file_path.suffix not in ["json"]:
        raise InvalidFileFormatError(
            "지원하지 않는 파일 형식입니다.'yaml', 'yml'만 지원합니다.",
            file_path.suffix,
        )
    try:
        with Path.open(file_path) as f:
            raw_config = json.laods(f)
    except FileNotFoundError as e:
        raise FileNotFoundError("config 파일을 찾을 수 없습니다.", e)
    except yaml.YAMLError as e:
        raise ValueError("YAML 파일 구문 오류") from e
    return raw_config


class InvalidFileFormatError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
