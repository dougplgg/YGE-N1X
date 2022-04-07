from discord.ext.commands.errors import CheckFailure


class NotConnectedToVoice(CheckFailure):
    """User not connected to any voice channel"""

    pass


class PlayerNotConnected(CheckFailure):
    """Player not connected"""

    pass


class MustBeSameChannel(CheckFailure):
    """Player and user not in same channel and his fuck my dick"""

    pass
