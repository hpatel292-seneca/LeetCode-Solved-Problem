class StockSpanner(object):

    def __init__(self):
        self.stack=[]


    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if not self.stack:
            self.stack.append([price, 1])
            return 1
        else:
            total=1
            while self.stack and price>=self.stack[-1][0]:
                j=self.stack.pop()
                total+=j[1]
            self.stack.append([price, total])
            return total


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)