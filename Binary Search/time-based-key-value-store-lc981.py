# page 35

class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = []
        self.hash[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result, values = "", self.hash.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:  # to make sure that we get the largest prev time step value
                result = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return result

# # Your TimeMap object will be instantiated and called as such:
# # obj = TimeMap()
# # obj.set(key,value,timestamp)
# # param_2 = obj.get(key,timestamp)

