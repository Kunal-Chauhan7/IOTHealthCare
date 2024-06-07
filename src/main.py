import os
import glob
import time
import datetime
import RPi.GPIO as GPIO
import max30102
import hrcalc
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106

import http.client
import urllib

# Adjust the function call above to match your field setup in ThingSpeak


# Initialize the OLED display
serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

# Initialize GPIO for various sensors
GPIO.setmode(GPIO.BCM)
sound_channel = 23
motion_channel = 24
led_channel = 16
gas_channel = 21
GPIO.setup(sound_channel, GPIO.IN)
GPIO.setup(motion_channel, GPIO.IN)
GPIO.setup(led_channel, GPIO.OUT)
GPIO.setup(gas_channel, GPIO.IN)

# Initialize the MAX30102 sensor
m = max30102.MAX30102()

def update_thingspeak(field1, field2, field3, field4, field5, field6):
    """
    Update the ThingSpeak channel with sensor data.
    
    field1: Heart Rate
    field2: SpO2
    field3: Temperature
    field4: Sound Status
    field5: Gas Status
    field6: Motion Status
    """
    # Your ThingSpeak Write API key
    api_key = 'RN5QDPIJFRFH6BAZ'
    # Base URL of ThingSpeak
    base_url = 'https://api.thingspeak.com/update?api_key=RN5QDPIJFRFH6BAZ&field1=5'
    # URL Parameters
    params = urllib.parse.urlencode({
        'field1': field1,
        'field2': field2,
        'field3': field3,
        'field4': field4,
        'field5': field5,
        'field6': field6,
        'key': api_key
    })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print("Connection failed")

def update_thingspeak(field1, field2, field3, field4, field5, field6):
    """
    Update the ThingSpeak channel with sensor data.
    
    field1: Heart Rate
    field2: SpO2
    field3: Temperature
    field4: Sound Status
    field5: Gas Status
    field6: Motion Status
    """
    # Your ThingSpeak Write API key
    api_key = 'RN5QDPIJFRFH6BAZ'
    # Base URL of ThingSpeak
    base_url = 'https://api.thingspeak.com/update?api_key=RN5QDPIJFRFH6BAZ&field1=1'
    # URL Parameters
    params = urllib.parse.urlencode({
        'field1': field1,
        'field2': field2,
        'field3': field3,
        'field4': field4,
        'field5': field5,
        'field6': field6,
        'key': api_key
    })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print("Connection failed")

def update_thingspeak(field1, field2, field3, field4, field5, field6):
    """
    Update the ThingSpeak channel with sensor data.
    
    field1: Heart Rate
    field2: SpO2
    field3: Temperature
    field4: Sound Status
    field5: Gas Status
    field6: Motion Status
    """
    # Your ThingSpeak Write API key
    api_key = 'RN5QDPIJFRFH6BAZ'
    # Base URL of ThingSpeak
    base_url = 'https://api.thingspeak.com/update?api_key=RN5QDPIJFRFH6BAZ&field1=2'
    # URL Parameters
    params = urllib.parse.urlencode({
        'field1': field1,
        'field2': field2,
        'field3': field3,
        'field4': field4,
        'field5': field5,
        'field6': field6,
        'key': api_key
    })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print("Connection failed")

def update_thingspeak(field1, field2, field3, field4, field5, field6):
    """
    Update the ThingSpeak channel with sensor data.
    
    field1: Heart Rate
    field2: SpO2
    field3: Temperature
    field4: Sound Status
    field5: Gas Status
    field6: Motion Status
    """
    # Your ThingSpeak Write API key
    api_key = 'RN5QDPIJFRFH6BAZ'
    # Base URL of ThingSpeak
    base_url = 'https://api.thingspeak.com/update?api_key=RN5QDPIJFRFH6BAZ&field1=3'
    # URL Parameters
    params = urllib.parse.urlencode({
        'field1': field1,
        'field2': field2,
        'field3': field3,
        'field4': field4,
        'field5': field5,
        'field6': field6,
        'key': api_key
    })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print("Connection failed")

def update_thingspeak(field1, field2, field3, field4, field5, field6):
    """
    Update the ThingSpeak channel with sensor data.
    
    field1: Heart Rate
    field2: SpO2
    field3: Temperature
    field4: Sound Status
    field5: Gas Status
    field6: Motion Status
    """
    # Your ThingSpeak Write API key
    api_key = 'RN5QDPIJFRFH6BAZ'
    # Base URL of ThingSpeak
    base_url = 'https://api.thingspeak.com/update?api_key=RN5QDPIJFRFH6BAZ&field1=4'
    # URL Parameters
    params = urllib.parse.urlencode({
        'field1': field1,
        'field2': field2,
        'field3': field3,
        'field4': field4,
        'field5': field5,
        'field6': field6,
        'key': api_key
    })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print("Connection failed")
def update_thingspeak(field1, field2, field3, field4, field5, field6):
    """
    Update the ThingSpeak channel with sensor data.
    
    field1: Heart Rate
    field2: SpO2
    field3: Temperature
    field4: Sound Status
    field5: Gas Status
    field6: Motion Status
    """
    # Your ThingSpeak Write API key
    api_key = 'RN5QDPIJFRFH6BAZ'
    # Base URL of ThingSpeak
    base_url = 'https://api.thingspeak.com/update?api_key=RN5QDPIJFRFH6BAZ&field1=6'
    # URL Parameters
    params = urllib.parse.urlencode({
        'field1': field1,
        'field2': field2,
        'field3': field3,
        'field4': field4,
        'field5': field5,
        'field6': field6,
        'key': api_key
    })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print("Connection failed")




# DS18B20 temperature sensor setup
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    with open(device_file, 'r') as f:
        return f.readlines()

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

def display_data(hr, spo2, temp_c, sound, gas, motion):
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((10, 0), "HR: {}  SpO2: {}".format(hr, spo2), fill="white")
        draw.text((10, 12), "Temp: {:.1f}C".format(temp_c), fill="white")
        draw.text((10, 24), "Sound: {}".format(sound), fill="white")
        draw.text((10, 36), "Gas: {}".format(gas), fill="white")
        draw.text((10, 48), "Motion: {}".format(motion), fill="white")

while True:
	
# Inside your while True loop, after reading sensor data and before sleeping


    # Read heart rate and SpO2
    red, ir = m.read_sequential()
    hr, hrb, sp, spb = hrcalc.calc_hr_and_spo2(ir, red)
    hr = int(hr) if hrb and hr != -999 else "N/A"
    spo2 = int(sp) if spb and sp != -999 else "N/A"

    # Read temperature
    temp_c = read_temp()

    # Read sound sensor
    sound = "Detected" if GPIO.input(sound_channel) else "None"

    # Read gas sensor
    gas = "None" if GPIO.input(gas_channel) else "Detected"

    # Read motion sensor
    motion = GPIO.input(motion_channel)
    motion_status = "None" if motion == 1 else "Detected"
    GPIO.output(led_channel, GPIO.LOW if motion == 1 else GPIO.HIGH)

    # Display the data on the OLED screen
    display_data(hr, spo2, temp_c, sound, gas, motion_status)

    # Log temperature data to file
    GetDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("/home/rasp_1/data.txt", "a+") as fo:
        fo.write("\n{} Temp: {:.1f}C\n".format(GetDateTime, temp_c))
    update_thingspeak(hr, spo2, temp_c, 1 if sound == "Detected" else 0, 1 if gas == "Detected" else 0, 1 if motion_status == "Detected" else 0)
    time.sleep(1)  # Wait for a second before the next read
