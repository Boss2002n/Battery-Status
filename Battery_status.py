import psutil

def get_battery_status():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    return (plugged, percent)

plugged, percent = get_battery_status()
if plugged:
    print("Battery is charging. Charging at {}%".format(percent))
else:
    print("Battery is discharging. Remaining at {}%".format(percent))
