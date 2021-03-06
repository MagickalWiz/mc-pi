from mcpi.minecraft import Minecraft
from mcpi import block    
from array import *

def init():
     #mc = Minecraft.create()
     mc = Minecraft.create("127.0.0.1", 4711)
     mc.setting("world_immutable",True)
     return mc
     
def pacMan(mc,x,y,z):
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

     mc.player.setPos(x+1,y,z)
     x, y, z = mc.player.getPos()

     m = [[0,(35,11),(35,11),0,0,0, (35,11),(35,11), 0,0,0,(35,11),(35,11),0],
          [(35,11),(35,11),(35,11),(35,11),0,(35,11), (35,11),(35,11), (35,11),0,(35,11),(35,11),(35,11),(35,11)],
          [(35,11),(35,11),(35,11),(35,11),(35,11),(35,11), (35,11),(35,11), (35,11),(35,11),(35,11),(35,11),(35,11),(35,11)],
          [(35,11),35,(35,11),(35,11),35,35, (35,11),(35,11), 35,35,(35,11),(35,11),35,(35,11)],
          [(35,11),(35,11),35,35,(35,11),(35,11), 35,35, (35,11),(35,11),35,35,(35,11),(35,11)],
          [(35,11),(35,11),(35,11),(35,11),(35,11),(35,11), (35,11),(35,11), (35,11),(35,11),(35,11),(35,11),(35,11),(35,11)],
          [(35,11),(35,11),(35,11),(35,11),(35,11),(35,11), (35,11),(35,11), (35,11),(35,11),(35,11),(35,11),(35,11),(35,11)],
          [0,(35,11),(35,11),(35,11),35,35, (35,11),(35,11), 35,35,(35,11),(35,11),(35,11),0],
          [0,(35,11),(35,11),(35,11),35,35, (35,11),(35,11), 35,35,(35,11),(35,11),(35,11),0],
          [0,(35,11),(35,11),(35,11),(35,11),(35,11), (35,11),(35,11), (35,11),(35,11),(35,11),(35,11),(35,11),0],     
          [0,0,(35,11),(35,11),(35,11),(35,11), (35,11),(35,11), (35,11),(35,11),(35,11),(35,11),0,0],
          [0,0,0,(35,11),(35,11),(35,11), (35,11),(35,11), (35,11),(35,11),(35,11),0,0,0],
          [0,0,0,0,0,(35,11), (35,11),(35,11), (35,11),0,0,0,0,0]]



     print()

     for k in range (0,13):
          for l  in range (0,14):
               print(m[k][l],end="")
               mc.setBlocks(x,y+k,z+l,x,y+k,z+l,m[k][l])



     mc.player.setPos(x,y,z-2)

def main():
     mc = init()
     x, y, z = mc.player.getPos()
     pacMan(mc,x,y,z)
     
if __name__ == "__main__":
 main()
 
 
'''
h = rows
l = columns

wool: white: 35
      black: ,15
      light blue: ,3
      blue: ,11
'''
