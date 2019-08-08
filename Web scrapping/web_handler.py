"""Scrapper - Starter kit

 ChromeDriver class:
    Automatically downloads driver executable file from Official chromedrive 
    repository and instantiates Selenium webdriver.
    
    __call__ method returns Selenium driver object.

 Scrapper class:
    Takes web page source code from Selenium driver / URL lib request to instantiate BeautifulSoup.

    __call__ method returns BeautifulSoup4 object.

 Author:    Evan Tirado
 Date:      Aug 7th, 2019

"""
_DEPENDENCIES = ('bs4', 'selenium')

from pkg_resources import require

for dep in _DEPENDENCIES:
    require(dep)
        
from selenium import webdriver
from bs4 import BeautifulSoup

import urllib.request
import requests
import zipfile
import sys
import os

# Stable release: https://sites.google.com/a/chromium.org/chromedriver/home

_DRIVER_VERSION = '75.0.3770.140'
_REPO = 'https://chromedriver.storage.googleapis.com/%s/'%_DRIVER_VERSION
_DRIVER_PATH = os.getcwd() + '\\chromedriver.exe'
_DEFAULT_URL = 'https://chromedriver.chromium.org/'

class ChromeDriver:
    def __init__(self, driver_path=_DRIVER_PATH):
        """Initialize ChromeDriver
        """
        try:
            _driver_filename = driver_path.split('\\')[-1]
            if _driver_filename not in os.listdir():
                self.get_driver()

            self.driver = webdriver.Chrome(driver_path)
        except Exception as error:
            _error = 'Not able to launch driver {} :: {}:{}'.format(
                        driver_path,
                        type(error).__name__,
                        error)
            print(_error)


    def get_driver(self):
        """Download zip file from _REPO url
        """
        try:
            _decoration = '*'*20
            _os = '_win32.zip' if sys.platform == 'win32' else '_linux64.zip'
            _file_path = '{}chromedriver{}'.format(_REPO, _os)
            
            if 'chromedriver.zip' in os.listdir():
                return self.unzip_driver()

            print('\n{0} Downloading chromedriver{1} {0}'.format(
                _decoration, _os))                                                      
            urllib.request.urlretrieve(
                _file_path, os.getcwd()+'\\chromedriver.zip')
            return self.unzip_driver()
        except Exception as error:
            _error = '{} download failed :: {}:{}'.format(
                        _file_path,
                        type(error).__name__,
                        error)
            print(_error)
    
    def unzip_driver(self):
        """Unzip chromedriver.zip file
        """
        try:
            _decoration = '*'*20
            _src_file = os.getcwd()+'\\chromedriver.zip'
            print('\n{0} Unzipping chromedriver.zip {0}'.format(
                _decoration)) 
            with zipfile.ZipFile(_src_file) as package:
                package.extractall(os.getcwd())
            return True
        except Exception as error:
            _error = '{} unzip failed :: {}:{}'.format(
                        _src_file,
                        type(error).__name__,
                        error)
            print(_error)
            return False

    def __call__(self):
        """Return Selenium driver
        """
        try:
            if hasattr(self, 'driver'):
                return self.driver
            raise AttributeError('Couldnt reach ChromeDriver')
        except Exception as error:
            _error = 'Not able to call {} :: {}:{}'.format(
                        self.__class__.__name__,
                        type(error).__name__,
                        error)
            print(_error)

class Scrapper(ChromeDriver):
    def __enter__(self):
        return self

    def __init__(self, website=_DEFAULT_URL, selenium=False):
        """Initialize launching website
        """
        self.website = website
        if selenium:
            ChromeDriver.__init__(self)
            self.driver.get(website)
        else:
            self.page = requests.get(website)

    def save_copy(self, output='copy.html', source=None):
        """Save website HTML copy
        """
        _source = source if source else self.driver.page_source
        with open(output, 'w', encoding="utf-8") as html:
            html.write(_source)

    def get(self, website):
        """Updates page source
        """
        if hasattr(self, 'page'):
            self.page = requests.get(website)
        elif hasattr(self, 'driver'):
            self.driver.get(website)

    def __call__(self):
        """Return BeautifulSoup - page content
        """
        if hasattr(self, 'page'):
            self.page_source = self.page.content
        elif hasattr(self, 'driver'):
            self.page_source = self.driver.page_source.encode("utf-8")

        return BeautifulSoup(self.page_source, 'html.parser')

    def __exit__(self, *args):
        """Kill driver process if active
        """
        if hasattr(self, 'driver'):
            self.driver.quit()