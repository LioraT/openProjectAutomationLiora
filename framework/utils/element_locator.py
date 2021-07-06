from selenium.webdriver.common.by import By


class ElementLocator:
    def __init__(self, by: By, value: str):
        self.by = by
        self.value = value
