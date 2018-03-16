"""
Creates a copy of an iterable
@:param iterable being the iterable to copy from
@:returns a copy of the given iterable
"""
def copyIterable(iterable):
    #return iterable[0::]  # copy
    return list(iterable)
#

"""
A class that represents iterables as handy objects
"""
class Array(object):
    """
    Create an Array from an iterable
    @:param iterable being the iterable to construct from
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
        if length == 0:
            return ""
        elif length == 1:
            return str(self[0])
        else:
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
    Computes the index of an element from a predicate
    @:param predicate used to determine the index
    @:returns -1 if no element satisfied the predicate, otherwise, the index of the first element that satisfied the predicate
    """
    def findIndex(self, predicate):
        for index in range(0, len(self)):
            if predicate(self[index]):
                return index
        #

        return -1
    #

    """
    Computes the index of the last element that satisfies the given predicate
    @:param predicate being the function used to determine the index
    @:returns -1 if no element satisfied the predicate, otherwise, the index of the last element that satisfied the predicate
    """
    def findLastIndex(self, predicate):
        foundIndex = -1

        for index in range(0, len(self)):
            if predicate(self[index]):
                foundIndex = index
        #

        return foundIndex
    #

    """
    Computes the first index of the given element
    @:param elem being the element from which we desire to know the index
    @:returns -1 if the given element is not in the Array, its first index if it was found
    """
    def indexOf(self, elem):
        return self.inner.index(elem)
    #

    """
    Computes the last index of the given element
    @:param elem being the element from which we desire to know the index
    @:returns -1 if the given element is not in the Array, its last index if it was found
    """
    def lastIndexOf(self, elem):
        foundIndex = -1

        for index in range(0, len(self)):
            if self[index] == elem:
                foundIndex = index
        #

        return foundIndex
    #

    """
    Applies a function to each element of this Array
    @:param functor being the function applied to each element
    @:returns self
    """
    def forEach(self, functor):
        for elem in self:
            functor(elem)

        return self
    #

    """
    Filters the elements of this Array according to a given predicate
    @:param predicate being the function used to determine whether an element should be kept in the array
    @:returns a filtered Array
    """
    def filter(self, predicate):
        return Array(list(filter(predicate, self.inner)))
    #

    """
    Maps the elements of this Array according to a mapper function
    @:param mapper being the function that transforms each element to a new value
    @:returns a mapped Array
    """
    def map(self, mapper):
        return Array(list(map(mapper, self.inner)))
    #

    """
    Reduces this Array to a single value according to a reducer function
    @:param reducer being the function applied on each element in order to retrieve the value
    @:param init being the initial value of the accumulator (defaulted to None and will use the first element of the Array)
    @:return the reduced value
    """
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


    """
    Creates a reversed copy of this Array
    @:returns the reversed Array
    """
    def reversed(self):
        return Array(reversed(self.inner))
    #

    """
    Reverses this Array in-place
    @returns self
    """
    def reverse(self):
        self.inner.reverse()
        return self
    #

    """
    Creates a sorted copy
    @returns the sorted Array
    """
    def sorted(self):
        return Array(sorted(self.inner))
    #

    """
    Sorts this Array in-place
    @:returns self
    """
    def sort(self):
        self.inner.sort()
        return self
    #

    """
    Determines whether or not each element of this Array satisfies the given predicate
    @:param predicate being the predicate to satisfy
    @:returns True if each element satisfies the predicate, False otherwise
    """
    def allMatch(self, predicate):
        for elem in self:
            if not predicate(elem):
                return False
        #

        return True
    #

    """
    Alias of "allMatch"
    @:param predicate being the predicate to satisfy
    @:returns True if each element satisfies the predicate, False otherwise
    """
    def every(self, predicate):
        return self.allMatch(predicate)
    #

    """
    Determines whether or not any element of this Array satisfies the given predicate
    @:param predicate being the predicate to satisfy
    @:returns True if at least one element satisfies the predicate, False otherwise
    """
    def anyMatch(self, predicate):
        for elem in self:
            if predicate(elem):
                return True
        #

        return False
    #

    """
    Alias of "anyMatch"
    @:param predicate being the predicate to satisfy
    @:returns True if at least one element satisfies the predicate, False otherwise
    """
    def some(self, predicate):
        return self.anyMatch(predicate)
    #

    """
    Determines whether or not no element of this Array satisfies the given predicate
    @:param predicate being the predicate to never satisfy
    @:returns True if no element satisfies the predicate, False otherwise
    """
    def noneMatch(self, predicate):
        return not self.anyMatch(predicate)
    #

    """
    Converts this Array to a native array
    @:returns this Array as a native array
    """
    def toArray(self):
        return copyIterable(self.inner)
    #

    """
    Hook to allow the use of the len() function on an Array
    """
    def __len__(self):
        return len(self.inner)
    #

    """
    Overload of the subscript operator to retrieve a value from its index
    @:param index being the index of the element to retrieve
    @:returns the desired item
    """
    def __getitem__(self, index):
        return self.inner[index]
    #

    """
    Overload of the subscript operator to set the value associated to the given index
    @:param index being the index to which we will associate the given value
    @:param value being the new value of the element at the given index
    """
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