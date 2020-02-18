from mcpi.minecraft import Minecraft
from mcpi import block    
from array import *

def init():
     #mc = Minecraft.create()
     mc = Minecraft.create("127.0.0.1", 4711)
     mc.setting("world_immutable",False)
     return mc

def Walls(mc,x,y,z):
	mc.setBlocks(x,y, z+1, x+24, y+3, z+24, 98)
	mc.setBlocks(x+1,y, z+2, x+23, y+3, z+23, 0)
     
'''
def ArrayWalls(mc,x,y,z):
     x, y, z = mc.player.getPos()

     m = [[],
          [],
          [],
          [],
          [],
          
          [],
          [],
          [],
          [],
          [],
          
          [],
          [],
          [],
          [],          
          [],
          
          [],
          [],
          [],
          [],
          [],
          
          [],
          [],
          [],
          [],
          []]
     
     print()

     for k in range (0,25):
          for l  in range (0,25):
               print(m[k][l],end="")
               mc.setBlocks(x,y+k,z+l,x,y+k,z+l,m[k][l])

     mc.player.setPos(x+1,y,z)
     x, y, z = mc.player.getPos()

     m = [[],
          [],
          [],
          [],
          [],
          
          [],
          [],
          [],
          [],
          [],
          
          [],
          [],
          [],
          [],          
          [],
          
          [],
          [],
          [],
          [],
          [],
          
          [],
          [],
          [],
          [],
          []]
     
     print()

     for k in range (0,25):
          for l  in range (0,25):
               print(m[k][l],end="")
               mc.setBlocks(x,y+k,z+l,x,y+k,z+l,m[k][l])


     mc.player.setPos(x,y,z-2)
'''

def WhileTwr(mc,x,y,z):
     done = 0
     x,y,z = mc.player.getPos()
     mc.player.setPos(x+12,y,z+12)
     while(done < 15):
          m = [[0,0,1,1,1,0,0],
               [0,1,0,0,0,1,0],
               [1,0,0,0,0,0,1],
               [1,0,0,0,0,0,1],
               [1,0,0,0,0,0,1],
               [0,1,0,0,0,1,0],
               [0,0,1,1,1,0,0]]
     for h in range (0,7):
          for k  in range (0,7):
               print(m[h][k],end="")
               mc.setBlocks(x+h,y+k,z,x+h,y+k,z,m[h][k])


def main():
     mc = init()
     x, y, z = mc.player.getPos()
     Walls(mc,x,y,z)
     #ArrayWalls(mc,x,y,z)
     WhileTwr(mc,x,y,z)
     
if __name__ == "__main__":
 main()
 
 
'''
h = x
k = y
l = z
'''
