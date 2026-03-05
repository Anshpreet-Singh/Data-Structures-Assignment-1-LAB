# Part A: Stack ADT
class StackADT:
    def __init__(self):
        self.items = []   # list to store stack items

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def test_stack():
    print("Part A: Stack Test")

    stack = StackADT()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack size:", stack.size())
    print("Top element:", stack.peek())

    print("Pop:", stack.pop())
    print("Pop:", stack.pop())

    print("Stack size after pops:", stack.size())
    print("Is stack empty?", stack.is_empty())


# Part B: Factorial

def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial(n - 1)


# Fibonacci naive
naive_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# Fibonacci memoized
memo_calls = 0

def fib_memo(n, memo={}):
    global memo_calls
    memo_calls += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]


def test_part_b():
    print("\nPart B: Factorial Tests")
    test_values = [0, 1, 5, 10]

    for n in test_values:
        print("factorial(", n, ") =", factorial(n))

    print("\nPart B: Fibonacci Tests")
    fib_tests = [5, 10, 20, 30]

    for n in fib_tests:
        global naive_calls, memo_calls

        # naive version
        naive_calls = 0
        result_naive = fib_naive(n)

        # memo version
        memo_calls = 0
        result_memo = fib_memo(n, {})

        print("\nFibonacci n =", n)
        print("Naive result:", result_naive, "Calls:", naive_calls)
        print("Memo result:", result_memo, "Calls:", memo_calls)


# Part C: Tower of Hanoi
def hanoi(n, source, auxiliary, destination, stack):
    if n == 1:
        move = "Move disk 1 from " + source + " to " + destination
        print(move)
        stack.push(move)
        return

    hanoi(n - 1, source, destination, auxiliary, stack)

    move = "Move disk " + str(n) + " from " + source + " to " + destination
    print(move)
    stack.push(move)

    hanoi(n - 1, auxiliary, source, destination, stack)


def test_part_c():
    print("\nPart C: Tower of Hanoi (N = 3)")

    move_stack = StackADT()
    hanoi(3, "A", "B", "C", move_stack)

    print("Total moves:", move_stack.size())


# Part D: Recursive Binary Search
def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)


def test_part_d():
    print("\nPart D: Binary Search Tests")

    arr = [1, 3, 5, 7, 9, 11, 13]
    search_values = [7, 1, 13, 2]

    for value in search_values:
        index = binary_search(arr, value, 0, len(arr) - 1)
        print("Search", value, "→ Index:", index)

    # empty array test
    empty = []
    result = binary_search(empty, 5, 0, len(empty) - 1)
    print("Search in empty array → Index:", result)


# Main Program
if __name__ == "__main__":
    test_stack()      # Part A
    test_part_b()     # Part B
    test_part_c()     # Part C
    test_part_d()     # Part D
