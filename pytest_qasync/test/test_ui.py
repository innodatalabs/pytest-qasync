import pytest
import qasync
import asyncio


if qasync.QtModuleName == 'PyQt5':
    from PyQt5.QtWidgets import QProgressBar

elif qasync.QtModuleName == 'PySide2':
    from PySide2.QtWidgets import QProgressBar

elif qasync.QtModuleName == 'PySide6':
    from PySide6.QtWidgets import QProgressBar

else:
    raise NotImplementedError(qasync.QtModuleName)


@pytest.mark.qasync
async def test_progress_bar():
    bar = QProgressBar()
    bar.show()

    for val in range(100):
        await asyncio.sleep(0.01)
        bar.setValue(val)
