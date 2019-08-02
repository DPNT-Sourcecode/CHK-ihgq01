

SKUS = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

SPECIAL_OFFERS = {
    'A': {
        'amount': 3,
        'price': 130
    },
    'B': {
        'amount': 2,
        'price': 45
    }
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    return -1 for any illegal values
    :param skus: a String containing the SKUs of all the products in the basket
    :return: an Integer representing the total checkout value of the items
    """
    total = 0

    illegal_skus = [sku for sku in skus if sku not in SKUS.keys()]
    if illegal_skus:
        return -1

    for sku in SPECIAL_OFFERS.keys():
        num_sku = skus.count(sku)
        print("SKU : ", sku)
        print("NUM IN SKUS : ", num_sku)
        if num_sku >= SPECIAL_OFFERS[sku]['amount']:
            skus = skus.replace(sku, '')
            print("REPLACING IN SKUS ", skus)
            while num_sku % SPECIAL_OFFERS[sku]['amount'] != 0:
                print("MODULO DOes NOT EQUAL 0")
                total += SKUS[sku]
                num_sku -= 1
            else:
                print("MODULO DOES EQUAL 0")
                multiplier = num_sku / SPECIAL_OFFERS[sku]['amount']
                print("MULTILIER ", multiplier)
                total += multiplier * SPECIAL_OFFERS[sku]['price']

    print("TOTAL SO FAR ", total)
    for sku in skus:
        print("NORMAL SKU ADDING ", sku)
        total += SKUS[sku]

    return total


