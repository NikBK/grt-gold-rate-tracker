import asyncio
from playwright.async_api import async_playwright

async def scrape_gold_price():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto("https://www.grtjewels.com/", wait_until="networkidle")

        # Wait for the gold rate element to load (adjust if needed)
        await page.wait_for_selector(".gold-silver-rate")  # This class exists

        # Get the text
        rate_section = await page.query_selector(".gold-silver-rate")
        text = await rate_section.inner_text()

        print("Gold Rate Info:")
        print(text)

        await browser.close()

asyncio.run(scrape_gold_price())
