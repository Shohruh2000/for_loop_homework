def main(list1):
    """
Returns a list where only the first letter of each name is capitalized.
Args:
    list1: list
Returns:
    list: return  answer
    """
    list = [ ]     
    n = len(list1)
    for i in list1:
        list.append(i.title())

    return list
print(main(["SalohiDdIn","ManGuberdi","ShOhruh","UMId"]))

