

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

    # If there are any illegal SKUs, we return -1
    illegal_skus = [sku for sku in skus if sku not in SKUS.keys()]
    if illegal_skus:
        return -1

    # Check for special offers first
    for sku in SPECIAL_OFFERS.keys():
        num_sku = skus.count(sku)
        # If there is a special offer available...
        if num_sku >= SPECIAL_OFFERS[sku]['amount']:
            # Remove from the main string as we will add to total here
            skus = skus.replace(sku, '')
            # Check for extra individual SKUs over the special offer
            while num_sku % SPECIAL_OFFERS[sku]['amount'] != 0:
                total += SKUS[sku]
                num_sku -= 1
            else:
                # Calculate how many special offers can be used
                multiplier = num_sku / SPECIAL_OFFERS[sku]['amount']
                total += multiplier * SPECIAL_OFFERS[sku]['price']

    # Add remaining individual SKU totals 
    for sku in skus:
        total += SKUS[sku]

    return total



