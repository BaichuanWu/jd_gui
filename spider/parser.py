# -*- coding: utf-8 -*-

from lxml import etree

def parse_enterprise_license(content):
    data = {}
    html = etree.HTML(content)
    element = html.xpath('//div[@class="shop-license"]//div[@class="details-bd"]/p[1]')
    if element:
        data['enterprise_name'] = element[0].text.strip().split("：")[-1]
    return data


C = """
<!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.0//EN" "http://www.wapforum.org/DTD/xhtml-mobile10.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
            <head>
    <meta charset="utf-8">
    <meta name="author" content="m.jd.com">
    <meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" name="viewport"/>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <Meta http-equiv="Expires" Content="Wed, 26 Feb 1997 09:21:57 GMT">
    <meta http-equiv="Last-Modified" content="Wed, 26 Feb 1997 09:21:57 GMT">
    <meta http-equiv="Cache-Control"
          content="no-store, no-cache, must-revalidate,max-age=0,post-check=0, pre-check=0,false">
    <meta http-equiv="Pragma" CONTENT="no-cache">
            <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
        <title>证照信息</title>
    <meta name="format-detection" content="telephone=no"/>
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">

    <script type="text/javascript" src="/js/jquery-1.11.1.min.js"></script>
    <script type="text/javascript" src="/js/jump.js"></script>
</head>        <body>
                <!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="format-detection" content="telephone=no">
    <title>证照信息</title>
    <link rel="stylesheet" href="/css/shopLicense.min.css">
</head>
<body>
<div class="shop-license">
    <div class="details-container">
        <div class="details-hd border-b">京东商城网店经营者营业执照信息</div>
        <div class="details-bd">
                            <p>
                                            企业名称：浙江百越汇农业科技有限公司<br>

                                            营业执照注册号：91330483MA2B9PTN02<br>

                                            法定代表人姓名：凌玮娴<br>

                                            营业执照所在地：乌镇镇子夜东路1508号悦景庄二街坊2号-63<br>

                                            企业注册资金：5000.0万元<br>

                                            营业执照有效期：2018年4月2日&#x20;至&#x20;2048年4月1日<br>

                                            公司地址：广东深圳市罗湖区深南东路4003号世界金融中心B座1408室<br>

                                            营业执照经营范围：农业领域内的技术开发和咨询服务；计算机软硬件的技术开发、技术推广、技术转让、技术咨询、技术服务；供应链管理及咨询服务；初级食用农产品、食品、手工艺品销售（含网上销售）；品牌策划和管理服务；农业项目的咨询、策划服务；餐饮服务；餐饮管理；广告策划。（依法须经批准的项目，经相关部门批准后方可开展经营活动）
                                    </p>
            <p class="details-tips">注：以上营业执照信息，根据国家工商总局《网络交易管理办法》要求对入驻商家营业执照信息进行公示，除企业名称通过认证之外，其余信息由卖家自行申报填写。如需进一步核实，请联系当地工商行政管理部门。</p>
                                        <p class="details-img"><img src="https://img30.360buyimg.com/popshop/jfs/t1/34106/3/8723/271212/5cc6f0b9E27a2b258/f8d0b7356c876db5.jpg" img-index="1"></p>
                            <p class="details-img"><img src="https://img30.360buyimg.com/popshop/jfs/t1/37319/6/7312/379395/5cd05898E2b364062/c4fa9537be612e88.jpg" img-index="2"></p>
                                </div>
    </div>
</div>
<div class="pswp" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="pswp__bg"></div>
    <div class="pswp__scroll-wrap">

        <div class="pswp__container">
            <div class="pswp__item"></div>
            <div class="pswp__item"></div>
            <div class="pswp__item"></div>
        </div>
        <div class="pswp__ui pswp__ui--hidden">
            <div class="pswp__top-bar">
                <div class="pswp__counter"></div>
                <div class="pswp__preloader">
                    <div class="pswp__preloader__icn">
                        <div class="pswp__preloader__cut">
                            <div class="pswp__preloader__donut"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

</body>
<script src="/js/jquery.min.js"></script>
<script src="/js/dialog.min.js"></script>
<script src="/js/photoswipe.min.js"></script>
<script src="/js/shoplicense.js"></script>
</html>
    </body>
</html>
"""

if __name__ == "__main__":
    parse_enterprise_license(C)