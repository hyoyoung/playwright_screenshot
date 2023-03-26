#!/usr/bin/env python3

import time
from playwright.sync_api import sync_playwright
import requests

USERNAME = "YOUR_ID"
PASSWD = "YOUR_PWD"
with sync_playwright() as p:
    for browser_type in [p.chromium]:
        #browser = browser_type.launch(headless=False)
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto('https://nid.naver.com/nidlogin.login?svctype=262144')
        time.sleep(1)
        inputbox = page.query_selector("//div/input[@id='id']");
        inputbox.type(USERNAME, delay=100)
        inputbox = page.query_selector("//div/input[@id='pw']");
        inputbox.type(PASSWD, delay=100)
        login_button = page.locator("//button[@id='log.login']")
        login_button.click()
        page.screenshot(path="n1shot.png")
        time.sleep(1)
        page.goto('https://m.mail.naver.com/v2/folders/0/all')
        time.sleep(5)
        page.screenshot(path="n2shot.png")
        browser.close()
