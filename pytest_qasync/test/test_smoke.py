import pytest
import qasync
import asyncio
import pytest_qasync.plugin

async def coro():
    return 1

def test_event_loop(event_loop):
    assert type(event_loop) is qasync.QEventLoop
    result = event_loop.run_until_complete(coro())
    assert result == 1


@pytest.mark.qasync
async def test_smoke(event_loop):
    result = await coro()
    assert result == 1


@pytest.mark.xfail(reason="testing failure", strict=True)
@pytest.mark.qasync
async def test_fail():
    result = await coro()
    assert result == 2

