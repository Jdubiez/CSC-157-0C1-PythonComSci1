from regPolygon import *


rp = RegPolygon(6)

rp.setRadius(2)
print(rp)

rp.setSide(4)	
print(rp)

rp.setApothem(3)
print(rp)

rp = RegPolygon(8)
rp.setSide(10)	

rp.draw()


