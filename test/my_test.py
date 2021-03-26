class Logic(object):

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.perforGate()
        return self.output


class Basic(Logic):

    def __init__(self, n):
        Logic.__init__(self, n)
        self.prinA = None
        self.prinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))


class Basic2(Logic):

    def __init__(self, n):
        Logic.__init__(self, n)
        self.basic2 = None

    def get_basic2(self):
        return input(("Enter Pin input for gate "+ self.getLabel()+"-->"))


if __name__ == '__main__':

    B2 = Basic2('123')
    print(B2.get_basic2())

a_li = [11,56,4,1,3,12,45,8,45]
b_li = [123,45,78,95,11,51,61]
min_value = a_li[0]
for i in a_li:
    for j in b_li:
        pass
print(min_value)