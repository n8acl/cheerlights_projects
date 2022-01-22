# CheerLights MQTT
MQTT Python based scripts for Raspberry Pi based Cheerlights Projects 

---

## Background
This is a fun little project I created for the Raspberry Pi CheerLights devices (I will explain more about CheerLights in a minute) I run at home. At one point I just had a BLINKT! that I was using for this project, but then I got my hands on a Pi Sense HAT and decided I wanted to use MQTT to have one point of truth for not only multiple devices but also be able to pull the information into Home Assistant, along with all my other MQTT sensors in use in my home automations.

These scripts are designed to work with a Pimoroni BLINKT! or a Pi Sense-Hat on a Raspberry Pi. 

I figured these would be fun to share with others who use MQTT and might want to play with CheerLights projects.

This project assumes you are already running your own MQTT Broker for something else, for example, home automation.

---

## What is...

#### cheerlights_bridge.py
This is a python script that I wrote that connects to the MQTT broker provided by Hans Scharler for the CheerLights project (more below). It listens to the 2 topics (cheerlightsRGB and cheerlights) provided there and relays them to your own MQTT broker to be used for your own CheerLights Projects. The reason I did this is so I only need one connection to the CheerLights Broker vs 3 or 4 or 5 pinging the CheerLights Broker just from my network alone. This can be run on any machine on your network, but you only need one copy running on your network. Once it is running, everything else would connect to your local broker.

#### cheerlights_mqtt_blinkt.py
This is a python script that I wrote that takes the data provided by the bridge above and turn the LEDS of the PiMoroni BLNIKT! hat the appropriate color. This connects to your MQTT Broker for the data.

#### cheerlights_mqtt_sense.py
Same thing as above for the BLINKT! but for the Pi Sense HAT.

#### Cheerlights
CheerLights is an “Internet of Things” project created by Hans Scharler that allows people’s lights all across the world to synchronize to one color set by Twitter. This is a way to connect physical things with social networking experiences.

More information can be found at: [https://cheerlights.com/](https://cheerlights.com/).

#### MQTT
MQTT is an OASIS standard messaging protocol for the Internet of Things (IoT). It is designed as an extremely lightweight publish/subscribe messaging transport that is ideal for connecting remote devices with a small code footprint and minimal network bandwidth. MQTT today is used in a wide variety of industries, such as automotive, manufacturing, telecommunications, oil and gas, etc. 

More Information can be found at: [https://mqtt.org/](https://mqtt.org/)

#### PiMoroni BLINKT!
Eight super-bright RGB LED indicators that are ideal for adding visual notifications to your Raspberry Pi.

More information can be found: [https://shop.pimoroni.com/products/blinkt](https://shop.pimoroni.com/products/blinkt)

#### Sense HAT
The Sense HAT has an 8×8 RGB LED matrix, a five-button joystick and includes the following sensors:

- Gyroscope
- Accelerometer
- Magnetometer
- Temperature
- Barometric pressure
- Humidity

More Information can be found: [https://www.raspberrypi.org/products/sense-hat/](https://www.raspberrypi.org/products/sense-hat/)

---

## Installation

In order to run the scripts, you will need to make sure a few packages are installed first.

First run the following commands on your Pi if you are doing a clean setup or don't have these packages installed already.

```bash
sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get -y dist-upgrade && sudo apt-get -y autoremove

sudo apt-get install python3 python3-pip git screen

pip3 install paho-mqtt
pip3 install requests

git clone https://github.com/n8acl/cheerlights_projects.git
```

Then, if you are using a PiMoroni BLINKT! on the Pi, run the following:

```bash
pip3 install blinkt
```

Or if you are using a Sense-Hat on the Pi, run the following:

```bash
sudo apt-get install sense-hat
```

### Configure the scripts
Next you will need to edit the files to put your broker information in.

In each of the script files under the define variables section, there are 2 variables that can be edited

```python
# Define Variables
my_broker = "YOUR BROKER INFO HERE" # Make sure to change this!
topic_base = "cheerlights/" # Optional change
```

```my_broker``` sets the IP address or url/FQDN of your personal broker. This variable needs to be changed to access that broker.

```topic_base``` sets the base part of the topic. This is optional. T\his can be changed to match your naming scheme better. If you Change this, you will need to remember it to be able to update the other scripts.

Once these variables have been updated, save the file and open the next. 

You will only need to update the variables in 2 files if you are running this all on one Pi: cheerlights_bridge.py and which ever hat you are using the appropriate script file.

Once everything has been updated, you are ready to run the script.

---

## Running the Scripts

Of course, which scripts you run will depend on which hat you have on the Pi. All of these scripts can be run together on the same Pi (cheerlights_bridge and whatever hat script you are going to run) or you could run the bridge on another machine to use with multiple Pi's/devices.

For example, I have the bridge script running on a server, the BLINKT script running on one Pi and the Sense-Hat script running on another Pi and use an MQTT sensor in Home Assistant to display the current color.

These next steps will assume you are running these scripts on one Pi, but can be adapted to other situations.

First we need to run the bridge to start pulling in MQTT data. This can be done by running the following commands:

```bash
cd cheerlightsmqtt

screen -S cheerlights_bridge

python3 cheerlights_bridge.py
```

The script will start running and not stop. To disconnect from the new screen session, press and hold ```CTRL``` and then tap ```A``` and ```D``` and that will bring you back to the main console. 

Now you can run the appropriate script for the hat you are using by typing (in a new screen session if you like to leave it run for a while or just to play around with):

```bash
python3 cheerlights_mqtt_blinkt.py
```
for a BLINKT or 

```bash
python3 cheerlights_mqtt_sense.py
```
for a Sense-Hat.

Now sit back and enjoy watching the world be able to effect your LED lights or take part in the fun by tweeting a color (that is recognized by the api) to @cheerlights and watch them change. Or you can join the CheerLights Discord server and change them with a bot from there. The server is [https://discord.gg/EupyBjpw](https://discord.gg/EupyBjpw)

Colors supported are:

- red
- green
- blue
- cyan
- white
- oldlace
- purple
- magenta
- yellow
- orange
- pink