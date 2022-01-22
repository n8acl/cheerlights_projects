# My CheerLights Projects
A catch all for my cheerlights projects

---

This repo has been put together as a place to share all of my work related to the CheerLights Projects that I have running at my house. These are intented as a way to maybe answer some questions that people may have about how to do some things and as a way to share what I have been doing with the rest of the CheerLights Community.

I was recently able to create the CheerLightsBot that resides in the CheerLights Discord Server and that is what kind of prompted me to start to pull all of these together.

These are everything I have been playing with over the last few months and years and also plan to update this as I create more things.

For the most part, all of these have one thing in common. They are all based on getting updates from an MQTT Broker. This can be a local broker on your network, or this can be the CheerLights Broker provided by the CheerLights Project, mqtt.cheerlights.com

---

## Included in this Repo

|Folder Name|Description|
|-----------|-----------|
|cheerlights_discord|This is a proof of concept that I used when building the CheerLightsBot. This will send a notification to a channel in a Discord server when the current CheerLights Color is changed.|
|cheerlightsmqtt|These are the base scripts that run my CheerLights devices in my house.|
|cheerlightsmqtt_ha|This is how I integrated CheerLights into my Home Assistant instance to be able to turn the device lights on and off as well as get what the current color is sent to my Home Assistant Dashboard.|
