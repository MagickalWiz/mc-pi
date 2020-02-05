from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    mc.setting("world_immutable",True)
    x, y, z = mc.player.getPos()
    return mc

def blockFunction(mc,x,y,z):
    m = [(35,1),(35,2),(35,3),(35,4),(35,5),(35,6),(35,7),(35,8),(35,9),(35,10)]
    print("LIST m LENGTH = ",len(m))
    for l in range (0,len(m)):
            print(m[l]," ",end="")
            mc.setBlock(x,y,z+l,m[l])

def main():
    mc = init()
    pos = mc.player.getPos()
    mc.postToChat(pos)
    x,y,z = mc.player.getPos() 
    blockFunction(mc,x+5,y+5,z+5)
    h,k,l = x,y+5,z
    mc.player.setPos(h,k,l) 

if __name__ == "__main__":
    main()
