import asyncio
from playwright.async_api import async_playwright


async def crawl_musinsa(keyword):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        url = f"https://www.musinsa.com/search/goods?keyword={keyword}&keywordType=keyword&gf=A"
        await page.goto(url)

        # 상품 정보 크롤링
        products = await page.query_selector_all("div.li_inner")
        for product in products:
            image = await (await product.query_selector("img.lazyload")).get_attribute("src")
            symbol = await (await product.query_selector("div.symbol")).inner_text()
            price = await (await product.query_selector("div.price")).inner_text()
            brand = await (await product.query_selector("p.item_title")).inner_text()

            print(f"Image: {image}")
            print(f"Symbol: {symbol}")
            print(f"Price: {price}")
            print(f"Brand: {brand}")
            print("---")

        await browser.close()

# 키워드 입력받기
keyword = input("검색 키워드를 입력하세요: ")
asyncio.get_event_loop().run_until_complete(crawl_musinsa(keyword))