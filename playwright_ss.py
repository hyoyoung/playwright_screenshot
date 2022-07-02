#!/usr/bin/env python3

import time
from playwright.sync_api import sync_playwright
import requests

with sync_playwright() as p:
    for browser_type in [p.firefox]:
        print('bty:', browser_type.name)
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto('https://www.youtube.com/watch?v=1-iS7LArMPA')
        # save screenshot to var
        img = page.screenshot(path=f'testshot1_{browser_type.name}.png')
        #page.locator(".player").screenshot(path="screenshot.png")
        for i in range(5):
            print(f'waiting : {i}')
            time.sleep(1)
        ytplayer = page.query_selector("//div[@id='player-container-inner']");
        ytplayer.screenshot(path='2shot.png')
        # pass var directly to your request
        # files = {'image': img, 'content-type': 'image/png'}
        # requests.post('http://yourresturl.com', files=files)
        browser.close()

        # /html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]
