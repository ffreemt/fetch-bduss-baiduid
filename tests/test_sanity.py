''' sanity check
'''
import pytest

from fetch_bduss_id import fetch_bduss_id


@pytest.mark.asyncio
async def test_sanity():
    ''' sanity check '''
    await fetch_bduss_id()
    assert 1
