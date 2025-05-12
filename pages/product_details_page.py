from playwright.sync_api import Page, expect


class ProductDetailsPage:

    def __init__(self, page: Page):
        self.page = page

        self.__product_card = self.page.locator('[class="product-details"]')
        self.__product_name = self.page.locator('[class="product-information"]>h2')
        self.__product_category = self.page.locator('p:has-text("Category")')
        self.__product_price = self.page.locator('xpath=/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/span')
        self.__product_availability = self.page.locator('text=Availability:')
        self.__product_condition = self.page.locator('text=Condition:')
        self.__product_brand = self.page.locator('text=Brand:')

    def is_product_card_visible(self) -> bool:
        return self.__product_card.is_visible()

    def is_product_name_visible(self) -> bool:
        return self.__product_name.is_visible()

    def is_product_category_visible(self) -> bool:
        return self.__product_category.is_visible()

    def is_product_price_visible(self) -> bool:
        return self.__product_price.is_visible()

    def is_product_availability_visible(self) -> bool:
        return self.__product_availability.is_visible()

    def is_product_condition_visible(self) -> bool:
        return self.__product_condition.is_visible()

    def is_product_brand_visible(self) -> bool:
        return self.__product_brand.is_visible()