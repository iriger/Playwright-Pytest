from playwright.sync_api import Page, expect


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

        self.__products_page_title = self.page.locator('h2:has-text("All Products")')
        self.__view_product = self.page.locator('[href="/product_details/1"]')
        self.__search_product_field = self.page.locator('#search_product')
        self.__search_btn = self.page.locator('#submit_search')
        self.__search_results_title = self.page.locator('text=Searched Products')
        self.__products_search_results = self.page.locator('div.product-image-wrapper')

    def is_product_page_title_visible(self) -> bool:
        return self.__products_page_title.is_visible()

    def goto_product_details(self) -> None:
        self.__view_product.click()

    def search_product(self, product_name) -> None:
        self.__search_product_field.fill(product_name)
        self.__search_btn.click()

    def is_search_results_title_visible(self) -> bool:
        return self.__search_results_title.is_visible()

    def is_products_search_results_contain_search_option(self, search_option: str) -> bool:
        count = self.__products_search_results.count()
        for i in range(count):
            wrapper = self.__products_search_results.nth(i)
            if wrapper.locator(f'p:has-text("{search_option}")').count() == 0:
                return False
        return True


