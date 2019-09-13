# ProxyPool
Proxypool based on Python3

[README_CN.md]() in Chinese

## Install requirements
>conda install --yes --file requirements.txt

### Configure Proxypool

### Redis service

If you set up redis authentication, you need to set 'REDIS_PASSWORD' in settings.py to your password

### Proxy providers

Proxypool provides several crawlers on free proxies. It can be seen in [proxy_web.txt](https://github.com/LMFrank/ProxyPool/blob/master/proxy_web.txt)

If needed, you can add crawlers to crawler.py

### Start project

cd into the project folder and input the command below:

>python run.py

Input http://127.0.0.1:5555 in the browser, then you can see the page by WebAPI encapsulation

![1568343397598](C:\Users\62373\AppData\Roaming\Typora\typora-user-images\1568343397598.png)

/random：provide a proxy randomly![1568343539737](C:\Users\62373\AppData\Roaming\Typora\typora-user-images\1568343539737.png)

/count：provide the total amount of proxypool

![1568343599231](C:\Users\62373\AppData\Roaming\Typora\typora-user-images\1568343599231.png)

### Get proxy

It is very convenient to  get proxy by WebAPI. 

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

### Summary

1. Project skeleton is based on *Python3Webspider*
2. This is my first time to write comments in English. Comments and suggestions are most welcome! 


