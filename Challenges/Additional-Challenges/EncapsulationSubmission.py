



class Protected:
    def __init__(self):
        self._protectedVar = 10
        self.__privateVar = 25

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private


obj = Protected()
print(obj._protectedVar)
obj._protectedVar = 30
print(obj._protectedVar)
obj.getPrivate()
obj.setPrivate(50)
obj.getPrivate()
