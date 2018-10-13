# coding:utf8
# Start your middleware class

#from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from settings import USER_AGENTS
import random
import time
import requests
import base64


# User-Agetn 下载中间件
class RandomUserAgent(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENTS)
        date = time.strftime(u"%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
        request.headers.setdefault('User-Agent', user_agent)

class RandomProxy(object):
    def __init__(self):

        self.proxy_auth = "*************************"
        self.proxy_api = "*************************************************"
        self.proxy_list = requests.get(self.proxy_api).text.split()

    def process_request(self, request, spider):
        proxy = random.choice(self.proxy_list)
        base64_userpass = base64.b64encode(self.proxy_auth)
        request.meta['proxy'] = "http://" + proxy
        request.headers['Proxy-Authorization'] = "Basic " + base64_userpass


#class ProxyMiddleware(object):
    # overwrite process request
    #def process_request(self, request, spider):
        # Set the location of the proxy
    #    sql = 'select ip,port from t_proxy_ip t where t.is_valid =1'
    #    result = SqlUtil.query_all(sql)
    #    ip_port = random.choice(result)
    #    logging.info(ip_port)
    #    request.meta['proxy'] = "http://{0}:{1}".format(ip_port['ip'], ip_port['port'])
        # # Use the following lines if your proxy requires authentication
        # proxy_user_pass = "USERNAME:PASSWORD"
        # # setup basic authentication for the proxy
        # encoded_user_pass = base64.encodestring(proxy_user_pass)
        # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
