import asyncio
from playwright.async_api import async_playwright

async def scrape_grt_schedule():
    async with async_playwright() as p:
        # Launch headless browser
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # Go to the GRT schedule page
        url = "https://www.grt.ca/en/schedules-maps/schedules.aspx"
        await page.goto("https://www.grtjewels.com/")

        # Wait for content to load (adjust the selector as needed)
        await page.wait_for_selector("#dropdown-basic-button1")

        # Extract content
        content = await page.content()
        print("Page loaded. Sample HTML:\n")
        print(content[:1000])  # Print a portion to verify

        # Optionally parse it with BeautifulSoup or extract text with Playwright
        # Example: Get all route names
        routes = await page.query_selector_all("#dropdown-basic-button1")  # Replace with real selector if known
        for r in routes:
            name = await r.inner_text()
            print("Route:", name)

        # Close browser
        await browser.close()

# Run the async script
asyncio.run(scrape_grt_schedule())
