import os
import urllib.request as ulib 
from bs4 import BeautifulSoup as Soup 
import ast 
import time
from selenium import webdriver

# chromPath = ''
dr = webdriver.Chrome()
# dr.get('https://www.baidu.com')
# time.sleep(10)
# print('Browser will be closed')
# dr.quit()
# dr.close()


URL = 'https://www.google.com/search?q=bus&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj_6LHN3_vfAhVD7VQKHZFZC5oQ_AUIDigB&biw=1440&bih=798'
# dr.get(url)

def geturls(URL):
    dr.get(URL)
    a = input()
    page = dr.page_source
    print(page)
    # dr.quit()
    # dr.close()
    soup = Soup(page)

    desiredURLs = soup.find_all('div',{'class':'rg_meta notranslate'})
    ourURLs = []



    for url in desiredURLs:
        theURL = url.text 
        theURL = ast.literal_eval(theURL)['ou']

        ourURLs.append(theURL)
    return ourURLs
URLs = geturls(URL)

def save_images(URLs, directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i,url in enumerate(URLs):
        savePath = os.path.join(directory, '{:06}.jpg'.format(i))

        try:
            ulib.urlretrieve(url, savePath)

        except:
            print('Failed with Url')

directory = '/Users/KentPeng/Documents/yolo3/images/'
save_images(URLs,directory)
# for url in URLs:
#     print(url)