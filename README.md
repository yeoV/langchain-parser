# HTML Parser LLM Module

This project provides a module to call parsing HTML content using LLMs API (Large Language Models) powered by `langchain` library.

---

---

## Requirements

- Python >= **3.10+**
- `uv` package manager

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies using `uv`:
   ```bash
   uv install
   ```

3. Verify the installation:
   ```bash
   python --version  # Ensure Python 3.10+ is installed
   uv --version      # Ensure uv is properly set up
   ```

---

## Usage
- [example](https://github.com/yeoV/langchain-parser/blob/main/langchain_parser/pipeline.py)
``` python
import asyncio

from inference import infer_batches_async
from models.openai import openai_model
from parsers.html_to_md_parser import HtmlToMdParser
from parsers.parser_factory import create_pydantic_parser
from prompts.loader import load_prompt_and_template
from utils import load_text, load_yaml


# Seperate to Config yaml
CONFIG_PATH = "./templates/model/default.yaml"
PROMPT_PATH = "./templates/prompt/default.json"
HTML_PATH = "../data/test.html"


async def main():
    config = load_yaml(CONFIG_PATH)
    model = openai_model(config["llama3.1"])
    # Load parser and Outputparser
    parser, instruction = create_pydantic_parser(HtmlToMdParser, get_instruction=True)
    # Load prompt and template from Path
    prompt, template = load_prompt_and_template(PROMPT_PATH)
    prompt = prompt.partial(
        format_instruction=instruction,
        system_prompt=template["system_prompt"],
        user_prompt=template["user_prompt"],
    )

    # HTML file load
    # [{"key":{"html_content":"content"}}]
    data = load_text(HTML_PATH)

    chain = prompt | model | parser
    results = infer_batches_async(chain, data, batch_size=100)

    return results


if __name__ == "__main__":
    asyncio.run(main())
```

---

## Run

1.Run
```bash
uv run python code.py
```
