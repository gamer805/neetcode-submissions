class TimeMap:

    def __init__(self):
        self.timemap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = {timestamp: value}
        else:
            self.timemap[key][timestamp] = value

        

    def get(self, key: str, timestamp: int) -> str:
        keymap = self.timemap.get(key, "")
        if keymap == "":
            return ""
        else:
            timestamps = list(keymap.items())
            print(timestamps)
            if len(timestamps) == 0:
                return ""
            if timestamp in keymap:
                return keymap[timestamp]
            while len(timestamps) > 0 and timestamps[-1][0] > timestamp:
                timestamps.pop()
            if len(timestamps) == 0:
                return ""
            return timestamps[-1][1]
        
