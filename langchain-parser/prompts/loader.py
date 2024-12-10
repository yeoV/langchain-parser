from typing import Any, Dict, Tuple

from langchain_core.prompts import PromptTemplate
from utils import load_json


def load_prompt_and_template(
    template_path: str,
) -> Tuple[PromptTemplate, Dict[str, Any]]:
    template = load_json(template_path)
    if "prompt_format" not in template.keys():
        raise KeyError("Key 'prompt_format' not found in template file.")
    return (PromptTemplate.from_template(template["prompt_format"]), template)
