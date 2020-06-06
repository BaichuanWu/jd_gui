import requests

from config import JD_SHOP_FETCH_HOST, JD_SHOP_TEMPLATE_URL, JD_ENTERPRISE_LICENSE_URL, JD_ENTERPRISE_FETCH_HOST
from utils.logger import logger


def fetch_shop_domain(shop_id):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Host": JD_SHOP_FETCH_HOST,
    }
    url = JD_SHOP_TEMPLATE_URL.format(shop_id=shop_id)
    try:
        rs = requests.get(url, timeout=2)
    except requests.RequestException as e:
        logger.warn("error in get:%s:%s" % (url, e))
        return {}
    if rs.status_code == 200:
        return rs.json()
    else:
        logger.warn("status_code:%s, content: %s" % (rs.status_code, rs.content))
        return {}

def fetch_enterprise_license(shop_id):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN",
        "Cookie": "mobilev=html5;",
        "Referer": JD_SHOP_TEMPLATE_URL.format(shop_id=shop_id),
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Host": "shopjump.m.jd.com",
    }
    url = JD_ENTERPRISE_LICENSE_URL.format(shop_id=shop_id)
    try:
        rs = requests.get(url, timeout=2)
    except requests.RequestException as e:
        logger.warn("error in get:%s:%s" % (url, e))
        return {}
    if rs.status_code == 200:
        return rs.content
    else:
        logger.warn("status_code:%s, content: %s" % (rs.status_code, rs.content))
        return {}

