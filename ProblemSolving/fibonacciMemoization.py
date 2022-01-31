"""
https://youtu.be/KEEKn7Me-ms
Non-Recursive using memoization

"""


class Fibonacci:
    result = {}

    def fibonacci(self, number):
        num1 = 0
        num2 = 1
        result = 0
        for i in range(2, number + 1):
            result = num1 + num2
            num1 = num2
            num2 = result
        return result



def main():
    fibonacci = Fibonacci()
    print(fibonacci.fibonacci(15))


if __name__ == '__main__':
    main()
