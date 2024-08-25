import asyncio
from playwright.async_api import async_playwright, TimeoutError

async def crawl_musinsa(keyword):
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            url = f"https://www.musinsa.com/search/musinsa/goods?q={keyword}&r_ctg="
            await page.goto(url)

            # 페이지가 로드될 때까지 기다림
            await page.wait_for_load_state('networkidle')

            # 상품 정보 크롤링 - 선택자 수정
            products = await page.query_selector_all("div.product")  # 여기에서 올바른 선택자를 사용
            if not products:
                print("No products found. The selector might be incorrect.")
            for product in products:
                try:
                    image_element = await product.query_selector("img")
                    symbol_element = await product.query_selector("div.icon")
                    price_element = await product.query_selector("div.price")
                    brand_element = await product.query_selector("p.item_title")

                    image = await image_element.get_attribute("data-original") if image_element else "No image"
                    symbol = await symbol_element.inner_text() if symbol_element else "No symbol"
                    price = await price_element.inner_text() if price_element else "No price"
                    brand = await brand_element.inner_text() if brand_element else "No brand"

                    print(f"Image: {image}")
                    print(f"Symbol: {symbol}")
                    print(f"Price: {price}")
                    print(f"Brand: {brand}")
                    print("---")
                except Exception as e:
                    print(f"An error occurred while processing a product: {e}")

        except TimeoutError:
            print("Timeout error occurred during the crawling process.")
        except Exception as e:
            print(f"An error occurred during the crawling process: {e}")
        finally:
            await asyncio.sleep(10)
            await browser.close()

# 키워드 입력받기
keyword = input("검색 키워드를 입력하세요: ")

# asyncio.run()을 사용하여 비동기 함수 실행
asyncio.run(crawl_musinsa(keyword))
