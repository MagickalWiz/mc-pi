from mcpi.minecraft import Minecraft
from mcpi import block

#mc = Minecraft.create("127.0.0.1", 4711)
#mc = Minecraft.create("192.168.7.103", 4711)
mc = Minecraft.create()
                                            
x, y, z = mc.player.getPos()  

mc.setBlocks(x,y, z, x+20, y+20, z+20, block.AIR.id)
