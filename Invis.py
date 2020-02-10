from mcpi.minecraft import Minecraft
from mcpi import block
import random
from time import sleep

def init():
     #mc = Minecraft.create("192.168.7.226", 4711)
     mc = Minecraft.create("127.0.0.1", 4711)
     mc.setting("world_immutable",False)
     return mc

def While(mc,x,y,z,):
	done = 0
	while(done < 500):
		h = random.randint(0,20)
		l = random.randint(0,20)
		mc.setBlock(x+h,y,z+l,95)
		done = done + 1
		
def main():
     mc = init()
     x, y, z = mc.player.getPos()
     While(mc,x,y,z)
     
if __name__ == "__main__":
 main()
