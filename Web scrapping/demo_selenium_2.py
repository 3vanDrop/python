from web_handler import Scrapper, _DEFAULT_URL

if __name__ == '__main__':

    with Scrapper(website=_DEFAULT_URL, selenium=True) as web:
        """selenium - Web scrapping using ChromeDriver
        """
        print('\n ** THIS IS JUST A WEB SCRAPPING DEMO USING SELENIUM  - CHROME DRIVER METHOD ** \n')

        print('>> type(web.driver)')
        print('>>', type(web.driver)) 
        # >><class 'selenium.webdriver.chrome.webdriver.WebDriver'>

        # Basic example taken from: https://selenium-python.readthedocs.io/getting-started.html#simple-usage

        print('>> Open website:', 'http://www.python.org')
        web.driver.get("http://www.python.org")
        assert "Python" in web.driver.title
        print('>> web.driver.find_element_by_name("q")')
        elem = web.driver.find_element_by_name("q")
        elem.clear()
        print('>> Type -pycon- inside search TextBox')
        elem.send_keys("pycon")
        print('>> web.driver.find_element_by_name("submit")')
        go_button = web.driver.find_element_by_name("submit")
        print('>> Go button Click()')
        go_button.click()

        assert "No results found." not in web.driver.page_source

        input()