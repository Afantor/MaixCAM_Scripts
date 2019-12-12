from machine import Timer,PWM
import time
from board import board_info
from fpioa_manager import fm

tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
ch0 = PWM(tim, freq=3000000, duty=20, pin=board_info.LED_G, enable=False)
ch0.enable()
time.sleep(3)
ch0.freq(2000000)
print("freq:",ch0.freq())
ch0.duty(60)
time.sleep(3)
ch0.disable()
