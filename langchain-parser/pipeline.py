from models.openai import openai_model
from parsers.parser_factory import create_pydantic_parser
from parsers.html_to_md_parser import HtmlToMdParser
from prompts.loader import load_prompt_and_template
from utils import load_yaml, load_text


# Seperate to Config yaml
CONFIG_PATH = "./templates/model/default.yaml"
PROMPT_PATH = "./templates/prompt/default.json"
HTML_PATH = "../data/test.html"


def main():
    config = load_yaml(CONFIG_PATH)
    model = openai_model(config["llama3.1"])
    # Load parser and Outputparser
    parser, instruction = create_pydantic_parser(HtmlToMdParser, get_instruction=True)
    # Load prompt and template from Path
    prompt, template = load_prompt_and_template(PROMPT_PATH)
    prompt = prompt.partial(format_instruction=instruction)

    # HTML file load
    html_content = load_text(HTML_PATH)

    chain = prompt | model | parser

    response = chain.invoke(
        {
            "system_prompt": template["system_prompt"],
            "user_prompt": template["user_prompt"],
            "html_content": html_content,
        }
    )


if __name__ == "__main__":
    main()
