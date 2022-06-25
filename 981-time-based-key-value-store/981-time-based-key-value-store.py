class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        need to store the key with the value
        the key can have multiple values, so it can be an array of values
        the timestamps will always be in increasing order, so if you append to the back of value array,
            the array will be in increasing order of timestamp
        """
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        """
        need to find the timestamp that is less than or equal to the given timestamp
        if a timestamp like that doesn't exist (the given TS is earlier than any already set TS)
            return ""
        just loop backwards through the key's value array and return the first TS item that is <= timestamp?
        """
        if key not in self.store:
            return ""
        
        for value, ts in reversed(self.store[key]):
            if ts <= timestamp:
                return value
        return ""
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)