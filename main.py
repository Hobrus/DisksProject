import asyncio
from unittest.mock import AsyncMock
import aioredis
import pytest


@pytest.fixture
async def redis(mocker):
    redis_mock = AsyncMock(spec=aioredis.Redis)
    mocker.patch('aioredis.from_url', return_value=redis_mock)
    return redis_mock


@pytest.mark.asyncio
async def test_set_and_get(redis):
    await redis.set('key', 'value')
    redis.set.assert_called_once_with('key', 'value')

    redis.get.return_value = b'value'
    value = await redis.get('key')
    assert value == b'value'


@pytest.mark.asyncio
async def test_incr(redis):
    redis.get.return_value = b'1'
    await redis.incr('counter')
    redis.incr.assert_called_once_with('counter')
    value = await redis.get('counter')
    assert value == b'1'


@pytest.mark.asyncio
async def test_hset_and_hget(redis):
    await redis.hset('hash', 'field', 'value')
    redis.hset.assert_called_once_with('hash', 'field', 'value')

    redis.hget.return_value = b'value'
    value = await redis.hget('hash', 'field')
    assert value == b'value'


@pytest.mark.asyncio
async def test_lpush_and_lpop(redis):
    redis.lpop.side_effect = [b'item2', b'item1']
    await redis.lpush('list', 'item1')
    await redis.lpush('list', 'item2')
    redis.lpush.assert_any_call('list', 'item1')
    redis.lpush.assert_any_call('list', 'item2')

    value = await redis.lpop('list')
    assert value == b'item2'
    value = await redis.lpop('list')
    assert value == b'item1'