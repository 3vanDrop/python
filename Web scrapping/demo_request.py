from web_handler import Scrapper, _DEFAULT_URL

if __name__ == '__main__':
    
    with Scrapper(website=_DEFAULT_URL, selenium=False) as web:
        """urllib.request - Web scrapping without web browser
        """
        print('\n ** THIS IS JUST A WEB SCRAPPING DEMO USING URLLIB.REQUEST - NO WEB BROWSER METHOD ** ')
        print('>> type(web())')
        print('>>', type(web())) 
        # >><class 'bs4.BeautifulSoup'>

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