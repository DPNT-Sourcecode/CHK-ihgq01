
# R1
# SKUS = {
#     'A': 50,
#     'B': 30,
#     'C': 20,
#     'D': 15
# }
#
# SPECIAL_OFFERS = {
#     'A': {
#         'amount': 3,
#         'price': 130
#     },
#     'B': {
#         'amount': 2,
#         'price': 45
#     }
# }

# R2
SKUS = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}

# Must be in correct order
SPECIAL_OFFERS = [
    {
        'sku': 'A',
        'offers': [
            {
                'amount': 3,
                'price': 130
            },
            {
                'amount': 5,
                'price': 200
            }
        ]
    },
    {
        'sku': 'E',
        'offers': [
            {
                'amount': 2,
                'price': 80,
                'free': 'B'
            }
        ]
    },
    {
        'sku': 'B',
        'offers': [
            {
                'amount': 2,
                'price': 45
            }
        ]
    }

]


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
    for offer in SPECIAL_OFFERS:
        sku = offer['sku']
        special_offers = offer['offers']
        num_sku = skus.count(sku)
        # If there is a special offer available...
        if num_sku > 0:

            spec_offer_amounts = [offer['amount'] for offer in reversed(special_offers)]

            for special_offer in reversed(special_offers):
                while num_sku >= special_offer['amount']:

                    multiplier = int(num_sku / special_offer['amount'])
                    total += multiplier * special_offer['price']
                    num_sku -= (multiplier * special_offer['amount'])
                    skus = skus.replace(sku, '', (multiplier * special_offer['amount']))

                    print("MULTIPLE ", multiplier)
                    print("AMOUNT OF SKU TO LOSE ", (multiplier * special_offer['amount']))
                    if special_offer.get('free', None):
                        free_sku = special_offer['free']
                        skus = skus.replace(free_sku, '', multiplier)
                else:
                    continue

    # Add remaining individual SKU totals
    for sku in skus:
        total += SKUS[sku]

    return total









