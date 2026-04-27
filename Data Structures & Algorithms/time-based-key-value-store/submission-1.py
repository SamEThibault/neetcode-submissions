class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.store.get(key, False):
            self.store[key].append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]
        print("SET: ", self.store)

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store.get(key, False)
        prev_val = ""
        if vals:
            for val in vals:
                if val[1] <= timestamp:
                    prev_val = val[0]
                else:
                    break
        return prev_val
