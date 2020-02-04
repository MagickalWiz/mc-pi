from mcpi.minecraft import Minecraft
from mcpi import block	  

mc = Minecraft.create()
                                            
x, y, z = mc.player.getPos()

mc.setBlocks(x,y, z+1, x+3, y+4, z+1, block.WATER.id)
mc.setBlocks(x,y, z+1, x+3, y+4, z+1, block.LAVA.id)
mc.setBlocks(x+3,y+4, z+1, x+3, y+4, z+1, block.OBSIDIAN.id)
mc.setBlocks(x+1,y+1, z+1, x+2, y+3, z+1, block.AIR.id)
mc.setBlocks(x+1,y+1, z+1, x+2, y+1, z+1, block.FIRE.id)
