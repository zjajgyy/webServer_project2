"""The module is a client for send requests to the server"""
from flask_jsonrpc.proxy import ServiceProxy
import types
import json
import urllib

class Client:    
    
    def __init__(self, addr):
        """
        parameters: 1 string fromated like "<host>:<port>"
        """
        self.proxy = ServiceProxy('http://'+addr+'/api')
        
    def time(self):
        """
        parameters: None
        returns: one integer
        """
        try:
            return (self.proxy.App.time())['result']
        except urllib.error.URLError:
            raise Exception("server unreachable")

    def ram(self):
        """
        parameters: None
        returns: 2 integers
        """
        try:
            ram_data = (self.proxy.App.ram())['result']
            return ram_data[0], ram_data[1]
        except urllib.error.URLError:
            raise Exception("server unreachable")   

    def hdd(self):
        """
        parameters: None
        returns: 2 integers
        """
        try:
            hdd_data = (self.proxy.App.hdd())['result']
            return hdd_data[0], hdd_data[1]
        except urllib.error.URLError:
            raise Exception("server unreachable")
  
    def add(self, a, b):
        """
        parameters: 2 integers
        returns: 1 integer
        """
        if (type(a)==type(1) and type(b)==type(1)):
            try:
                return (self.proxy.App.add(a,b))['result']
            except urllib.error.URLError:
                raise Exception("server unreachable")
        else:
            raise Exception("not an integer")
 
    def sub(self, a, b):
        """
        parameters: 2 integers
        returns: 1 integer
        """
        if (type(a)==type(1) and type(b)==type(1)):
            try:
                return (self.proxy.App.sub(a,b))['result']
            except urllib.error.URLError:
                raise Exception("server unreachable")
        else:
            raise Exception("not an integer")

    def json_to_xml(self, json_str):
        """
        parameters: 1 string
        returns: 1 string
        """
        try:
            if (type(json_str)==type("1") and json_str!="" and isinstance(json.loads(json_str), dict)):
                try:
                    xml_str = (self.proxy.App.json_to_xml(json_str))['result']
                    return xml_str[2:-1]
                except urllib.error.URLError:
                    raise Exception("server unreachable")  
            else:
                raise Exception("invalid JSON string")
        except ValueError:
            raise Exception("invalid JSON string")
