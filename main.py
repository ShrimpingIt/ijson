import ijson

# based on '4.1 Configuration of the Wifi' from https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_basics.html
def connect_wifi(essid, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(essid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

# based on '5.2 HTTP Get Request' from https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_tcp.html
# TODO CH be sure to call s.close() or use context manager interface 
def http_stream(url):
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    return s

def print_forecast(filelike):
    forecast = []
    total = 0
    for prefix,event,value in ijson.parse(filelike):
        if prefix =="list.item.rain.3h" and event=="number":
            total += float(value)
        elif prefix == "list.item.rain" and event=="end_map":
            forecast.append(total)
            total = 0
    print(forecast)


def print_url():
    print_forecast(urlopen('http://shrimping.it/tmp/weatherapi/openweathermap.json'))

def print_local():
    with open("openweathermap.json", 'r') as f:
        print_forecast(f)