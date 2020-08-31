from features.helper.BasePage import BasePage

class HomePage(BasePage):
    _locators = {
        "button_age_gate_yes": "id=age-gate-button-yes",
        "search_address": "id=fake-address-search-input",
        "input_address": "id=address-search-input-address",
        "address": "xpath:*//div/div[3]/div/div[3]/li[1]",
        "adress_input_number": "id=address-details-input-number",
        "address_details_input_complement": "id=address-details-input-complement",
        "adress_button_continue": "id=address-details-button-continue",
    }

    def gate_yes(self):
        self._generic_click_element(self.locator.button_age_gate_yes)
    
    
    def informe_adress(self, address):
        self._generic_click_element(self.locator.search_address)
        self._generic_input_text(self.locator.input_address, address)
        self._generic_click_element(self.locator.address)
        self._generic_input_text(self.locator.adress_input_number, '100')
        self._generic_input_text(self.locator.address_details_input_complement, 'teste')
        self._generic_click_element(self.locator.adress_button_continue)
