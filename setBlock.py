from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()

mc.setBlock(pos,15)
