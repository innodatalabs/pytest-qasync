# pytest-qasync

Pytest plugin to test [qasync](https://pypi.org/project/qasync/).

## Example

```
import pytest

async def coro():
    return 1

@pytest.mark.qasync
async def test_qasync():
    res = await coro()
    assert res == 1
```

## Disclaimer

Code mostly stolen from [pytest-asyncio](https://pypi.org/project/pytest-asyncio) project.


