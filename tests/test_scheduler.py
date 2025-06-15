import asyncio
import pytest
from unittest.mock import patch, Mock
from src.scheduler.scheduler import MindshareScheduler

@pytest.fixture
def scheduler():
    with patch.dict('os.environ', {
        'KAITO_API_KEY': 'test_key',
        'AGENT_PATH': 'test_agent_path',
        'INTENT_ACCOUNT_ID': 'acc',
        'INTENT_PRIVATE_KEY': 'key',
        'NETWORK': 'testnet'
    }):
        return MindshareScheduler(interval=1)


def test_scheduler_initialization(scheduler):
    assert scheduler.interval == 1
    assert scheduler.api_key == 'test_key'
    assert scheduler.agent_path.endswith('src/agent')


@patch('subprocess.run')
def test_execute_agent_success(mock_run, scheduler):
    mock_process = Mock()
    mock_process.returncode = 0
    mock_process.stdout = "Success output"
    mock_run.return_value = mock_process

    asyncio.run(scheduler.execute_agent())

    assert mock_run.call_count == 3
    args = mock_run.call_args[0][0]
    assert "nearai" in args
    assert "agent" in args
    assert "task" in args
