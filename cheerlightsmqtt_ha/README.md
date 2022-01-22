# Turning CheerLights on and off with Home Assistant
How I use Home Assistant to turn my CheerLights on and off.

---

I use my Blinkt! on a Raspberry Pi Zero W as a way to have ambient light behind my montior using CheerLights. I also have a SenseHat that I use with CheerLights some times. So I wanted a way to be able to easily turn the lights on and off, like at night when I go to bed, since my work area is in our bedroom. I figured I could do something with home automation to do it, and enter Home Assistant.

I already run Home Assistant to run other things in the house, like lights and sensors, so it made sense to use it to control these lights as well. Here is how I did it.

---

### Assumptions

For this walkthrough, I am assuming the following:
- You use Home Assistant and it is already configured.
- You use an MQTT Broker locally with Home Assistant.
- You are going to use the cheerlights_bridge script or connect directly to the CheerLights MQTT Broker

---

### The Scripts

The Script that I have included in this folder provides an example of how I handle the "power" state via MQTT in the script. You can use that as a way to base your own work off of. I am not going to go through how to make the script work. Since this is a modified script from the cheerlightsmqtt folder in this repo, you can read through there how to make all the scripts work. Or feel free to reach out to me and I will help you get them going. This folder is more about how to configure Home Assistant to make these work.

---

### Configuring Home Assistant

Here is how I went about getting Home Assistant configured to work. Your Mileage may vary, but this is a starting point.

First make sure that your Home Assistant Instance is configured to use a local MQTT broker.

In case it is not, edit your configuration.yaml file and add the following:

```yaml
# Enable MQTT Broker
mqtt:
  broker: YOUR BROKER IP HERE
```

Changeing the "YOUR BROKER IP HERE" to the IP Address of your Broker.

Next make sure HACS is installed. Again, there are walkthroughs online on how to do that.

Once that is all done (and you restarted Home Assistant), install the virtual_components Package through HACS. You will need to edit your configuration.yaml file again and add the following:

```yaml
# Enable Virtual Components:
virtual:
```

Restart Home Assistant.

Now... Edit your configuration.yaml file again and add the following one more time:

```yaml
sensor:
    - platform: mqtt
        state_topic: "cheerlights/cheerlights"
        name: "Current Cheerlights Color"
        icon: "mdi:lightbulb"

switch:
  - platform: virtual
    name: Cheerlights
```

and restart Home Assistant one last time.

Now that it is backup, we need to add the sensor and switch to the Lovelace Dashboard.

Create a card with the following Entities:

![Screen Shot 2022-01-21 at 22 05 49](https://user-images.githubusercontent.com/40501228/150622563-423f39cf-e0e4-4bb7-a3cf-3ddee2f3307b.png)

Edit the sensor.current_cheerlights_color entity and set your settings to:

![Screen Shot 2022-01-21 at 22 06 53](https://user-images.githubusercontent.com/40501228/150622600-080645dd-7c30-4699-b2bc-5e021f38837d.png)

You will end up with something similiar to this on your dashboard when you are done:

![Screen Shot 2022-01-21 at 22 07 56](https://user-images.githubusercontent.com/40501228/150622631-8626935a-12ab-4479-bec4-e3f334083a62.png)

Current color will probably show "Unknown" until the sensor is updated by MQTT on the next color update.

Not only is this now the power switch, but when the CheerLights color is changed, it will update on the dashaboard and show you the current color and when it was last changed.

Now we need to create the automation behind the virtual switch we created for the CheerLights control.

Head over to Automations and Scenes.

We are going to create 4 different automations.

First let's create the switch on/off automations

Create a new Automation and start with a blank one.

#### _Power Off_

Call it whatever you want, but this first one I called CheerLights - Power Off

Your Trigger will be the following:

![Screen Shot 2022-01-21 at 22 12 26](https://user-images.githubusercontent.com/40501228/150622760-a43a7650-8bcb-4d7e-a426-4ddd7b7bbc7b.png)

And your Action will be the following:

![Screen Shot 2022-01-21 at 22 13 26](https://user-images.githubusercontent.com/40501228/150622783-30149dd1-9c6a-4390-bfab-8345b6f5bef0.png)

Save it. 

#### _Power On_

Next is the power on automation.

Again Create a new Automation, start with a blank.

I called this one CheerLights - Power On

Your Trigger:

![Screen Shot 2022-01-21 at 22 14 37](https://user-images.githubusercontent.com/40501228/150622808-d41a18c9-5330-46e2-9a96-ace2021a2877.png)

And your Action:

![Screen Shot 2022-01-21 at 22 15 10](https://user-images.githubusercontent.com/40501228/150622826-696dbce1-e202-41ff-9ea4-ae69b3089b6e.png)

Save it.

Now as long as you have the appropriate script running on your cheerlights project, they will turn off and on from this switch.

But what if the script errors out or you have to restart the pi or something. Well I handled that also.

Time for two more automations.

#### _Script Stop_

You know the drill.... Create a new automation, start with a blank.

I called this one CheerLights - Script Stop

Your Trigger is:

![Screen Shot 2022-01-21 at 22 18 42](https://user-images.githubusercontent.com/40501228/150622911-80d8f2dd-5912-4a28-a404-698561513573.png)

and your Action is:

![Screen Shot 2022-01-21 at 22 19 32](https://user-images.githubusercontent.com/40501228/150622923-7f6af800-aeb5-41a5-9f49-37160df10eab.png)

If the script stops for whatever reason, this will cause the switch in Home Assistant to switch off. This could be used in another automation or even a notification added to this one to let you know that the script has stopped for some reason to let you take a look at it.

#### _Script Start_

You know the drill.... Create a new automation, start with a blank.

I called this one CheerLights - Script Start

Your Trigger is:

![Screen Shot 2022-01-21 at 22 20 43](https://user-images.githubusercontent.com/40501228/150622963-295bfa8b-4899-4174-9f52-29938327c5ee.png)

and your action is:

![Screen Shot 2022-01-21 at 22 22 02](https://user-images.githubusercontent.com/40501228/150622995-7eb1c08f-2ce2-4103-84e1-32e1bd459fc0.png)

Like the stop automation, this will flip the switch to on when the script starts back up. Again this would be useful for notifications that the script has started if you like. I just use these 2 s a way to set the swtich in case something happens.

And that is how I use Home Assistant to automate/control my CheerLights.