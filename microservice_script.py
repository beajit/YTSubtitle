from selenium import webdriver
import chromedriver_autoinstaller

from selenium.webdriver.common.by import By

import sys
from pytube import YouTube


from home.models import YtVideoData


def link_Caption(youtube_link):

    # Create a YouTube object
    source = YouTube(youtube_link)
    en_caption = source.captions.get_by_language_code('en')

    en_caption_convert_to_srt =(en_caption.generate_srt_captions())
    return en_caption_convert_to_srt


def getData():
    opt = webdriver.ChromeOptions()
    opt.add_argument("--start-maximized")
    opt.headless = True

    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=opt)
    url = "https://www.youtube.com/feed/trending"

    driver.get(url)

    codes = []
    try:
        table_id = driver.find_elements(By.ID, "grid-container")
        print("............1111111111111111111111111111", len(table_id))

    except:
        print("No Data")

    try:
        
        for parent_element in table_id:
            dictt = {}

            # Assuming you already have the parent element, let's call it 'parent_element'

            # Find the ytd-video-renderer tag
            video_renderer = parent_element.find_elements(By.CSS_SELECTOR, 'ytd-video-renderer')
            count = 0
            if count <= 100:
                for one in video_renderer:
                    print("..", count)
                    try:
                        # Find the dismissible id element
                        dismissible_id_element = one.find_element(By.CSS_SELECTOR, 'div#dismissible')

                        # Find the ytd-thumbnail tag element
                        thumbnail_element = dismissible_id_element.find_element(By.CSS_SELECTOR, 'ytd-thumbnail')

                        # Find the 'a' tag and get the 'href' attribute
                        a_tag = thumbnail_element.find_element(By.CSS_SELECTOR, 'a')
                        href = a_tag.get_attribute('href')
                        print("href", href)
                        href = href.replace("https://www.youtube.com/watch?v=","")
                        # Print the 'href' attribute
                        print(link_Caption(href))
                        
                        YtVideoData.objects.create(video_link = href, video_discription = "", video_subtitle = link_Caption(href))
                        print("saved", srt)
                        count += 1
                    except:
                        continue
            else:
                break
    except:
        print(sys.exc_info())

    print("...............................", codes)
    driver.close()
    driver.quit()

    return codes


code_scrap_fun = getData()
