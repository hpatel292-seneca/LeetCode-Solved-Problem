import random
class RandomizedSet(object):

    def __init__(self):
        self.hashMap={}
        self.list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        exist = val not in self.hashMap
        if exist:
            self.hashMap[val]=len(self.list)
            self.list.append(val)
        return exist


    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        res = val in self.hashMap
        if res:
            idx = self.hashMap[val]
            lastval = self.list[-1]
            self.list[idx] = lastval
            self.list.pop()
            self.hashMap[lastval] = idx
            del self.hashMap[val]
        return res
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


ab = RandomizedSet()
print(ab.insert(1))
print(ab.remove(2))
          