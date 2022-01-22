import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json
import blinkt
import requests
import os
from subprocess import check_output
from re import findall
from time import sleep

############# Change This variable #############
my_broker = 'YOUR BROKER IP HERE'

############# DO NOT CHANGE BELOW ##############

cl_base_topic = "cheerlights/"
cheerlights_api_url = 'http://api.thingspeak.com/channels/1417/field/2/last.json'
blinkt_brightness = 1.0
color_topic = cl_base_topic + "cheerlightsRGB"
power_topic = cl_base_topic + "power"
script_topic = cl_base_topic + "script_state"
power = 1

blinkt.set_clear_on_exit()

def hex_to_rgb(col_hex):
    """Convert a hex colour to an RGB tuple."""
    col_hex = col_hex.lstrip('#')
    return bytearray.fromhex(col_hex)

def use_api():
    r = requests.get(cheerlights_api_url, timeout=None)
    json = r.json()
    return json['field2']

def clear_lights():
    blinkt.clear()
    blinkt.show()

def show_lights(color_code):
    r, g, b = hex_to_rgb(color_code)

    for i in range(blinkt.NUM_PIXELS):
        blinkt.set_pixel(i, r, g, b, blinkt_brightness)

    blinkt.show()

def script_state(state):
    publish.single(script_topic,state,hostname=my_broker)

def on_message(client, userdata, message):
    global power
    if (message.topic == power_topic):
        if (str(message.payload.decode("utf-8")).strip() == "on"):
            power = 1
            show_lights(use_api())
        elif (str(message.payload.decode("utf-8")).strip() == "off"):
            power = 0
            clear_lights()
        elif (str(message.payload.decode("utf-8")).strip() == "reboot"):
            clear_lights()
            script_state(0)
            os.system('sudo reboot now')
    
    else:
        if power == 1:
            show_lights(str(message.payload.decode("utf-8")).strip())
        else:
            power = 0
            clear_lights()            


def on_connect(client, userdata, flags, rc):
    # Subscribe to cheerlights and cheerlightsRGB topics on mqtt.cheerlights.com
    client.subscribe([(color_topic,0),(power_topic,0),(asterisk_topic,0)])

show_lights(use_api())
script_state(1)

try:
    # create connecton clients
    client = mqtt.Client("blinkt")

    # Bind functions to callbacks for receiving Cheerlights messages
    client.on_message=on_message
    client.on_connect=on_connect

    # Connect to broker mqtt.cheerlights.com
    client.connect(my_broker, keepalive=60)#connect

    # Start loop to process received messages
    client.loop_forever() 

except KeyboardInterrupt:
    client.disconnect()
    clear_lights()
    script_state(0)

except:
    client.disconnect()
    clear_lights()
    script_state(0)
