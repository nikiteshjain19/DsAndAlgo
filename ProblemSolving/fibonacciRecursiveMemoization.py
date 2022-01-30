"""
https://youtu.be/KEEKn7Me-ms
Recursive using memoization

"""


class Fibonacci:

    def helper(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        return self.helper(number - 1) + self.helper(number - 2)

    def fibonacci(self, number):
        return self.helper(number)


def main():
    fibonacci = Fibonacci()
    print(fibonacci.fibonacci(4))


if __name__ == '__main__':
    main()

