from spider.fetcher import fetch_enterprise_license, fetch_shop_domain
from spider.parser import parse_enterprise_license

def generate_jd_detail_by_shop_id(shop_id, need_data=False):
    data = {'shop_id': shop_id}

    shop_domain = fetch_shop_domain(shop_id)
    if not shop_domain:
        return
    if need_data and not shop_domain.get("data"):
        return
    data['shop_name'] = shop_domain['shopInfo']['shopName']
    enterprise_content = fetch_enterprise_license(shop_id)
    if not enterprise_content:
        return
    data.update(parse_enterprise_license(enterprise_content))
    return data