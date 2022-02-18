import collections


def findMaxBreadthOfParenthesis(parenthesis_str):
    count_for_depth = collections.defaultdict(int)
    max_depth = 0
    open_bracket = 0
    for i in parenthesis_str:
        if i == "(":
            open_bracket += 1
        else:
            count_for_depth[open_bracket] += 1
            max_depth = max(count_for_depth[open_bracket], max_depth)
            open_bracket -= 1

    return max_depth


if __name__ == '__main__':
    input = ["((())((()()()()())))", "(()()())"]
    for i in input:
        x = findMaxBreadthOfParenthesis(i)
        print(x)
