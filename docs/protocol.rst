Minecraft Pi Protocol Specification
===================================

This is a quick documentation of the Minecraft Pi protocol. In theory there is a
documentation in the download archive provided by Mojang, but in practice the
documentation is partially wrong, and there are some available API calls that
are undocumented. So here is a version that I found to be working.

Some parts are taken directly from ``mcpi_protocol_spec.txt``.

Communication
-------------

- Connect a TCP socket to port 4711.
- Commands plain text lines, encoded with ASCII and terminated by LF.

Types
-----

- x,y,z -- Vector of three integers.
- xf,yf,zf -- Vector of three floats.
- blockTypeId -- Integer 0-108.
- blockData -- Integer 0-15.

More information about the block type and block data IDs can be found here:
http://minecraft.gamepedia.com/Data_values_(Pocket_Edition)

Most coordinates are in the form of a three integer vector ``X,Y,Z`` which
address a specific tile in the game world. ``0,0,0`` is the spawn point sea
level. (X,Z) is the ground plane and Y is towards the sky.

Commands
--------

The following commands are in the format ``name(args,[optargs]) --> return_value``.

**World**

::

    world.getBlock(x,y,z) --> blockTypeId

    world.setBlock(x,y,z,blockTypeId)
    world.setBlock(x,y,z,blockTypeId,blockData)

    world.setBlocks(x1,y1,z1,x2,y2,z2,blockTypeId)
    world.setBlocks(x1,y1,z1,x2,y2,z2,blockTypeId,blockData)

    world.getHeight(x,z) --> Integer

    world.checkpoint.save()
    world.checkpoint.restore()

    world.setting(KEY,0/1)

**Chat**

::

    chat.post(message)

**Camera**

::

    camera.mode.setNormal([entityId])
    camera.mode.setFixed()
    camera.mode.setFollow([entityId])
    camera.mode.setPos(x,y,z,)

**Player**

::

    player.getTile() --> x,y,z
    player.setTile(x,y,z)

    player.getPos() --> xf,yf,zf
    player.setPos(xf,yf,zf)
