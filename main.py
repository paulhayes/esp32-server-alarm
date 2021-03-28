import urequests
import ujson
import time

headers = dict()
hostname = "api.pingdom.com"
path = "/api/3.1/checks"
token = ""

#headers['Content-Type'] = 'application/json'
headers['Authorization'] = 'Bearer '+token

url = "https://"+hostname+path

def check():
    print("checking",url)
    response = urequests.get(url,headers=headers)
    #print( response.text )

    responseJson = ujson.loads(response.text)

    if "checks" in responseJson:
        for check in responseJson["checks"]:
            if check["status"]!="up":
                print("hostname "+check["hostname"]+" is down")
                return False

    return True


def alarm():
    #do the alarm stuff here
    pass

while( True ):
    success = check()
    if success :
        time.sleep(10)
    else :
        alarm()

