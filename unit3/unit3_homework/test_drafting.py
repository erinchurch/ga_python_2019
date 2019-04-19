class howDictionariesWork:
    name = {
            1:"erin",
            2:"church",
            3:"stuff",
           }
    print("checking class level dictinary.\t", name.items())
    def has_dictinary(self):
        self.name
        print("in dictionary method")
        print(self.name.items())
        return self.name

    def print(self, d):
        print(d.items())


a = howDictionariesWork
b = howDictionariesWork.has_dictinary(a)
howDictionariesWork.print(a,b)