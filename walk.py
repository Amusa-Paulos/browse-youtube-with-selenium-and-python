from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, sys

print("parsing cli arg...")
argz = sys.argv[1:]

page_arg = ''.join([arg.split("=")[1] if arg.startswith("page") else '' for arg in argz])
page_arg = int(page_arg) if page_arg != '' else 5

query_arg = ' '.join([arg if not arg.startswith("page") else '' for arg in argz]).strip()
print("cli arg parsed")

print("initialising Firefox webdriver...")
browser = webdriver.Firefox()
print("Firefox webdriver initialized")


print("Loading Youtube...")
browser.get('http://www.youtube.com')
print("Youtube finished loading...")

print("Sleeping for 2 seconds...")
time.sleep(2)
print("Done sleeping for 2 seconds")

print("Getting and sending the search query to the search box...")
print("Searching for ", query_arg, "...")
search_box = browser.find_element(By.CSS_SELECTOR, "input[id='search']")
search_box.send_keys(query_arg)

print("Sleeping for 2 seconds...")
time.sleep(2)
print("Done sleeping for 2 seconds")
search_box.send_keys(Keys.ENTER)
print("query and enter key sent")

print("Sleeping for 4 seconds...")
time.sleep(4)
print("Done sleeping for 4 seconds")
print("Getting top 5 videos...")
video_titles = browser.find_elements(By.CSS_SELECTOR, 'a[id="video-title"]')
print("done getting video titles")

print("Opening videos in a new tab...")
for i in range(page_arg):
    print("Opening " + video_titles[i].get_attribute('href') + "...")
    browser.execute_script(f"window.open('{video_titles[i].get_attribute('href')}')")
    print(video_titles[i].get_attribute('href'), "Opened")

print("Done")