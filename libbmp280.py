import time
from bmp280 import BMP280

temperature_calibration = -0.77
pressure_calibration = 22

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

# Initialise the BMP280
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

def zaokrouhlit(val, dec):
    if (dec != False):
        return "{:.2f}".format(val)
    else:
        return val

def temperature(decimals=False):
    return zaokrouhlit(bmp280.get_temperature() + temperature_calibration, decimals)
def pressure(decimals=False):
    return zaokrouhlit(bmp280.get_pressure() + pressure_calibration, decimals)
def raw_temperature(decimals=False):
    return zaokrouhlit(bmp280.get_temperature(), decimals)
def raw_pressure(decimals=False):
    return zaokrouhlit(bmp280.get_pressure(), decimals)

def initialization():
  init_temp = raw_temperature()
  init_press = raw_pressure()

initialization()
