

class Store:
    products = []

    def __init__(self, products):
        self._products = products
        for product in self._products:
            Store.products.append(product)


    def add_product(self, product):
        """ Add product to products list"""
        Store.products.append(product)


    def remove_product(self, product):
        """ Removes product form products list"""
        Store.products.remove(product)


    def get_total_quantity(self) -> int:
        """ Returns how many products are in products list"""
        total_quantity = 0
        for product in Store.products:
            total_quantity += product._quantity
        return total_quantity


    def get_all_products(self) -> list:
        """ Returns all products in the store that are active."""
        activ_products = []
        for product in Store.products:
            if product._activ == True:
                activ_products.append(product)
        return activ_products

    def order(self, shopping_list) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price


