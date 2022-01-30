# Introduction

This repo consists of a small bit of code written and data collected
while helping my son run his science experiment "What brand of AA
battery lasts longest?"

# Principle of operation

We will use a simple resistive load to exercise several samples of
several brands of AA battery.  The selection of the load was primarly
based on time, i.e., getting all the different brands tested within a
week.  The datasheet for [Duracell's
AA's](https://www.duracell.com/wp-content/uploads/2020/02/MN15US11191.pdf)
shows that at 10 ohms it akes about 20 hours to train below 1V, and 24
ohms is about 50 hours.  It was easiest to home-build a 20 ohm
resistor, so I went with that to land somewhere in between.

# Test procedure

1. Plug the Raspberry Pi into the the USB port of the host computer.

1. Select 3 units of a given brand of battery and insert them into the
battery holders.

1. Load battery-monitor.py into the Raspberry Pi (FIXME: Say how) and start it running.

1. Allow data to collect until all battery readings are consistently
below 1V.  This will take a day or so.

1. Stop the monitoring program and save the collected readings to a file.

1. Remove the spent batteries and store them together.

1. Repeat for the next brand.

# Parts

* Raspberry Pi Pico RP2040 ($5)
* Half-size breadboard ($5)

* 15 100-ohm resistors.  I soldered the legs of 5 100-ohm resistors
  together in parallel to form a hacky 20 ohm resistor (FIXME: link to article about parallel resistors), and made 3 of
  these bundles. It would have been much better to buy some nice high
  wattage, low ohm resistors but time was tight and I had the 100-ohm
  resistors on hand.  ($0)

* 3 Duracell alkaline AA batteries
* 3 Energizer alkaline AA batteries
* 3 Amazon Basics alkaline AA batteries
* 3 Safeway alkaline AA batteries

# Sample measurement output

This is what the output of battery-monitor.py looks like:

    Minutes,Time,random0,random1,random2
    0,2022/01/30 13:35:02,1.245878,1.227297,1.425544
    5,2022/01/30 13:40:02,1.176539,1.148341,1.373175
    10,2022/01/30 13:45:02,1.06455,1.02905,1.264408
    15,2022/01/30 13:50:02,1.011325,0.9863492,1.223268
    20,2022/01/30 13:55:02,0.9976287,0.9734584,1.210378
    25,2022/01/30 14:00:02,0.9766811,0.9500938,1.187819
    30,2022/01/30 14:05:02,0.9637903,0.9404257,1.180568

# FIXMEs

* The connections on the breadboard were very sensitive to touch and
  measurements were affected sometimes.  After the first few rounds of
  experimentation I ended up soldering some of the connections better
  but there is still room for improvement.

* Voltage readings at ADC2 are consistently higher than the others.  I
  haven't investigated this.

* It's too hard to get the batteries out of the older.  It needs one
  of those ribbons that lays under the batteries that you can use to
  pull them up.  And the holder needs to be mounted to something the
  user easily can apply force to.

