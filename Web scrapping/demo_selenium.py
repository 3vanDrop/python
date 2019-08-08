from web_handler import Scrapper, _DEFAULT_URL

if __name__ == '__main__':

    with Scrapper(website=_DEFAULT_URL, selenium=True) as web:
        """selenium - Web scrapping using ChromeDriver
        """
        print('\n ** THIS IS JUST A WEB SCRAPPING DEMO USING SELENIUM  - CHROME DRIVER METHOD ** ')
        print('>> type(web())')
        print('>>', type(web())) 
        # >><class 'bs4.BeautifulSoup'>

        print('>> type(web.driver)')
        print('>>', type(web.driver)) 
        # >><class 'selenium.webdriver.chrome.webdriver.WebDriver'>
        print('Selenium driver can be reached through web.driver\n',
                '  Find further information of how to use this: ',
                'https://selenium-python.readthedocs.io/')

        print('Also, you can look for an example on the following Selenium demo: demo_selenium_2.py')

        input('\n -- PRESS ENTER TO SHOW <a> TAGS FOUND IN SOURCE CODE -- \n')
        _a = web().find_all('a', attrs={})
        for a in _a:
            print(a)
            input('\n -- PRESS ENTER TO SHOW NEXT ITEM -- \n')

        input('\n -- PRESS ENTER TO SHOW <div> TAGS FOUND IN SOURCE CODE -- \n')
        _div = web().find_all('div', attrs={})
        for div in _div:
            print(div)
            input('\n -- PRESS ENTER TO SHOW NEXT ITEM -- \n')
