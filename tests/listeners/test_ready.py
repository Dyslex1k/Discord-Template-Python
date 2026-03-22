import pytest
from unittest.mock import MagicMock
from listeners.ready import ReadyListener

@pytest.mark.asyncio
async def test_on_ready_listener(capsys: pytest.CaptureFixture[str]):
    # Mock the bot and its user property
    bot = MagicMock()
    bot.user = "TestBot#1234"
    
    cog = ReadyListener(bot)
    
    # Trigger the event
    await cog.on_ready()

    # Verify the print statement output
    captured = capsys.readouterr()
    assert "Ready! Logged in as TestBot#1234" in captured.out