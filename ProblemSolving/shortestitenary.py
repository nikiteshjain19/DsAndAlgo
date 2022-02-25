import collections


class Solution:
    def __init__(self):
        self.result = None

    def find_best_route(self, routes, start, end):
        routes_dic = collections.defaultdict(list)
        for i in routes:
            routes_dic[i[0]].append(i[1])

        def recursive(starting_airport, prev_route):
            prev_route.append(starting_airport)
            if starting_airport == end:
                if self.result is None:
                    self.result = prev_route.copy()
                else:
                    if len(self.result) > len(prev_route):
                        self.result = prev_route.copy()
                return
            for dest in routes_dic[starting_airport]:
                if dest not in prev_route:
                    recursive(dest, prev_route)
                    prev_route.pop()

        recursive(start, [])
        return self.result


if __name__ == "__main__":
    solution = Solution()
    airport_list = ["BGI", "CDG", "DEL", "DOH", "DSM"]
    routes_to_from = [
        ["BGI", "DEL"],
        ["BGI", "DOH"],
        ["DSM", "DEL"],
        ["DSM", "CDG"],
        ["DOH", "DSM"],
        ["DEL", "BGI"],
        ["DOH", "CDG"]
    ]
    solution.find_best_route(routes_to_from, "BGI", "CDG")
