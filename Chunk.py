from mcpi.minecraft import Minecraft
from mcpi import block	  

mc = Minecraft.create()
                                            
x, y, z = mc.player.getPos()  

mc.setBlocks(x,y, z, x+20, y+20, z+20, block.AIR.id)
