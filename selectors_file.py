from dataclasses import dataclass

from selenium.webdriver.common.by import By


class Selector:
    def __init__(self, value: str, by: str = By.XPATH):
        self.value = value
        self.by = by


@dataclass
class Selectors:
    # Home Page
    TODO_ITEM_INPUT = Selector('//input[@placeholder="New Item"]')
    ADD_ITEM_BUTTON = Selector('//button[contains(text(), "Add Item")]')
