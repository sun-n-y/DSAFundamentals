class MyClass:
    # constructor
    # self is passed in every method of a class, like this keyword
        def __init__(self, nums):
            # create member variables
            self.nums = nums
            self.size = len(nums)

        # method for this class
        # self keyword required as param, to get access to member variables
        def getLenght(self):
            return self.size

        # call member function from another function
        def getDoubleLenght(self):
            return 2 * self.getLenght()

p1 = MyClass([1,2,3])

print(p1.getDoubleLenght())



