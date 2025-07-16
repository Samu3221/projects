from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://autbor.con/example3.html')
    elems = page.locator('p')
    print(elems.nth(0).inner_text)
    print(elems.nth(0).inner_html)