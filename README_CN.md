# ProxyPool

基于python3的代理池项目

英文版[README.md](https://github.com/LMFrank/ProxyPool/blob/master/README.md)

## 安装依赖

> conda install --yes --file requirements.txt

### 配置代理池

### Redis服务

如果redis使用了密码验证，那么需要将settings.py文件中的REDIS_PASSWORD更改为你自己的密码

### 代理网站

代理池提供了多家网站免费代理的爬取，详情见[proxy_web.txt](https://github.com/LMFrank/ProxyPool/blob/master/proxy_web.txt)。如有需求，可以自行添加在crawler.py中。

### 打开代理池

进入项目所在文件夹，在命令行中输入

> python run.py

网页中输入http://127.0.0.1:5555，即可进入封装好的WebAPI中

![](https://github.com/LMFrank/ProxyPool/blob/master/imgs/page.png)

/random：提供一个随机代理

![](https://github.com/LMFrank/ProxyPool/blob/master/imgs/page1.png)

/count：提供代理池中代理的总量

![](https://github.com/LMFrank/ProxyPool/blob/master/imgs/page2.png)

### 获取代理

通过访问此接口即可获取一个随机可用的代理，代码如下：

```
import requests

PROXY_POOL_URL = 'http://localhost:5555/random'

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None
```

### 小结

1. 本项目框架来自于《Python3网络爬虫开发实践》
2. 第一次尝试使用英文注释，欢迎指正

