from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import youtube_dl
import os
import time

starttime = time.time()

def download_ytvid_as_mp3(urll=""):
    video_url = urll#input("enter url of youtube video:")
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"C:/Users/ajuga/Music/music/{video_info['title']}.mp3"#f"{video_info['title']}.mp3"
    
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("Download complete... {}".format(filename))


chrome_options = Options()
chrome_options.add_argument("--headless")
os.system("cls||clear")

search_query = input().split()
os.system("cls||clear")
path = r"C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(path, options=chrome_options)
driver.implicitly_wait(5)

os.system("cls||clear")
print(search_query)
os.system("cls||clear")
final_query = "+".join(search_query)

driver.get('https://www.youtube.com/results?search_query={}'.format(final_query))
# select = driver.find_element(By.CSS_SELECTOR, 'div#contents ytd-item-section-renderer>div#contents a#thumbnail')
select = driver.find_elements(By.CSS_SELECTOR, 'div#contents ytd-item-section-renderer>div#contents a#thumbnail')

for selecter in select[:5]:
    link = [selecter.get_attribute("href")]
    print(link[0])


#print([driver.find_elements(By.CSS_SELECTOR, 'div#contents ytd-item-section-renderer>div#contents a#thumbnail')])

#print(select.get_attribute('href'))
# link = [select.get_attribute('href')]

# link = link[0]
# os.system("cls||clear")
driver.close()

# print(link)
#download_ytvid_as_mp3(link)

finshtime = time.time()

print(finshtime - starttime)