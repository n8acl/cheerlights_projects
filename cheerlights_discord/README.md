# CheerLights Discord Notifcations
MQTT Python based scripts to send a notification to a Discord Channel 

---

Want to be notified in your Discord server when the current CheerLights color is changed?

Here is a way to do that using MQTT and python.

The included script will listen to an MQTT broker (whether that be your own or the CheerLights MQTT Broker) and send the color notification to a channel in your Discord Server.

---
## Disclaimer

Be aware that this script has the potential of spamming your server. This was a proof of concept when I was designing the CheerLightsBot for the Offical CheerLights Discord Server, but I could see where someone might want to have it to use in their server. 

If you want to see the CheerLightsBot in action, join the Official CheerLights Discord Server: [https://discord.gg/EupyBjpw](https://discord.gg/EupyBjpw)

---

## Installation

In order to run the script, you will need to make sure a few packages are installed first.

First run the following commands on your system if you are doing a clean setup or don't have these packages/libraries installed already.

```bash
sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get -y dist-upgrade && sudo apt-get -y autoremove

sudo apt-get install python3 python3-pip git screen

pip3 install paho-mqtt
pip3 install discord-webhook

git clone https://github.com/n8acl/cheerlights_projects.git
```

---

## Configure the Script

You will need to edit the script and change the following variables:

```my_broker``` sets the IP address or url/FQDN of your personal broker or the CheerLights provided MQTT broker.

```discord_wh_url``` sets the webhook url for the channel you want notifications sent to.

Save it.

---

## Getting the Discord Webhook

In case you have never configured a Discord Webhook for a channel before:

- Create a new text channel for the bot (Ex: #cheerlights).
- Go to the settings of the new channel (click on the gear next to the channel name or right click and go to edit channel.)
- Click Integrations on the left side.
- Click on Webhooks in the middle of the screen
- In the middle of the screen should be a button that says "New Webhook". Click that.
- Name it something that will mean something (ex. CheerLightsBot)
- Make sure under channel it is the correct channel for the CheerLights notifications.
- Click the "Copy Webhook URL" button at the bottom of the window. 
- Click Save and you are done.
- Add that Webhook URL to the Python script in the variable talked about above.

---

## Running the Script

To set the script running, run the following commands:

```bash
cd cheerlights_projects/cheerlights_mqtt_discord

screen -S cheerlights_discord

python3 cheerlights_mqtt_discord.py
```

The script will start running and not stop. To disconnect from the new screen session, press and hold ```CTRL``` and then tap ```A``` and ```D``` and that will bring you back to the main console.

In this way, you can leave the script running all the time.

When a new color is sent, you will get a notification in your Discord Channel that looks like:

![Screen Shot 2022-01-21 at 22 55 18](https://user-images.githubusercontent.com/40501228/150623799-8a5f7280-59fe-4a3f-a783-4853ed76c18a.png)
