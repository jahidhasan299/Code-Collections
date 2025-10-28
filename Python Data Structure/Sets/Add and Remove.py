# Demonstrate how to add and discard elements in a set.

numbers = {1, 2, 3}
numbers.add(4)
numbers.discard(2)
numbers.remove(1)
numbers.update([5, 6])

if __name__ == '__main__':
    print("Updated set:", numbers)