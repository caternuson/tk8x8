# tk8x8
Python 2.7 Tkinter based GUI for interacting with Adafruit 8x8 LED matrices.
<img src="tk8x8_heart.png" style="float: right;"/>

# Dependencies
* Python Imaging Library (PIL)
    * https://pypi.python.org/pypi/PIL
* Adafruit Python Library for LED Backpacks
    * https://github.com/adafruit/Adafruit_Python_LED_Backpack

# Install
Simply clone this repo and run:
```
$ git clone https://github.com/caternuson/tk8x8.git
$ cd tk8x8
$ sudo python tk8x8.py
```
# Configure
Set the I2C address of the LED 8x8 matrix:
```python
I2C_ADDRESS = 0x70
```

Set the LED color by selecting an option from the `LED_COLOR` dictionary:
```python
LED_ON_COLOR = LED_COLOR["red"]
```

Additional color definitions can be added to the `LED_COLOR` dictionary in string
format. However, the syntax must be supported by both PIL and Tkinter.
The following are options:
* '#rgb'
* '#rrggbb'
* 'red'

Set the names of the output files:
```python
IMG_FILE = "led8x8.jpg"
TXT_FILE = "led8x8.txt"
```