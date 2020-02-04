from mcpi.minecraft import Minecraft
from mcpi import block    
from array import *

#mc = Minecraft.create()
mc = Minecraft.create("127.0.0.1", 4711)
mc.setting("world_immutable",False)
                                            
x, y, z = mc.player.getPos()

m = [[(46,9),0,(46,9),0,0,(46,9),0,0,(46,9)],
     [(46,9),0,(46,9),0,0,(46,9),0,0,0],
     [(46,9),(46,9),(46,9),0,0,(46,9),0,0,(46,9)],
     [(46,9),0,(46,9),0,0,0,0,0,(46,9)],
     [(46,9),0,(46,9),0,0,(46,9),0,0,(46,9)]]

print()

for k in range (0,5):
     for l  in range (0,9):
          print(m[k][l],end="")
          mc.setBlocks(x,y+k,z+l,x,y+k,z+l,m[k][l])

mc.player.setPos(x,y,z-2)
