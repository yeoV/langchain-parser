from models import openai_client
from parsers import create_pydantic_parser
from utils import load_yaml


# Seperate to Config yaml
CONFIG_PATH = "./config/default.yaml"


def main():
    config = load_yaml("")
    client = openai_client(config)
    parser, instruction = create_pydantic_parser(get_instruction=True)


if __name__ == "__main__":
    main()
