class Solution:
    def __init__(self):
        self.res = []

    def permute(self, char):
        track = []

        def backtrack(char_list, track):
            if len(track) == len(char_list):
                self.res.append(track.copy())
                return
            for i in range(len(char_list)):
                if char_list[i] in track:
                    continue
                track.append(char_list[i])
                backtrack(char_list, track)
                track.pop()

        backtrack(char, track)
        return self.res


if __name__ == '__main__':
    char_list = ["a", "b", "c"]
    solution = Solution()
    solution.permute(char_list)