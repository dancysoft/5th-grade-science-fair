# MicroPython code intended to run on a Raspberry Pi Nano which 3 ADC
# converters which we use to measure the voltage of 3 battery at a
# time.

from machine import Pin, ADC
import time

# ADC voltage reference. We're using the Nano's internal reference of 3.3V.
VREF = 3.3
# Load resistance
R = 20 # Ohms

# FIXME: Use configuration file
batteries = {
    0: { "name": "safeway0" },
    1: { "name": "safeway1"},
    2: { "name": "safeway2"},
    }

def read_adc(adc):
    raw = adc.read_u16()
    return raw / ( 65535 / VREF )
    
def timestring():
    (year, month, day, hour, minute, second, dow, doy) = time.localtime()
    return "{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}".format(year, month, day, hour, minute, second)

def main():
    for channel, battery in batteries.items():
        battery["adc"] = ADC(channel)
        
    names = [None]*len(batteries)
    for channel, battery in batteries.items():
        names[channel] = battery["name"]
                
    print("Minutes,Time,{}".format(",".join(names)))
        
    start = time.time()
        
    while True:
        reports = [None] * len(batteries)
        
        for channel, battery in batteries.items():
            reports[channel] = str(read_adc(battery["adc"]))
        print("{},{},{}".format((time.time()-start) // 60, timestring(), ",".join(reports)))
        # FIXME: Make configurable at runtime
        #interval=1 # Seconds
        interval = 60 * 5
        time.sleep(interval)

if __name__ == '__main__':
    main()
