from time import sleep
import urequests

x = 7
y = 9

def connect():
    import network
 
    ssid = "WIFI-NAME" 
    password = "PASSWORD" 
 
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Already connected")
        return
 
    station.active(True)
    station.connect(ssid, password)
 
    while station.isconnected() == False:
        pass
 
    print("Connection successful")
    print(station.ifconfig())
    
connect()

while True:
    sleep(2)
    
    h = {'content-type' : 'application/x-www-form-urlencoded'}
    form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfTfxMNKdGAepcyGISCoz6ynsDEdTJy9JiGha_HL5ypHgSg-g/formResponse?usp=pp_url&'
    form_data = 'entry.1234193767=' + str(x) + '&entry.1555660614=' + str(y)
    r = urequests.post(form_url, data=form_data, headers=h)
    r.status_code
    r.close()
    print("check google form")
    
    #https://docs.google.com/forms/d/e/1FAIpQLSfTfxMNKdGAepcyGISCoz6ynsDEdTJy9JiGha_HL5ypHgSg-g/viewform?usp=pp_url&entry.1234193767=20&entry.1555660614=20
