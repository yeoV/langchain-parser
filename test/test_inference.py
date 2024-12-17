import asyncio
import time

import pytest

from langchain_parser.inference import infer_batches_async


class MockChain:
    async def ainvoke(self, input_value: str) -> str:
        await asyncio.sleep(0.1)  # 비동기 호출 시뮬레이션
        return f"Processed: {input_value}"


@pytest.mark.asyncio
async def test_infer_batches_async():
    test_data = [{f"Key{i}": f"Value_{i}"} for i in range(10)]

    mock_chain = MockChain()
    s_time = time.time()
    results = await infer_batches_async(mock_chain, test_data, batch_size=5)
    e_time = time.time()
    expected_results = [{f"Key{i}": f"Processed: Value_{i}"} for i in range(10)]

    assert results == expected_results
    assert e_time - s_time < 1.1
