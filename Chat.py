from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc = Minecraft.create("192.168.7.103", 4711)

mc.postToChat("What is the Answer to Life, the Universe, and Everything?")
mc.postToChat("")
mc.postToChat("")
