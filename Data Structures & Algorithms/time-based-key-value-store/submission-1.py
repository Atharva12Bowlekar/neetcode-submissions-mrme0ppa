class TimeMap:
    def __init__(self):
        self.dct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.dct.get(key, 0) == 0:
            self.dct[key] = {}
        self.dct[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        while timestamp > 0 and key in self.dct.keys():
            if self.dct[key].get(timestamp, None):
                return self.dct[key][timestamp]
            else:
                timestamp -= 1 
        return ""