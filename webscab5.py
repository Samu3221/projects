from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto('https://autbor.com/example3.html')
    print(page.title())
    browser.close()