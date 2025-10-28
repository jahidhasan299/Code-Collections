# Perform common set operations: union, intersection, difference.

a = {1, 3, 4, 5}
b = {6, 7, 8, 9}

if __name__ == '__main__':
    print("Union: ", a | b)
    print("Intersection: ", a & b)
    print("Difference (a -b) and (b - a): ", a - b, b-a)
    print("Symmetric differnces: ", a ^ b)