from features.helper.BasePage import BasePage
import re
import time

class ProductPage(BasePage):
    _locators = {
        "select_product": "xpath://*[@id='__next']/div/div[5]/div[2]/div/a[1]",
        "add_amount_six": "id=add-amount-6",
        "add_product": "id=add-product",
        "product_amount": "id=product-amount",
        "product_value": "class:css-kj8j5x-priceText",
        "total_value" : "id=subtotal"
    }

    def select_product(self):
        self._generic_click_element(self.locator.select_product)
    
    def add_amount_product(self):
        self._generic_click_element(self.locator.add_amount_six)

    def add_products(self):
        self._generic_click_element(self.locator.add_product)

    def get_products_value(self):
        self._generic_check_element_is_visible(self.locator.product_value)
        self.value_product = self.selib.get_text(self.locator.product_value)
        self.value_output = re.findall("\d*,\d*", self.value_product)
        self.value_output_product = float(self.value_output[0].replace(',','.'))

    def get_value_amount(self):
        self.value_amount = int(self.selib.get_text(self.locator.product_amount))
        

    def calculate_cart(self):
        self.get_products_value()
        self.get_value_amount()
 
        self.total_value_sub = float("{0:.2f}".format(self.value_output_product * self.value_amount))
        self.teste = str(self.total_value_sub)
        self.value_output_product_str = str(self.teste.replace('.',','))

        self.selib.element_text_should_be(self.locator.total_value, "R$ " + self.value_output_product_str)
