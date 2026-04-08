class TimeMap:
    def __init__(self):
        self.dct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.dct.get(key, 0) == 0:
            self.dct[key] = []
        self.dct[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.dct.get(key, [])
        l = 0 
        r = len(values) - 1

        while l <= r:
            mid = (l+r) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res