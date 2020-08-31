from PageObjectLibrary import PageObject


class BasePage(PageObject):
    _wait_timeout = 30

    def _generic_click_element(self, element_to_interact):
        self._wait_element_iterable(element_to_interact)
        self.selib.click_element(element_to_interact)
    
    def _generic_check_element_is_visible(self, element_to_interact, wait_timeout=None):
        self._wait_element_iterable(element_to_interact, wait_timeout)

    def _generic_input_text(self, element_to_interact, text):
        self._wait_element_iterable(element_to_interact)
        self.selib.input_text(element_to_interact, text)

    def _generic_select_from_list_by_index(self, element_to_interact, index):
        self._wait_element_iterable(element_to_interact)
        self.selib.select_from_list_by_index(element_to_interact, index)

    def _generic_select_from_list_by_value(self, element_to_interact, value):
        self._wait_element_iterable(element_to_interact)
        self.selib.select_from_list_by_value(element_to_interact, value)

    def _wait_element_iterable(self, element_to_interact, wait_timeout=None):
        wait_timeout = wait_timeout or self._wait_timeout
        self.selib.wait_until_page_contains_element(element_to_interact, wait_timeout)
        self.selib.wait_until_element_is_visible(element_to_interact, wait_timeout)

    def _generic_get_value(self, element_to_interact):
        self._wait_element_iterable(element_to_interact)
        self.selib.get_text(element_to_interact)
