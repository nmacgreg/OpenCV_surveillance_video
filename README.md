# OpenCV_surveillance_video

* I found this neat stuff online - OpenCV - and other people are using it for cool stuff
* Can a program detect a human in my front door camera?

## Installation

* (Fedora 36)
* How to install OpenCV: `dnf install opencv python3-opencv`
* You might also need the H.264 codec for gstreamer: `dnf install gstreamer1-plugin-openh64 mozilla-openh264 openh264`
* (and, clone this repository)

## About Credentials

* I'm using fd2.py with an exterior camera pointed at my front door.  It features a live RTSP stream that you can access with VLC, in this format: 

`rtsp://<userid>:<password>@10.0.0.10/Streaming/channels/101`

* If you'll copy "credentials.json.template" to credentials.json & fill in the values for the userid and password, everything will work out!

# Current State of the Art

* On my beefiest gaming workstation, a 6-core AMD, run it with: `./fd2.py`
* You'll see a window appear, displaying live video
* ... but if you look at the timecode, it's noticably slow.  In fact, over 30 seconds, it falls 15 seconds behind...
* And the CPU's go nuts, averaging 90%.  Also, the fan noise kicks up...
* So, real-time monitoring with this setup is out of the question
* I tried switching fd2.py over to use the 640x480 "channel/102" of the camera, but nope, its not any better (network inbound is better, though)




