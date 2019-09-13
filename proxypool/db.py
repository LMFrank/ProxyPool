import redis
from random import choice
import re
from proxypool.settings import REDIS_HOST, REDIS_KEY, REDIS_PASSWORD, REDIS_PORT
from proxypool.settings import MAX_SCORE, MIN_SCORE, INITIAL_SCORE
from proxypool.error import PoolEmptyError

class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        Initialize.
        :param host: Redis host
        :param port: Redis port
        :param password: Redis password
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
    
    def add(self, proxy, score=INITIAL_SCORE):
        """
        Add proxy and set the score to max.
        :return: add result
        """
        if re.match('\d+\.\d+\.\d+\.\d+\:\d+', proxy) is None:
            print("Proxy does not meet the rule", proxy, "is dropped")
            return
        if self.db.zscore(REDIS_KEY, proxy) is None:
            return self.db.zadd(REDIS_KEY, {proxy:score})
    
    def random(self):
        """
        Get proxies randomly.
        First, try to access the proxy with the highest score.
        If the highest score does not exit, it will be otainend according to the rank.
        Otherwise, it will raise error.

        :return: random proxy
        """
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError
    
    def decrease(self, proxy):
        """
        Substract one point from the score.
        If the score is less than MAX_SCORE, delete the proxy.
        :param proxy: Proxy
        :return: the modified score of the proxy
        """
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('Proxy:', proxy, 'Current score', score, '-1')
            return self.db.zincrby(REDIS_KEY, -1, proxy)
        else:
            print('Proxy', proxy, 'Current score', score, 'remove')
            return self.db.zrem(REDIS_KEY, proxy)
    
    def exists(self, proxy):
        """
        Judgment of existence.
        :param proxy: Proxy
        :return: existence
        """
        return not self.db.zscore(REDIS_KEY, proxy) == None
    
    def max(self, proxy):
        """
        Set proxy score to MAX_SCORE.
        :param proxy: Proxy
        :return: end of setting
        """
        print('Proxy', proxy, "is avaliable and setted as", MAX_SCORE)
        return self.db.zadd(REDIS_KEY, {proxy:MAX_SCORE})
    
    def count(self):
        """
        Get the amount.
        :return: amount
        """
        return self.db.zcard(REDIS_KEY)
    
    def all(self):
        """
        Get all proxies.
        :return: list of all proxies
        """
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)
    
    def batch(self, start, stop):
        """
        Get proxies
        :param start: Start index
        :param stop: Stop index
        :return: proxy list
        """
        return self.db.zrevrange(REDIS_KEY, start, stop - 1)


if __name__ == '__main__':
    conn = RedisClient()
    result = conn.batch(680, 688)
    print(result)