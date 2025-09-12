# --- Bước 5: Gói gọn công thức thành một hàm hoàn chỉnh ---

import requests
from bs4 import BeautifulSoup


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
            print(f"Lỗi {response.status_code} khi truy cập {url}")
            return None

        soup = BeautifulSoup(response.content, 'html.parser')

        # === ĐIỀN THÔNG TIN BẠN ĐÃ TÌM ĐƯỢC VÀO ĐÂY ===
        title_class = 'sc-c0f8c612-0 dEurho'  # Class của tên sản phẩm
        price_class = 'sc-4ade12da-0 enfFJg'
        description_class = 'sc-34e0efdc-0 dSZwVn'

        title_tag = soup.find('h1', {'class': title_class})
        title = title_tag.get_text(strip=True) if title_tag else "N/A"

        price_tag = soup.find('div', {'class': price_class})
        price = price_tag.get_text(strip=True) if price_tag else "N/A"

        desc_tag = soup.find('div', {'class': description_class})
        description = desc_tag.get_text(strip=True) if desc_tag else "N/A"
        # =======================================================

        product_data = {
            'title': title,
            'price': price,
            'description': description,
            'url': url
        }
        return product_data

    except Exception as e:
        print(f"Có lỗi xảy ra với URL {url}: {e}")
        return None


# Chạy cell này để định nghĩa hàm
print("Hàm scrape_single_product đã sẵn sàng để sử dụng!")
# --- Bước 6: Thử nghiệm hàm vừa tạo ---

# Dán lại link sản phẩm của bạn vào đây
test_url = 'https://tiki.vn/qua-n-du-i-short-gio-nam-the-thao-basic-tre-trung-nang-do-ng-thoa-ng-ma-t-co-gia-n-4-chie-u-mrm-manlywear-p99958075.html?itm_campaign=CTP_YPD_TKA_PLA_UNK_ALL_UNK_UNK_UNK_UNK_X.299618_Y.1881938_Z.3985450_CN.07%2F9---Q%C4%90N---Auto&itm_medium=CPC&itm_source=tiki-ads&spid=99958305'

# Gọi hàm để lấy dữ liệu
product_info = scrape_single_product(test_url)

# In ra kết quả dưới dạng JSON cho đẹp
import json
if product_info:
    print(json.dumps(product_info, indent=4, ensure_ascii=False))
else:
    print("Không lấy được dữ liệu.")