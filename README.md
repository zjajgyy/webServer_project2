# project_2
## Introduction
The project is based on python and Flask, using jsonrpc to cover all the requirements. This project includes five files:
- http_rpc_server.py
- http_rpc_client.py
- requirements.txt
- README.md
- .gitignore

## Information
To run the project, you should first import the *http_rpc_client.py* in your test file.
Here are some information about how to run the project correctly:
- run: *"> python http_rpc_server.py &"* to start the server
- run your test file which imports the client module
- call functions to test the project

## Functions on client
- Client.init(self, addr)

    This is the constructed function and send an address with the format of *host:8088* like *127.0.0.1:8088* to initial to connection. 
- Client.time(self) -> int
  
    Call the function and time of the system will be returned.
- Client.ram(self) -> int, int
  
    Call the function and ram of the system will be returned.
- Client.hdd(self) -> int, int
  
    Call the function and hdd of the system will be returned.
- Client.add(self, a, b) -> int
  
    Call the function and send two integers as parameters, and sum of the two integers will be returned.
- Client.sub(self, a, b) -> int
  
    Call the function and send two integers as parameters, and sub of the two integers will be returned.
- Client.json_to_xml(self, json_string) -> xml_string
 
    Call the function and send a json string as parameters and a xml string will be returned.
￼

## Exceptions raised in cases
If the parameters of the __add__ and __sub__ are not integers, exception with __"not an integer"__ will be raised.
If the parameter of the json_to_xml is not a valid json string, exception with __"invalid JSON string"__ will be raised.
If the server is not working, every time a function is called, exception with __"server unreachable"__ will be raised.
If the parameters are invalid, whether the server is working or not will not be checked.

