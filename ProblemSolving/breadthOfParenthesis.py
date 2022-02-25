import collections


def findMaxBreadthOfParenthesis(parenthesis_str):
    max_depth = 0
    open_bracket = 0
    prev_d = 0
    dixt_x = collections.defaultdict(list)
    c = 0
    for i in parenthesis_str:
        if i == "(":
            if open_bracket != prev_d:
                dixt_x[prev_d].append(c)
                c = 0
                prev_d = open_bracket
            c += 1
            open_bracket += 1
        else:
            prev_d = open_bracket
            open_bracket -= 1
    print(dixt_x)
    return max_depth


if __name__ == '__main__':
    input = ["()(()()()())(())"]
    for i in input:
        x = findMaxBreadthOfParenthesis(i)
        print(x)

