

def findMaxDepthOfParenthesis(parenthesis_str):
    max_depth = 0
    open_bracket = 0
    for i in parenthesis_str:
        if i == "(":
            open_bracket += 1
        else:
            max_depth = max(open_bracket, max_depth)
            open_bracket -= 1
    return max_depth


if __name__ == '__main__':
    input = ["((())((()()()()())))", "(()()())"]
    for i in input:
        x = findMaxDepthOfParenthesis(i)
        print(x)
