import pytest
from unittest.mock import AsyncMock, MagicMock
from commands.hello import Hello

@pytest.mark.asyncio
async def test_hello_command():
    bot = MagicMock()
    cog = Hello(bot)
    
    # Mock the interaction and the user triggering it
    interaction = AsyncMock()
    interaction.user.display_name = "Lexi"
    
    await cog.hello.callback(cog, interaction) # type: ignore

    interaction.response.send_message.assert_called_once_with("Hello Lexi!")