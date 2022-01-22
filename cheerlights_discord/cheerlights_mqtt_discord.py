import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json
import os
from subprocess import check_output
from re import findall
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed

######## Change Me!!! #############
my_broker = "YOUR BROKER IP HERE" # or use the CheerLights MQTT Broker mqtt.cheerlights.com
discord_wh_url = "WEBHOOK URL FOR CHEERLIGHTS DISCORD CHANNEL HERE"

######## DO NOT CHANGE BELOW ############
cl_base_topic = "cheerlights/"
color_topic = cl_base_topic + "cheerlightsRGB"
errormsg = "There was an error with the Cheerlights Program. It has stopped."


color_pick = {
    "#FF0000": "red",
    "#008000": "green",
    "#0000FF": "blue",
    "#00FFFF": "cyan",
    "#FFFFFF": "white",
    "#FDF5E6": "oldlace",
    "#800080": "purple",
    "#FF00FF": "magenta",
    "#FFFF00": "yellow",
    "#FFA500": "orange",
    "#FFC0CB": "pink"
}

def on_message(client, userdata, message):
    color_code = str(message.payload.decode("utf-8")).strip()

    print(color_code)
    print(color_pick[color_code.upper()])

    webhook = DiscordWebhook(url=discord_wh_url)

    embed = DiscordEmbed(title="Current Cheerlights Color", description=color_pick[color_code.upper()], color=color_code.lstrip('#'))
    webhook.add_embed(embed)

    response = webhook.execute() 

def send_discord_msg(msg,discord_wh_url):
    webhook = DiscordWebhook(url=discord_wh_url, content=msg)
    response = webhook.execute() 


def on_connect(client, userdata, flags, rc):
    # Subscribe to cheerlights and cheerlightsRGB topics on mqtt.cheerlights.com
    client.subscribe([(color_topic,0)])

try:
    # create connecton clients
    client = mqtt.Client("pythonpi")

    # Bind functions to callbacks for receiving Cheerlights messages
    client.on_message=on_message
    client.on_connect=on_connect

    # Connect to broker mqtt.cheerlights.com
    client.connect(my_broker, keepalive=60)#connect

    # Start loop to process received messages
    client.loop_forever() 

except KeyboardInterrupt:
    client.disconnect()

except:
    client.disconnect()
    send_discord_msg(errormsg,discord_wh_url)