from proxypool.db import RedisClient

conn = RedisClient()

def set(proxy):
    result = conn.add(proxy)
    print(proxy)
    print("Successful import" if result else "Failed import")

def scan():
    print('Please input proxy, input "exit" to exit')
    while True:
        proxy = input()
        if proxy == 'exit':
            break
        set(proxy)

if __name__ == '__main__':
    scan()
