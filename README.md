# microcovid
A micropython COVID-19 display on the TTGO 16M Bytes (128M Bit) Pro ESP32 OLED V2.0 using urequests and ssd1306.

Esp32 used: TTGO 16M Bytes (128M Bit) Pro ESP32 OLED V2.0

Connects to https://coronavirus-19-api.herokuapp.com api, receives current COVID-19 data as json and parses it.
Currently displays only when button GPIO0 is pressed to save energy.

![microcovidpythonesp32ttgo](https://user-images.githubusercontent.com/936824/77230367-f4fd0600-6b50-11ea-9529-6f3d97d434f2.gif
)

How to:
- Install micropython on esp32 via esptool: https://docs.micropython.org/en/latest/esp32/tutorial/intro.html
- Connect to esp32 via terminal/serial (picocom or similar) see: https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html
- Configure webrepl via "import webrepl_setup"
- Setup wifi: https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html
- Select your country/countries: https://coronavirus-19-api.herokuapp.com/ + Your Country/Countries
- Edit main.py for your Country/Countries (Line 94, 131, 168)
- Upload boot.py, ssd1306.py and main.py via webrepl (http://micropython.org/webrepl/)
- Press the GPIO0 button to see new stats
- Wash your hands & stay home

Credits: 
- https://github.com/javieraviles/covidAPI
- https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py
- https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/
- https://bcmullins.github.io/parsing-json-python/
