def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    ls = [ ]
    for i in range(A,B+1):
        ls.append(i)

    return ls[::-1]

print(main(3,5))
    