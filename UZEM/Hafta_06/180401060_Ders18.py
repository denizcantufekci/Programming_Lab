class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + (self.name) + ', ' + str(self.value) + ', ' + str(self.weight) + '>'
        return result


def maxValue(toConsider, avail):
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        result = maxValue(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxValue(toConsider[1:], (avail - nextItem.getWeight()))
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxValue(toConsider[1:], avail)
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result
    
    
def smallTest():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    val, taken = maxValue(Items, 5)
    for item in taken:
        print(item)
    print("Total value of items taken = ", val)
    
    
#smallTest()  
