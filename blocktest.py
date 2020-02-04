from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
                                            
x, y, z = mc.player.getPos()  

mc.setBlocks(x,y, z, x+1, y, z, block.ICE.id)
