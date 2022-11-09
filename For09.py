def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    sonlar = list(range(1,11))
    yangi = []
    for son in sonlar:
        yangi.append(son*price)
    
    return yangi
print(main(2.25))

