def copyIterable(iterable):
    return iterable[0::]  # copy
#

class Array(object):
    """
    Constructor
    @:param iterable being the iterable to construct form
    """
    def __init__(self, iterable):
        self.inner = copyIterable(iterable)
    #

    """
    Joins the element into a string
    @:param glue being the string to use as a "glue" between elements
    @:returns a string that represents the elements of this Array glued together using the given glue
    """
    def join(self, glue=", "):
        length = self.length()
        if length == 0: #if there's no elements, return an empty string
            return ""
        elif length == 1: #if there's only one element, return this element as a string
            return str(self[0])
        else: #otherwise, glue the elements together
            ret = str(self[0])
            for i in range(1, length):
                ret += glue + str(self[i])

            return ret
    #

    """
    Determines the size of this Array
    @:returns the size of this Array
    """
    def length(self):
        return len(self)
    #

    """
    Alias of "length"
    @:returns the size of this Array
    """
    def size(self):
        return self.length()
    #

    """
    Determines whether or not the given element appears in this Array
    @:param elemToFind being the element to find
    @:returns True if it appears in this Array, False otherwise
    """
    def contains(self, elemToFind):
        return self.indexOf(elemToFind) >= 0
    #

    """
    Alias of "contains"
    @:param elemToFind being the element to find
    @:returns True if it appears in this Array, False otherwise
    """
    def includes(self, elemToFind):
        return self.contains(elemToFind)
    #

    """
    Adds an element to the end of this Array
    @:param elem being the element to add
    @:returns self
    """
    def push(self, elem):
        self.inner.append(elem)
        return self
    #

    """
    Deletes the last element of this Array
    @:returns the element that was removed
    """
    def pop(self):
        return self.inner.pop()
    #

    """
    Computes the
    """
    def findIndex(self, predicate):
        for index in range(0, len(self)):
            if predicate(self[index]):
                return index
        #

        return -1
    #

    def findLastIndex(self, predicate):
        foundIndex = -1

        for index in range(0, len(self)):
            if predicate(self[index]):
                foundIndex = index
        #

        return foundIndex
    #

    def indexOf(self, elem):
        return self.inner.index(elem)
    #

    def lastIndexOf(self, elem):
        foundIndex = -1

        for index in range(0, len(self)):
            if self[index] == elem:
                foundIndex = index
        #

        return foundIndex
    #

    def forEach(self, functor):
        for elem in self:
            functor(elem)

        return self
    #

    def filter(self, predicate):
        return Array(list(filter(predicate, self.inner)))
    #

    def map(self, mapper):
        return Array(list(map(mapper, self.inner)))
    #

    def reduce(self, reducer, init=None):
        acc = init
        found = init is not None

        for elem in self:
            if not found:
                acc = elem
                found = True
                continue
            #

            acc = reducer(acc, elem)
        #

        return acc
    #


    def reversed(self):
        return Array(reversed(self.inner))
    #

    def reverse(self):
        self.inner.reverse()
        return self
    #

    def sorted(self):
        return Array(sorted(self.inner))
    #

    def sort(self):
        self.inner.sort()
        return self
    #

    def allMatch(self, predicate):
        for elem in self:
            if not predicate(elem):
                return False
        #

        return True
    #

    def every(self, predicate):
        return self.allMatch(predicate)
    #

    def anyMatch(self, predicate):
        for elem in self:
            if predicate(elem):
                return True
        #

        return False
    #

    def some(self, predicate):
        return self.anyMatch(predicate)
    #

    def noneMatch(self, predicate):
        return not self.anyMatch(predicate)
    #

    def toArray(self):
        return copyIterable(self.inner)
    #

    def __len__(self):
        return len(self.inner)
    #

    def __getitem__(self, index):
        return self.inner[index]
    #

    def __setitem__(self, index, value):
        self.inner[index] = value
        return self
    #
#



if __name__ == "__main__":
    a = Array(range(0, 12)) \
        .filter(lambda x: x % 2) \
        .map(lambda x: x + 2) \
        .join(", ")

    print(a)
#



