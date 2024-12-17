from __future__ import annotations

from typing import Any, ClassVar, Dict, Optional

from langchain_openai import OpenAI
from pydantic import BaseModel, ConfigDict, Field


class OpenAIConfig(BaseModel):
    additional_option: ClassVar[ConfigDict] = ConfigDict(extra="allow")

    model: str = Field(description="사용할 OpenAI 모델의 이름 (예: gpt-3.5-turbo).")
    base_url: str = Field(
        description="Model API의 기본 URL (예: https://localhost:8080)."
    )
    api_key: str = Field(
        description="요청을 인증하는 데 필요한 API 키.", default="None"
    )
    max_tokens: Optional[int] = Field(
        description="응답에서 허용되는 최대 토큰 수", default=0.7
    )
    temperature: Optional[float | int] = Field(
        description="출력의 랜덤성을 제어 default 0.7"
    )


def openai_model(config: Dict[str, Any]) -> OpenAI:
    return OpenAI(**OpenAIConfig(**config).model_dump())
