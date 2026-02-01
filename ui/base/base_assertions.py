import allure

from playwright.sync_api import Page, expect

from ui.base.base_page import BasePage


class Assertions(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    @allure.step('Проверка текущего url на соответствие ожидаемому')
    def should_be_url(
            self,
            url: str,
            timeout: int = 3,
            err_msg: str = None
    ) -> None:
        expect(self.page, err_msg if err_msg else 'Проверка URL').to_have_url(url, timeout=timeout * 1000)

    @allure.step('Проверка видимости элемента')
    def should_be_visible(
            self,
            locator: str,
            timeout: int = 3,
            err_msg: str = None
    ) -> None:
        expect(self.page.locator(locator), err_msg).to_be_visible(timeout=timeout * 1000)

    @allure.step('Проверка на равенство фактического и ожидаемого значений')
    def assert_equal(self, actual, expected, err_msg: str = None) -> None:
        assert actual == expected, (
            f'{err_msg if err_msg else "Значения должны быть равны"}\n:'
            f'Actual: {actual}\nExpected: {expected}'
        )
