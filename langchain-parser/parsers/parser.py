from typing import TYPE_CHECKING, Optional, Tuple, Type


if TYPE_CHECKING:
    from pydantic import BaseModel

from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser


def create_pydantic_parser(
    pydantic_class: Type[BaseModel], get_instruction: False
) -> Tuple[PydanticOutputParser, Optional[str]]:
    """
    PydanticOutputParser 객체와 포맷 명령어를 반환하는 함수.

    :param pydantic_class: Pydantic 모델 클래스.
    :param get_inst: 포맷 명령어 반환 여부를 결정하는 플래그 (기본값: False).
                    - True: parser와 함께 포맷 명령어 문자열 반환.
                    - False: parser 객체와 포맷 명령어를 반환.

    :return:
        - PydanticOutputParser 객체
        - 포맷 명령어 문자열 (parser.get_format_instructions() 결과)
    """
    instruction = None
    parser = PydanticOutputParser(pydantic_object=pydantic_class)
    if get_instruction:
        instruction = parser.get_format_instructions()
    return parser, instruction


def create_str_parser():
    return StrOutputParser()
