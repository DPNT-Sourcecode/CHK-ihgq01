

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

    illegal_skus = [sku for sku in skus not in SKUS.keys()]
    if illegal_skus:
        return -1

    for sku in SPECIAL_OFFERS.keys():
        num_sku = skus.count(sku)
        if num_sku > SPECIAL_OFFERS[sku]['amount']:
            while num_sku % SPECIAL_OFFERS[sku]['amount'] != 0:
                total += SKUS[sku]
                num_sku -= 1
            else:
                multiplier = num_sku / SPECIAL_OFFERS[sku]['amount']
                total += multiplier * SPECIAL_OFFERS[sku]['price']


    return total




