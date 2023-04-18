products = ['хлеб', 'молоко', 'колбаса', 'сыр', 'сок', 'яйца']

filterd_products = [product for product in products if len(product) % 2 == 0]
product_list = ', '.join(filterd_products)
print(product_list)