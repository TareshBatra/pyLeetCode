# page 25

# Array Based Approach
"""
class StockSpanner:

    def __init__(self):
        self.array = []


    def next(self, price: int) -> int:

        if self.array:

            if price < self.array[-1][0]:
                self.array.append([price,1])
                return 1

            elif price == self.array[-1][0]:
                self.array.append([price,self.array[-1][1] + 1])
                return self.array[-1][1]

            else:
                days = 1

                while days <= len(self.array):
                    if price < self.array[len(self.array) - days][0]:
                        break

                    elif price == self.array[len(self.array) - days][0]:
                        days += self.array[len(self.array) - days][1]
                        break

                    else:
                        days += self.array[len(self.array) - days][1]

                self.array.append([price, days])
                return days

        else:
            self.array.append([price,1])
            return 1

"""
# Using Stack

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:

        if self.stack:

            if price < self.stack[-1][0]:
                self.stack.append([price, 1])
                return 1

            elif price == self.stack[-1][0]:
                days = self.stack[-1][1] + 1
                self.stack.pop()
                self.stack.append([price, days])
                return days

            else:
                days = 1

                while self.stack:
                    if price < self.stack[-1][0]:
                        break

                    elif price == self.stack[-1][0]:
                        days += self.stack[-1][1]
                        self.stack.pop()
                        break

                    else:
                        days += self.stack[-1][1]
                        self.stack.pop()

                self.stack.append([price, days])
                return days

        else:
            self.stack.append([price, 1])
            return 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)