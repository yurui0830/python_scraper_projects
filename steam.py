import certifi
import urllib3
from bs4 import BeautifulSoup

"""
scrape steam sales information
"""

# go through how many pages
ALL_PAGE = 10

# need a PoolManager instance to make requests
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

for page in range(ALL_PAGE):
    # set url
    if page == 0:
        url = 'https://store.steampowered.com/specials#tab=TopSellers'
    else:
        url = 'https://store.steampowered.com/specials#' + 'p=' + str(page) + '&tab=TopSellers'
    # make a request
    r = http.request(method='GET', url=url)
    # read http source
    soup = BeautifulSoup(r.data, 'lxml')
    # locate the sales part on the whole page
    top_sellers = soup.find('div', {'id': 'TopSellersTable'})
    # find the sale items
    items = top_sellers.find_all('div', {'class': ['tab_item_content', 'discount_block tab_item_discount']})
    # print items
    for i in items:
        print(i.text)
