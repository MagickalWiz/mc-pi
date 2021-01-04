from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import random

def init():
    ip = "127.0.0.1"
    mc = Minecraft.create(ip, 4711)
    mc.setting("world_immutable",True)
    x, y, z = mc.player.getPos()        
    return mc
    
def clearAir(mc,x,y,z):
  mc.setBlocks(x,y,z,x+10,y+10,z+10,0)

def matrix(mc,x,y,z):
  
  X = ["1000000002",
       "0000000000",
       "0000000000",
       "0000000000",
       "0000005000",
       "0000000000",
       "0005000000",
       "0000000000",
       "0000000000",
       "4000000003"]
      #"123456789A"
 
  y1 = 10
  for h in range (0,10):
    x1 = 10
    for k  in range (0,10):
      print(X[h][k],end="") # debug
      #print(h,k," ",end="")
      theBlock = X[h][k]
      c = 0
      if (theBlock == "1"):
        c = random.randint(0,19)
      if (theBlock == "2"):
        c = random.randint(20,39)
      if (theBlock == "3"):
        c = random.randint(40,59)
      if (theBlock == "4"):
        c = random.randint(60,79)
      if (theBlock == "5"):
        c = random.randint(80,98)
      mc.setBlock(x1-x,y1+y,z,35,c)
      x1 = x1 - 1
    y1 = y1 - 1
    print()
    
def main():
  mc = init()
  x,y,z = mc.player.getPos()
  clearAir(mc,x,y,z)
  matrix(mc,x,y,z+5)
  mc.player.setPos(x,y,z-5)

if __name__ == "__main__":
  main()
