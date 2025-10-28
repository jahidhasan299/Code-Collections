# A tuple that contains other tuples.

nested = ((1,2), (3,4), (5,6), ("a", "b", "c"))

def flatten_tuple(t):
    out = []
    for item in t:
        if isinstance(item, tuple):
            out.extend(flatten_tuple(item))
        else:
            out.append(item)
        return tuple(out)

if __name__ == '__main__':
    print("Nested tuple: ", nested)
    print("Flattened tuple:", flatten_tuple(nested))