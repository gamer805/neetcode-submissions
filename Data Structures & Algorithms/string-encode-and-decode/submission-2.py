class Solution:

    def encode(self, strs: List[str]) -> str:
        string = str(len(strs)) + "_^_^"
        for s in strs:
            string += s
        for s in strs:
            string += "_^_^"+str(len(s))
        return string

    def decode(self, s: str) -> List[str]:
        items = list(s.split("_^_^"))
        num_strs = int(items[0])
        strlens = items[len(items)-num_strs:]
        strs = []
        index = 0
        for length in strlens:
            strs.append(items[1][index:index+int(length)])
            index += int(length)
        return strs