import unittest
from playwright.sync_api import sync_playwright

class TestTodoCreation(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.p = sync_playwright().start()
        cls.browser = cls.p.chromium.launch(headless=False, slow_mo=1000)
        cls.context = cls.browser.new_context()
        cls.context.set_default_timeout(5_000)

    def setUp(self) -> None:
        self.page = self.context.new_page()
        self.page.goto("https://vanilton.net/web-test/todos/#/")

    def test_criar_todo(self) -> None:
        self.page.get_by_placeholder("What needs to be done?").click()
        self.page.get_by_placeholder("What needs to be done?").fill("teste")
        self.page.get_by_placeholder("What needs to be done?").press("Enter")

        self.assertTrue(self.page.locator("text=teste").is_visible())

    def tearDown(self) -> None:
        self.page.close()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.context.close()
        cls.browser.close()
        cls.p.stop()

if __name__ == '__main__':
    unittest.main()
