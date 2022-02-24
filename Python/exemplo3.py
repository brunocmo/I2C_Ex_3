import RPi_I2C_driver
import smbus2
import bme280
from time import *


porta_i2c = 1
endereco = 0x76
bus = smbus2.SMBus(porta_i2c)

calibracao_parametros = bme280.load_calibration_params(bus, endereco)

dado = bme280.sample(bus, endereco, calibracao_parametros)

mylcd = RPi_I2C_driver.lcd()

display1 = "Temperatura:    "
display2 = (str(dado.temperature))[0:5] + "°C"
mylcd.lcd_display_string(display1, 1)
mylcd.lcd_display_string(display2, 2)

print(display1)
print(display2)

sleep(1)

display1 = "Humidade:       "
display2 = (str(dado.humidity))[0:5] + "%"
mylcd.lcd_display_string(display1, 1)
mylcd.lcd_display_string(display2, 2)

print(display1)
print(display2)


sleep(1)

display1 = "Pressao:        "
display2 = (str(dado.pressure))[0:6] + "hPa"
mylcd.lcd_display_string(display1, 1)
mylcd.lcd_display_string(display2, 2)

print(display1)
print(display2)
