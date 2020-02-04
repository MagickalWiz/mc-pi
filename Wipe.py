from mcpi.minecraft import Minecraft
from mcpi import block

#mc = Minecraft.create("127.0.0.1", 4711)
#mc = Minecraft.create("192.168.7.103", 4711)
mc = Minecraft.create()

x, y, z = mc.player.getPos()  

confirm = input("This will destructionize your world; Please be at coordinates 0,0,0 before confirming. Press 1 to confirm: ")
if (confirm == 1):
	mc.setBlocks(x-1000,y+1000, z-1000, x+1000, y-62, z+1000, block.AIR.id)
	mc.setBlocks(x,y-2, z, x, y-2, z, block.BEDROCK.id)
	#mc.setBlocks(x-1000,y-62,z-1000, x+1000,y-62,z+1000, 46,9)
