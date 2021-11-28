# libbmp280
BMP280 Python easy library (temperature sensor)<br>
<br>
Requirements installation:<br>
pip install bmp280<br>
For usage with Python 3 install also for Python 3:<br>
pip3 install bmp280
<br><br>
Usage: clone libbmp280 and include into your Python script with "include libbmp280". Insert into libbmp280.py your values for calibration of the BMP280 sensor. (eg. if the real temperature is 25°C, but sensor shows 26.5°C, write into "temperature_calibration = -1.5", and so with pressure. Use libbmp280.temperature() or libbmp280.pressure() in your script to get the values. You can get also two-decimal rounded values (please inspect the script).
