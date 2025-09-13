# Đây là phiên bản HOÀN HẢO cuối cùng cho file src/scraper.py của bạn

import requests
from bs4 import BeautifulSoup
import json
import time
import os


# ===================================================================
# === PHẦN 1: ĐỊNH NGHĨA HÀM (CÔNG CỤ) ===
# ===================================================================
def scrape_single_product(url):
    """
    Hàm này nhận vào URL của một sản phẩm Tiki,
    cào dữ liệu và trả về một dictionary chứa thông tin.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"-> Lỗi {response.status_code} với URL: {url[:50]}...")
            return None

        soup = BeautifulSoup(response.content, 'html.parser')

        # Sử dụng các class name bạn đã tìm thấy:
        title_class = 'sc-c0f8c612-0 dEurho'
        price_class = 'sc-4ade12da-0 enfFJg'
        description_class = 'sc-34e0efdc-0 dSZwVn'

        title_tag = soup.find('h1', {'class': title_class})
        title = title_tag.get_text(strip=True) if title_tag else "N/A"

        price_tag = soup.find('div', {'class': price_class})
        price = price_tag.get_text(strip=True) if price_tag else "N/A"

        desc_tag = soup.find('div', {'class': description_class})
        description = desc_tag.get_text(strip=True) if desc_tag else "N/A"

        product_data = {
            'title': title,
            'price': price,
            'description': description,
            'url': url
        }
        return product_data

    except Exception as e:
        print(f"-> Exception với URL {url[:50]}...: {e}")
        return None


# ===================================================================
# === PHẦN 2: KHỐI ĐIỀU KHIỂN CHÍNH (DÂY CHUYỀN SẢN XUẤT) ===
# ===================================================================
if __name__ == "__main__":

    # Sử dụng danh sách URL bạn đã cung cấp
    product_urls = [
        'https://tiki.vn/combo-2-qua-n-du-i-nam-qua-n-short-gio-nam-the-thao-hoa-tiet-ran-ri-tre-trung-nang-do-ng-thoa-ng-ma-t-co-gia-n-4-chie-u-mrm-manlywear-p154298071.html?spid=154298080',
        'https://tiki.vn/set-2-qua-n-du-i-nam-qua-n-short-gio-nam-the-thao-basic-tre-trung-nang-do-ng-thoa-ng-ma-t-co-gia-n-4-chie-u-mrm-manlywear-p99968881.html?spid=99968992',
        'https://tiki.vn/quan-short-nam-q3m418r0-cnin697-2701-0-p278109813.html?spid=278109828',
        'https://tiki.vn/quan-short-nam-kaki-lung-thun-tui-hop-thoi-trang-tre-trung-formen-shop-fmps254-p277944078.html?spid=277944148',
        'https://tiki.vn/quan-short-dui-nam-hometex-lung-thun-vai-dui-mem-min-thoang-mat-cao-cap-chuan-form-p276582873.html?spid=276582879',
        'https://tiki.vn/quan-hai-lop-nam-tap-gym-do-gym-shop-chat-thun-lo-kim-thoang-khi-khi-choi-the-thao-p269904929.html?spid=269904933',
        'https://tiki.vn/quan-dui-tap-gym-nam-p246730359.html?spid=246730427',
        'https://tiki.vn/quan-dui-nam-fasvin-vai-gio-dep-hang-nha-may-chat-luong-cao-the-thao-hay-mac-nha-q22553-hn-p221277381.html?spid=221277407',
        'https://tiki.vn/quan-dui-nam-fasvin-dang-lung-vai-dep-hang-nha-may-chat-luong-cao-the-thao-hay-mac-nha-t23557-hn-p221277189.html?spid=221277195',
        'https://tiki.vn/quan-dui-nam-fasvin-dang-lung-vai-dep-hang-nha-may-chat-luong-cao-the-thao-hay-mac-nha-t23558-hn-p221277108.html?spid=221277141',
        'https://tiki.vn/quan-short-the-thao-nam-fasvin-s22492-hn-chat-lieu-cao-cap-mem-min-thoai-mai-p195192648.html?spid=195192669',
        'https://tiki.vn/quan-short-jean-nam-leman-xanh-tron-jl04-slim-form-p174016304.html?spid=174016316',
        'https://tiki.vn/quan-dui-nam-mac-nha-kate-cao-cap-mem-min-mau-ngau-nhien-formen-shop-fmtt002-p172120459.html?spid=172120473',
        'https://tiki.vn/combo-5-qua-n-du-i-nam-mac-nha-cotton-thoa-i-ma-i-thoa-ng-ma-t-hoa-tiet-ngau-nhien-jamano-p162033134.html?spid=162033138',
        'https://tiki.vn/combo-2-qua-n-du-i-nam-qua-n-short-gio-nam-the-thao-hoa-tiet-ran-ri-tre-trung-nang-do-ng-thoa-ng-ma-t-co-gia-n-4-chie-u-mrm-manlywear-p154298071.html?spid=189475417',
        'https://tiki.vn/quan-thun-nam-mac-ngu-the-thao-tap-gym-a077-p130969557.html?spid=130969567',
        'https://tiki.vn/combo-2-qua-n-du-i-nam-cotton-ma-c-nha-thoa-i-ma-i-thoa-ng-ma-t-jamano-ma-u-nga-u-nhien-p110704393.html?spid=110704399',
        'https://tiki.vn/combo-2-quan-dui-nam-may-10-phien-ban-co-tui-2-ben-mau-ngau-nhien-p107801368.html?spid=107801370',
        'https://tiki.vn/quan-short-nam-big-size-quan-sot-nam-the-thao-quan-dui-nam-mac-nha-quan-thun-nam-cotton-4-chieu-co-gian-cao-cap-shopn6-tsb2-p104904605.html?spid=104904607',
        'https://tiki.vn/quan-dui-ngan-nam-fasvin-r21448-hn-vai-gio-chun-mem-mai-co-gian-thoai-mai-van-dong-p100369140.html?spid=100369604',
    ]

    all_products_data = []

    for url in product_urls:
        print(f"Đang cào dữ liệu từ: {url[:70]}...")
        data = scrape_single_product(url)

        if data:
            all_products_data.append(data)

        time.sleep(1)

    os.makedirs('data/raw', exist_ok=True)
    file_path = 'data/raw/products.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(all_products_data, f, ensure_ascii=False, indent=4)

    print(f"\nHoàn tất! Đã cào và lưu thành công {len(all_products_data)} sản phẩm vào file: {file_path}")