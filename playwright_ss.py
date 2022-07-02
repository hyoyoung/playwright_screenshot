#!/usr/bin/env python3

import time
from playwright.sync_api import sync_playwright
import requests

with sync_playwright() as p:
    for browser_type in [p.firefox]:
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto('https://www.youtube.com/watch?v=1-iS7LArMPA') # NY Times Square live CCTV
        img = page.screenshot(path=f'testshot1_{browser_type.name}.png')
        for i in range(5):
            print(f'waiting : {i}')
            time.sleep(1)
        ytplayer = page.query_selector("//div[@id='player-container-inner']");
        ytplayer.screenshot(path='2shot.png')
        browser.close()
