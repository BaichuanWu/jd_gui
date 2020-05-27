from config import JD_SHOP_FETCH_HOST, JD_SHOP_FETCH_URL
import requests

def fetch_shop_domain(shop_id):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Host": JD_SHOP_FETCH_HOST,
    }
    rs = requests.get(JD_SHOP_FETCH_URL)
    if rs.status_code == 200:
        return rs.json()
    else:
        return {}

def 