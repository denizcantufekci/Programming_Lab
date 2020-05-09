import random

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


def buildManyItems(numItems, maxVal, maxWeight):
    items = []
    for i in range(numItems):
        items.append(Item(str(i), random.randint(1, maxVal), random.randint(1, maxWeight)))
    return items


def bigTest_rec(numItems):
    items = buildManyItems(numItems, 10, 10)
    val, taken = maxValue(items, 40)
    print("Items taken")
    for item in taken:
        print(item)
    print("Total value of items taken = ", val)


def fastMaxVal(toConsider, avail, memo={}):
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = fastMaxVal(toConsider[1:], (avail - nextItem.getWeight()), memo)
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail, memo)
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result


def bigTest_dyn(numItems):
    items = buildManyItems(numItems, 10, 10)
    val, taken = fastMaxVal(items, 40)
    print("Items taken")
    for item in taken:
        print(item)
    print("Total value of items taken = ", val)   
    
    
bigTest_rec(4)
print("---------")
bigTest_dyn(4)
