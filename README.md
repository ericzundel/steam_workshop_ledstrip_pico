# steam_workshop_ledstrip_pico

Eric Z. Ayers <ericzundel@gmail.com>

This project is designed for a 45 minute workshop for 8th grade (13 year old) students at Charles R. Drew Charter School in Atlanta, Georgia USA. If you find this useful in your environment, I would love to hear from you!

The goals of the workshop were:

- To develop enthusiasm among rising high school students
for engineering.
- To get some hands on experience wiring up components
- To get some experience changing a computer program.


- [Student handout](https://docs.google.com/document/d/e/2PACX-1vSE6z_H7V74koNKeVgu1kfEfqWtKPY3R7keaxq7UDjTkhpBHoc52DhxsD8lurqK2ZTsT8mfkcEvM0S_/pub)
- [Assistant handout](https://docs.google.com/document/d/e/2PACX-1vSa5i62UpHBG86p7boatN77IFu9AuDR94MtcsdqDq_Wuo8tprsK84hueinjkh-Wr5RQYVI2xfdaMRjb/pub)

## Environment

We made use of windows laptops with the Mu Editor installed.  We used Raspberry Pi Pico W hardware and a NeoPixel LED strip clone.  I cut a strip of 10 pixels for each  laptop and pre-soldered breadboard wires onto the Neopixels.  I used heat shrink over the end as strain relief based on my experience with breakage in  the past.

## Usage

These files should be copied to the Pico filesystem.  There is a bash shell scripted named 'copy_to_pico.sh' that helps with that.  Once the files are on the chip, a MSDOS .bat file named 'reset.bat' resets the files to the initial state.


## Philosopy

This is not meant to be an exercise in learning how a computer language works, understanding hardware, or using a canonical computer language.  The workshop was designed so that students could experience success in programming hardware a short time frame. To that end, the example works out of the box. I also used macros to create shortcuts to make additional coding simpler and more forgiving.  Also, I wanted to give enough depth to the exercise so that eager students would not get bored, so there are multiple goodies commented out in the file for students to explore.  At the advice of a student helper, I gave the students the experience of wiring the LED strip to the Arduino in each workshop (even though it was time consuming) to give the students hands on experience.

To inspire students, I tacked up a 100 led strand to the front of the classroom with all of the logic uncommented and turned it on once we finished wiring up the hardware.

In March 2022 I ran a version of this workshop using the Arduino environment four times with 15-20 8th grade students. In each workshop, every student got their light strip to work.

## Notes on the code

### code-steamworkshop-example.py

This is ripped off from the (Adafruit website neopixel example)[https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel].  I added a few functions to mimic my workshop from 2022 in C++.

## lib/ directory

The library files in the lib/ directory are for student convenience. They are currently compiled for CircuitPython 9
