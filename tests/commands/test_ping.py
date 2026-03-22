import pytest
from unittest.mock import AsyncMock, MagicMock
from commands.ping import Ping

@pytest.mark.asyncio
async def test_ping_command():
    # 1. Setup mocks
    bot = MagicMock()
    cog = Ping(bot)
    interaction = AsyncMock()
    
    # 2. Execute the command
    await cog.ping.callback(cog, interaction) # type: ignore

    # 3. Assertions
    interaction.response.send_message.assert_called_once_with("Pong!")