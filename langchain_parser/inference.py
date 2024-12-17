import asyncio
from typing import Dict, List

from langchain_core.runnables.base import RunnableSerializable


def infer_single_sync(chain: RunnableSerializable, input: Dict[str, str]) -> str:
    """
    Args:
    chain (RunnableSerializable): Langchain 에 chain 담당 객체.
    input (Dict[str, str]): 입력 데이터 목록.
        - 각 input은 key: value 형식의 Dict 타입이어야 합니다.
        - 예시: {"key1": "value1"}


    Returns:
        Str : llm 추론 후 결과를 String으로 반환
    """
    return chain.invoke(input)


async def infer_multiple_async(
    chain: RunnableSerializable, inputs: List[Dict[str, str]]
) -> List[str]:
    """
    Args:
    chain (RunnableSerializable): Langchain 에 chain 담당 객체.
    inputs (List[Dict[str, str]]): 입력 데이터 목록.
        - 각 input은 key: value 형식의 Dict 타입이어야 합니다.
        - 예시: [{"key1": "value1"}, {"key2": "value2"}]


    Returns:
        List[Any]: 모든 비동기 작업의 결과를 리스트로 반환.
    """

    async def _call(input):
        k, v = next(iter(input.items()))
        res = await chain.ainvoke(v)
        return {k: res}

    tasks = [_call(input) for input in inputs]
    return await asyncio.gather(*tasks, return_exceptions=False)


def _split_list_into_batches(data, batch_size: int):
    for i in range(0, len(data), batch_size):
        yield data[i : i + batch_size]


async def infer_batches_async(
    chain: RunnableSerializable, data: List[Dict[str, str]], batch_size=100
) -> List:
    results = []
    for batch in _split_list_into_batches(data, batch_size):
        batch_result = await infer_multiple_async(chain, batch)
        results.extend(batch_result)
    return results
