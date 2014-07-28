from .connection import Connection


class CommandError(RuntimeError):
    pass


class Command:
    """
    The command base class.
    """
    func_prefix = ''

    def __init__(self, connection):
        self.conn = connection

    def _send(self, func, *args):
        full_func = '%s.%s' % (self.func_prefix, func)
        self.conn.send(full_func, *args)

    def _send_receive(self, func, *args):
        full_func = '%s.%s' % (self.func_prefix, func)
        return self.conn.send_receive(full_func, *args)


class WorldCommand(Command):
    func_prefix = 'world'

    def get_block(self, x, y, z) -> int:
        return int(self._send_receive('getBlock', x, y, z))

    def set_block(self, x, y, z, block_type) -> None:
        self._send('setBlock', x, y, z, block_type)

    def set_blocks(self, x1, y1, z1, x2, y2, z2, block_type) -> None:
        self._send('setBlocks', x1, y1, z1, x2, y2, z2, block_type)

    def get_height(self, x, z) -> int:
        return int(self._send_receive('getHeight', x, z))

    def save_checkpoint(self) -> None:
        self._send('saveCheckpoint')

    def restore_checkpoint(self) -> None:
        self._send('restoreCheckpoint')

    def setting(self) -> None:
        # TODO what does this do?
        pass


class ChatCommand(Command):
    func_prefix = 'chat'

    def post(self, message) -> None:
        self._send('post', message)
        pass


class Minecraft:

    def __init__(self, ip='127.0.0.1', port=4711):
        conn = Connection(ip, port)
        self.world = WorldCommand(conn)
        self.chat = ChatCommand(conn)
