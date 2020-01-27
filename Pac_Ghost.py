from mcpi.minecraft import Minecraft
from mcpi import block    
from array import *

mc = Minecraft.create()
                                            
x, y, z = mc.player.getPos()

m = [[0,(35,3),(35,3),0,0,0, (35,3),(35,3), 0,0,0,(35,3),(35,3),0],
     [(35,3),(35,3),(35,3),(35,3),0,(35,3), (35,3),(35,3), (35,3),0,(35,3),(35,3),(35,3),(35,3)],
     [(35,3),(35,3),(35,3),(35,3),(35,3),(35,3), (35,3),(35,3), (35,3),(35,3),(35,3),(35,3),(35,3),(35,3)],
     [(35,3),(35,3),(35,3),(35,3),(35,3),(35,3), (35,3),(35,3), (35,3),(35,3),(35,3),(35,3),(35,3),(35,3)],
     [(35,3),(35,3),(35,3),(35,3),(35,3),(35,3), (35,3),(35,3), (35,3),(35,3),(35,3),(35,3),(35,3),(35,3)],
     [(35,3),(35,3),35,35,(35,3),(35,3), (35,3),(35,3), (35,3),35,35,(35,3),(35,3),(35,3)],
     [(35,3),(35,15),(35,15),35,35,(35,3), (35,3),(35,3), (35,15),(35,15),35,35,(35,3),(35,3)],
     [0,(35,15),(35,15),35,35,(35,3), (35,3),(35,3),(35,15),(35,15),35,35,(35,3),0],
     [0,35,35,35,35,(35,3), (35,3),(35,3), 35,35,35,35,(35,3),0],
     [0,(35,3),35,35,(35,3),(35,3), (35,3),(35,3), (35,3),35,35,(35,3),(35,3),0],     
     [0,0,(35,3),(35,3),(35,3),(35,3), (35,3),(35,3), (35,3),(35,3),(35,3),(35,3),0,0],
     [0,0,0,(35,3),(35,3),(35,3), (35,3),(35,3), (35,3),(35,3),(35,3),0,0,0],
     [0,0,0,0,0,(35,3), (35,3),(35,3), (35,3),0,0,0,0,0]]

print()

for k in range (0,13):
     for l  in range (0,14):
          print(m[k][l],end="")
          mc.setBlocks(x,y+k,z+l,x,y+k,z+l,m[k][l])

'''
print()

for k in range (0,10):
	for l  in range (0,2):
		print(m[k][l],end="")
		mc.setBlocks(x,y, z, x,y,z,m[k][l])

	print()
'''

mc.player.setPos(x,y,z-2)

'''
h = rows
l = columns

wool: white: 35
      black: ,15
      light blue: ,3
      blue: ,11
'''
