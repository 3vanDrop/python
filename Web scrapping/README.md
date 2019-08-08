# Web scrapper - Starter kit

Dependencies:
 - Selenium - https://pypi.org/project/selenium/
 - BeautifulSoup4 - https://pypi.org/project/beautifulsoup4/

Classes to start using Selenium & Beautiful Soup 4 for Web scrapping

 - web_handler.ChromeDriver class: 
    Automatically downloads driver executable file from Official chromedrive repository and starts
    __call__ method returns Selenium driver object.

 - web_handler.Scrapper class:
    Takes web page source code from Selenium driver / URL lib request to instantiate BeautifulSoup.
    __call__ method returns BeautifulSoup4 type obj to be used as per demo_request.py/demo_selenium.py