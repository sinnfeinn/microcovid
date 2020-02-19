# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, I2C
import ssd1306
from time import sleep
import urequests

def extract_element_from_json(obj, path):
    '''
    Extracts an element from a nested dictionary or
    a list of nested dictionaries along a specified path.
    If the input is a dictionary, a list is returned.
    If the input is a list of dictionary, a list of lists is returned.
    obj - list or dict - input dictionary or list of dictionaries
    path - list - list of strings that form the path to the desired element
    '''
    def extract(obj, path, ind, arr):
        '''
            Extracts an element from a nested dictionary
            along a specified path and returns a list.
            obj - dict - input dictionary
            path - list - list of strings that form the JSON path
            ind - int - starting index
            arr - list - output list
        '''
        key = path[ind]
        if ind + 1 < len(path):
            if isinstance(obj, dict):
                if key in obj.keys():
                    extract(obj.get(key), path, ind + 1, arr)
                else:
                    arr.append(None)
            elif isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        extract(item, path, ind, arr)
            else:
                arr.append(None)
        if ind + 1 == len(path):
            if isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        arr.append(item.get(key, None))
            elif isinstance(obj, dict):
                arr.append(obj.get(key, None))
            else:
                arr.append(None)
        return arr
    if isinstance(obj, dict):
        return extract(obj, path, 0, [])
    elif isinstance(obj, list):
        outer_arr = []
        for item in obj:
            outer_arr.append(extract(item, path, 0, []))
        return outer_arr


#define button
button = Pin(0, Pin.IN)

#turn LED on
led = Pin(2, Pin.OUT)


#set reset Pin high to activate display
pin16 = Pin(16, Pin.OUT)
pin16.value(1)

# ESP32 Pin assignment
i2c = I2C(-1, scl=Pin(15), sda=Pin(4))

# ESP8266 Pin assignment
#i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

#oled_invert = true
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)




while True:
    if not button.value():
        led.on()
#get weather json data
        response = urequests.post("http://api.openweathermap.org/data/2.5/weather?id=5746545&appid=d49b96661878b91463d9daccc71e6def&units=metric&lang=de")
        parsed = response.json()
#weather parsed to display
        position_final = parsed["name"]
        position_string = str(position_final)
        positionstr = position_string
        oled.text("<<<" + " " + positionstr + " " + ">>>", 0, 0)
        oled.show()
        temp_final = extract_element_from_json(parsed, ["main", "temp"])
        temperature_string = str(temp_final)
        tempstr = temperature_string[1:-1]
        oled.text("Temp:" + ' ' +  tempstr  + "C", 0, 10)
        oled.show()
        pressure_final = extract_element_from_json(parsed, ["main", "pressure"])
        pressure_string = str(pressure_final)
        pressurestr = pressure_string[1:-1]
        oled.text("Pressure:" + ' ' +  pressurestr, 0, 20)
        oled.show()
        humidity_final = extract_element_from_json(parsed, ["main", "humidity"])
        humidity_string = str(humidity_final)
        humiditystr = humidity_string[1:-1]
        oled.text("Humidity:" + ' ' +  humiditystr, 0, 30)
        oled.show()
        description_final = extract_element_from_json(parsed, ["weather", "description"])
        description_string = str(description_final)
        descriptionstr = description_string[2:-2]
        oled.text(descriptionstr, 0, 40)
        oled.show()
        wind_final = extract_element_from_json(parsed, ["wind", "speed"])
        deg_final = extract_element_from_json(parsed, ["wind", "deg"])
        wind_string = str(wind_final)
        deg_string = str(deg_final)
        windstr = wind_string[1:-1]
        degstr = deg_string[1:-1]
        oled.text("Wind:" + ' ' + windstr + "ms" + ',' + degstr + "deg", 0, 50)
        oled.show()
        sleep(4)
        oled.fill(0)
        oled.show()
        oled.text("Sleeping", 0, 0)
        oled.show()
        sleep(1)
    else:
        led.off()
        oled.fill(0)
        oled.show()
    sleep(.4)
