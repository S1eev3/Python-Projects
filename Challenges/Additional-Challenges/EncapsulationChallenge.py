
# defining class with protected and private variables
class Parent:
    def __init__(self):
        # protected variable
        self._protVar = 10
        # private variable
        self.__privVar = 20


        # Displaying the original protected value
        print("Here is the original protected value: {}".format(self._protVar))

        # Modifying the protected value
        self._protVar = 15
        print("Here is that protected value changed: {}".format(self._protVar))

        # Displaying the original private value
        def getPrivate(self):
            print(self.__privVar)



if __name__ == "__main__":
    obj = Parent()
    obj.getPrivate()


    

    
