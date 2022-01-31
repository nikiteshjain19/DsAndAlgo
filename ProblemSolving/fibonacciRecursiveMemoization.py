"""
https://youtu.be/KEEKn7Me-ms
Recursive using memoization

"""


class Fibonacci:
    result = {}

    def helper(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number not in self.result:
            self.result[number] = self.helper(number - 1) + self.helper(number - 2)
        return self.result.get(number)

    def fibonacci(self, number):
        return self.helper(number)


def main():
    fibonacci = Fibonacci()
    print(fibonacci.fibonacci(15))


if __name__ == '__main__':
    main()

