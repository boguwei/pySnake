# Segment
# 
# author:   boguwei@gmail.com
# date:     3/31/16

from colors import colors

class Segment:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.size = 10

    def copySegment(self, otherSegment):
        self.x = otherSegment.x
        self.y = otherSegment.y
        self.z = otherSegment.z

    def moveSegment(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        if self.z + dz >= 0 and self.z + dz < len(colors):
            self.z += dz

    def printSegment(self):
        print('[ ',str(self.x),' ',str(self.y),' ',str(self.z),' ]')
