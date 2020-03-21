# Parts of this code are derived from https://RandomNerdTutorials.com, extract_element_from_json by https://bcmullins.github.io/parsing-json-python/

from machine import Pin, I2C
import ssd1306
from time import sleep
import urequests

#extract part of the json response
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


# define button
button = Pin(0, Pin.IN)

# turn LED on
led = Pin(2, Pin.OUT)


# set reset Pin high to activate display (needed for banggood TTGO clone)
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

# on keypress show covid data
while True:
    if not button.value():
        led.on()
# get Covid json data USA
        response = urequests.get("https://coronavirus-19-api.herokuapp.com/countries/USA")
        parsed = response.json()
# Data parsed to display
        position_final = parsed["country"]
        position_string = str(position_final)
        positionstr = position_string
        oled.text("<<<" + " " + positionstr + " " + ">>>", 0, 0)
        oled.show()
        cases = parsed["cases"]
        cases_string = str(cases)
        casesstr = cases_string
        oled.text("Cases:" + casesstr, 0, 10)
        oled.show()
        todayCases = parsed["todayCases"]
        todayCases_string = str(todayCases)
        todayCasesstr = todayCases_string
        oled.text("New Cases:" + todayCasesstr, 0, 20)
        oled.show()
        recovered = parsed["recovered"]
        recovered_string = str(recovered)
        recoveredsstr = recovered_string
        oled.text("Recovered:" + recoveredsstr, 0, 30)
        oled.show()
        deaths = parsed["deaths"]
        deaths_string = str(deaths)
        deathssstr = deaths_string
        oled.text("Deaths:" + deathssstr, 0, 40)
        oled.show()
        casepermil = parsed["casesPerOneMillion"]
        casepermil_string = str(casepermil)
        casepermilstr = casepermil_string
        oled.text("Cases/Mill:" + casepermilstr, 0, 50)
        oled.show()
        sleep(6)
        oled.fill(0)
        oled.show()
# get Covid json data Austria
        response2 = urequests.get("https://coronavirus-19-api.herokuapp.com/countries/Austria")
        parsed = response2.json()
# Data parsed to display
        position_final = parsed["country"]
        position_string = str(position_final)
        positionstr = position_string
        oled.text("<<<" + " " + positionstr + " " + ">>>", 0, 0)
        oled.show()
        cases = parsed["cases"]
        cases_string = str(cases)
        casesstr = cases_string
        oled.text("Cases:" + casesstr, 0, 10)
        oled.show()
        todayCases = parsed["todayCases"]
        todayCases_string = str(todayCases)
        todayCasesstr = todayCases_string
        oled.text("New Cases:" + todayCasesstr, 0, 20)
        oled.show()
        recovered = parsed["recovered"]
        recovered_string = str(recovered)
        recoveredsstr = recovered_string
        oled.text("Recovered:" + recoveredsstr, 0, 30)
        oled.show()
        deaths = parsed["deaths"]
        deaths_string = str(deaths)
        deathssstr = deaths_string
        oled.text("Deaths:" + deathssstr, 0, 40)
        oled.show()
        casepermil = parsed["casesPerOneMillion"]
        casepermil_string = str(casepermil)
        casepermilstr = casepermil_string
        oled.text("Cases/Mill:" + casepermilstr, 0, 50)
        oled.show()
        sleep(6)
        oled.fill(0)
        oled.show()
# get Covid json data Belgium
        response3 = urequests.get("https://coronavirus-19-api.herokuapp.com/countries/Belgium")
        parsed = response3.json()
# Data parsed to display
        position_final = parsed["country"]
        position_string = str(position_final)
        positionstr = position_string
        oled.text("<<<" + " " + positionstr + " " + ">>>", 0, 0)
        oled.show()
        cases = parsed["cases"]
        cases_string = str(cases)
        casesstr = cases_string
        oled.text("Cases:" + casesstr, 0, 10)
        oled.show()
        todayCases = parsed["todayCases"]
        todayCases_string = str(todayCases)
        todayCasesstr = todayCases_string
        oled.text("New Cases:" + todayCasesstr, 0, 20)
        oled.show()
        recovered = parsed["recovered"]
        recovered_string = str(recovered)
        recoveredsstr = recovered_string
        oled.text("Recovered:" + recoveredsstr, 0, 30)
        oled.show()
        deaths = parsed["deaths"]
        deaths_string = str(deaths)
        deathssstr = deaths_string
        oled.text("Deaths:" + deathssstr, 0, 40)
        oled.show()
        casepermil = parsed["casesPerOneMillion"]
        casepermil_string = str(casepermil)
        casepermilstr = casepermil_string
        oled.text("Cases/Mill:" + casepermilstr, 0, 50)
        oled.show()
        sleep(6)
        oled.fill(0)
        oled.show()
        oled.text(">>>>>>>><<<<<<<<", 0, 0)
        oled.text("      WASH", 0, 10)
        oled.text("      YOUR", 0, 20)
        oled.text("      HANDS", 0, 30)
        oled.text("  & STAY HOME", 0, 40)
        oled.text(">>>>>>>><<<<<<<<", 0, 50)
        oled.show()
        sleep(6)
    else:
        led.off()
        oled.fill(0)
        oled.show()
    sleep(.4)
