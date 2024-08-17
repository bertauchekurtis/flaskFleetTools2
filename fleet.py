# fleet.py
from plane import Plane

class Fleet:
    def __init__(self) -> None:
        self.planes = {}

    def addTypeToFleet(self, newType: Plane, count = 0):
        if newType not in self.planes.keys():
            self.planes[newType] = count

    def updateTypeCount(self, type: Plane, newCount):
        if type in self.planes.keys():
            self.planes[type] = newCount

    def getCountOfType(self, type: Plane) -> int:
        if type not in self.planes.keys():
            return 0
        else:
            return self.planes[type]

