import requests
import json

def successHandler(address, status, country, city, timezone, isp):
    data = f"""
IP Address: {address}
Status: {status}
Location: {city}, {country}
Timezone: {timezone}
Provider: {isp}
    """
    return data

def failHandler(address, status, message):
    data = f"""
IP Address: {address}
Status: {status}
Message: {message}    
    """
    return data

class IP:
    def __init__(self, ip):
        self.url = "http://ip-api.com/json/"
        self.address = str(ip)
        
    def lookup(self):
        try:
            request = requests.get(url=f"{self.url}{self.address}")
            response = json.loads(request.text)
            status = response['status']
            if status == 'success':
                country = response['country']
                city = response['city']
                timezone = response['timezone']
                isp = response['isp']
                result = successHandler(self.address, status, country, city, timezone, isp)
            else:
                message = response['message']
                result = failHandler(self.address, status, message)
            return result
        
        except Exception as e:
            print("Error:", str(e))
            
            
session = IP("114.124.1925.7")
print(session.lookup())
                
            
            
        