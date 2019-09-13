import json
from proxypool.utils import get_page
from lxml import etree

class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print("Succeed in crawling", proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count=10):
        """
        Crawl daili66.
        :param page_count: Page
        :return: proxy
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(page_count)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = etree.HTML(html)
                ip = doc.xpath('//div[@align="center"]//table//tr[position()>1]//td[1]/text()')
                port = doc.xpath('//div[@align="center"]//table//tr[position()>1]//td[2]/text()')
                ip_address = list(zip(ip, port))
                for ip, port in ip_address:
                    yield ':'.join([ip, port])
    
    def crawl_kuaidali(self, page_count=10):
        """
        Crawl kuaidaili.
        :param page_count: Page
        :return: Proxy
        """
        start_url = 'https://www.kuaidaili.com/free/inha/{}'
        urls = [start_url.format(page) for page in range(page_count)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = etree.HTML(html)
                ip = doc.xpath('//table[@class="table table-bordered table-striped"]//tr/td[1]/text()')
                port = doc.xpath('//table[@class="table table-bordered table-striped"]//tr/td[2]/text()')
                ip_address = list(zip(ip, port))
                for ip, port in ip_address:
                    yield ':'.join([ip, port])
    
    def crawl_qydaili(self, page_count=10):
        """
        Crawl qydaili.
        :param page_count: Page
        :return: Proxy
        """
        start_url = 'http://www.qydaili.com/free/?action=china&page={}'
        urls = [start_url.format(page) for page in range(page_count)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = etree.HTML(html)
                ip = doc.xpath('//table[@class="table table-bordered table-striped"]//tr/td[@data-title="IP"]/text()')
                port = doc.xpath('//table[@class="table table-bordered table-striped"]//tr/td[@data-title="PORT"]/text()')
                ip_address = list(zip(ip, port))
                for ip, port in ip_address:
                    yield ':'.join([ip, port])
    
    def crawl_xicidaili(self, page_count=10):
        """
        Crawl XiciDaili.
        :param page_count: Page
        :return: Proxy
        """
        start_url = 'http://www.xicidaili.com/nn/{}'
        urls = [start_url.format(page) for page in range(page_count)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = etree.HTML(html)
                ip = doc.xpath('//*[@id="ip_list"]//tr/td[2]/text()')
                port = doc.xpath('//*[@id="ip_list"]//tr/td[3]/text()')
                ip_address = list(zip(ip, port))
                for ip, port in ip_address:
                    yield ':'.join([ip, port])
    
    def crawl_iphai(self):
        """
        Crawl iphai
        :return: Proxy
        """
        start_url = 'http://www.iphai.com'
        print('Crawling', start_url)
        html = get_page(start_url)
        if html:
            doc = etree.HTML(html)
            ip_list = doc.xpath('//table[@class="table table-bordered table-striped table-hover"]//tr/td[1]/text()')
            ip = list(map(lambda x: x.strip(), ip_list))
            port_list = doc.xpath('//table[@class="table table-bordered table-striped table-hover"]//tr/td[2]/text()')
            port = list(map(lambda x: x.strip(), port_list))
            ip_address = list(zip(ip, port))
            for ip, port in ip_address:
                yield ':'.join([ip, port])