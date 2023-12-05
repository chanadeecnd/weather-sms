from weather import get_weather
from message import send_message

lat = 13.82535264157781
lon = 100.51602189588719
result = get_weather(lat, lon, True)
print(result)

send_message('0858762024',"test sent😘")

