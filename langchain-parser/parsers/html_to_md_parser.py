from pydantic import BaseModel, Field


# description 잘 작성해야함. -> langchain prompt에 들어감
class HtmlToMdParser(BaseModel):
    output: str = Field(description="")
    rules: str = Field(description="")
