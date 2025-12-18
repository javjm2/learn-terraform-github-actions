import pytest


def test_add_item(go_to_site, send_keys_to_input, get_element_by_selector, selectors, get_element_by_xpath):
    test_txt = 'test'
    send_keys_to_input(selectors.TODO_ITEM_INPUT, test_txt)
    get_element_by_selector(selectors.ADD_ITEM_BUTTON).click()
    assert get_element_by_xpath(f"//div[contains(text(), '{test_txt}')]")