"""The module returns the time, ram, hdd of the computer and some other functions"""
import time
import types
import json
import dicttoxml
from flask import Flask
import psutil
from flask_jsonrpc import JSONRPC

APP = Flask(__name__)
jsonrpc = JSONRPC(APP, '/api', enable_web_browsable_api=True)

class server_rpc:
    
    @jsonrpc.method('App.time')
    def time():
        """The function is used to get time information of the computer""" 
        time_int = int(time.time())
        return time_int
    
    @jsonrpc.method('App.ram')
    def ram():
        """The function is used to get RAM information of the computer""" 
        mem = psutil.virtual_memory()
        mem_int_total = int(mem.total/1024/1024)
        mem_int_used = int(mem.used/1024/1024)
        return mem_int_total, mem_int_used
    
    @jsonrpc.method('App.hdd')
    def hdd():
        """The function is used to get HDD information of the computer"""
        hdd = psutil.disk_usage('/')
        hdd_int_total = int(hdd.total/1024/1024)
        hdd_int_used = int(hdd.used/1024/1024)
        return hdd_int_total, hdd_int_used

    @jsonrpc.method('App.add')
    def add(a, b):
        """The function is used to calculate the sum of a and b"""
        return int(a+b)

    @jsonrpc.method('App.sub')
    def sub(a, b):
        """The function is used to calculate the sub of a and b"""
        return int(a-b)

    @jsonrpc.method('App.json_to_xml')
    def json_to_xml(json_string):
        """The function is used to translate json string to xml string"""
        dict_string = json.loads(json_string)
        xml_string = dicttoxml.dicttoxml(dict_string)
        return str(xml_string)
  
if __name__ == '__main__':
   APP.run(host = "0.0.0.0", port = 8088)  
