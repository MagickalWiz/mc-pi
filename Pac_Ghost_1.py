from mcpi.minecraft import Minecraft
from mcpi import block    
from array import *

def init():
     mc = Minecraft.create()
     return mc


def matrixTop(mc,x,y,z):
    m = [[1,1,1,1,1,1,1,1,1,1],
     [0,1,1,1,1,1,1,1,1,1],
     [0,0,0,0,0,0,0,0,1,1],
     [1,1,1,1,1,1,1,0,0,1],
     [1,1,1,0,1,1,1,0,1,1],
     [1,1,1,0,1,1,1,0,0,1],
     [1,1,1,0,0,0,0,0,1,1],
     [1,1,1,1,1,1,1,0,0,1],
     [1,1,1,1,1,1,1,1,0,1],
     [1,1,1,1,1,1,1,1,1,1]]
    print(m)
    for h in range (0,10):
        for l  in range (0,10):
            print(m[h][l],end="")
            mc.setBlocks(x+h,y-5, z+l, x+h,y+20,z+l,m[h][l])

    print()
    mc.setBlocks(x-1,y-5, z-1, x+11,y-5,z+11,89)
    mc.setBlocks(x-1,y+10, z-1, x+11,y+10,z+11,89)
    mc.setBlocks(x-1,y+20, z-1, x+11,y+20,z+11,89)


def pacMan(mc,x,y,z):
     mc.player.setPos(x,y,z-2)
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
               
def main():
     mc = init()
     x, y, z = mc.player.getPos()
     pacMan(mc,x,y,z)
     
if __name__ == "__main__":
 main()
'''
print()

for k in range (0,10):
	for l  in range (0,2):
		print(m[k][l],end="")
		mc.setBlocks(x,y, z, x,y,z,m[k][l])

	print()
'''



'''
h = rows
l = columns

wool: white: 35
      black: ,15
      light blue: ,3
      blue: ,11
'''
