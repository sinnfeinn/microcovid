# microweather
A micropython weather display on the TTGO 16M Bytes (128M Bit) Pro ESP32 OLED V2.0 using urequests and ssd1306.

Esp32 used: TTGO 16M Bytes (128M Bit) Pro ESP32 OLED V2.0

Connects to https://openweathermap.org/ api, receives current weather as json and parses it.
Currently displays only when button GPIO0 is pressed to save battery.

How to:
- Install micropython on esp32 via esptool: https://docs.micropython.org/en/latest/esp32/tutorial/intro.html
- Connect to esp32 via terminal/serial (picocom or similar) see: https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html
- Configure webrepl via "import webrepl_setup"
- Setup wifi: https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html
- Create free openweather map account and generate api key: https://home.openweathermap.org/users/sign_up
- Edit main.py for your city (Line 91) and add your api key (also Line 91)
- Upload boot.py, ssd1306.py and main.py via webrepl (http://micropython.org/webrepl/)
- Press the GPIO0 button to see weather
- Profit

Credits: 
https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py
https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/
https://bcmullins.github.io/parsing-json-python/
