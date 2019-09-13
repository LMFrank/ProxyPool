import time
from multiprocessing import Process
from proxypool.webapi import app
from proxypool.getter import Getter
from proxypool.tester import Tester
from proxypool.db import RedisClient
from proxypool.settings import *

class Scheduler(object):
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        Test proxy regularly
        :param cycle: TEST_CYCLE
        """
        tester = Tester()
        while True:
            print("Tester starts running")
            tester.run()
            time.sleep(cycle)
    
    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        Get proxy regularly
        :param cycle: GETTER_CYCLE
        """
        getter = Getter()
        while True:
            print('Start getting proxies')
            getter.run()
            time.sleep(cycle)
    
    def schedule_api(self):
        """
        Open API
        """
        app.run(API_HOST, API_PORT)
    
    def run(self):
        print("ProxyPool starts running")
        
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()
        
        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()
        
        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()
