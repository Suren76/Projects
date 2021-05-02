import Adafruit_DHT
from time import sleep

while True:
    h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
    print(h,t)
    sleep(5)