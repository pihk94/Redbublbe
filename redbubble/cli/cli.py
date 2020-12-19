from selenium import webdriver
from bs4 import BeautifulSoup
import click
import logging
import os

logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO'))
class Redbubble:
    def __init__(self):
        self.profile = webdriver.ChromeOptions()
        self.profile.add_argument("accept-language=en-US")
        self.profile.add_argument('--lang=en')
        self.profile.add_argument('headless')
        self.driver = webdriver.Chrome(options=self.profile, executable_path=os.path.dirname(__file__) + '\chromedriver.exe')
    
    def extract_keyword(self, url):
        self.driver.get(url)
        el = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/main/div/div/div[2]/div/div[2]/div[3]')
        tag_list = el.text.split('\n') 
        sticker_start = tag_list.index('Stickers Tags')
        all_product = tag_list.index('All Product Tags')
        other_product = tag_list.index('Other Products')
        sticker_tags = tag_list[sticker_start +  1:all_product]
        all_product_tags = tag_list[all_product + 1:other_product]
        other_product_tags = tag_list[other_product + 1:]
        self.driver.quit()
        return sticker_tags, all_product_tags, other_product_tags


@click.group()
def cli():
    """Redbubbles utils"""
    print('Package redbubble')


@cli.command()
@click.option('--link',
              "-l",
              default=False,
              help='Link')
def keywords(link):
    """Find keyword for an english page

    Args:
        link (str): The link to the english webpage
    """
    extract = Redbubble()
    logging.info("Getting keyword from {}".format(link))
    sticker, all_, other = extract.extract_keyword(link)
    logging.info('===========Sticker TAGS=================')
    print(sticker)
    logging.info('===========All product TAGS=================')
    print(all_)
    logging.info('===========Ohter products TAGS=================')
    print(other)
