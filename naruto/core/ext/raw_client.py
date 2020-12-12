
__all__ = ['RawClient']

import time
from typing import Optional

from pyrogram import Client

import naruto  # pylint: disable=unused-import


class RawClient(Client):
    """ naruto raw client """
    DUAL_MODE = False
    LAST_OUTGOING_TIME = time.time()

    def __init__(self, bot: Optional['naruto.core.client._narutoBot'] = None, **kwargs) -> None:
        self._bot = bot
        super().__init__(**kwargs)
        self._channel = naruto.core.types.new.ChannelLogger(self, "CORE")
        naruto.core.types.new.Conversation.init(self)
