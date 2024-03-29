import utime
from Maix import GPIO
from board import board_info
from fpioa_manager import fm

# register pin to gpiohs0,
# arg force means force register no matter we have registered before or not
# if arg force=False(by default), register func will return a tuple that registered info,
#                                                           or return number 1
fm.register(board_info.LED_R, fm.fpioa.GPIO0, force=True)
fm.register(board_info.LED_G, fm.fpioa.GPIOHS0, force=True)
fm.register(board_info.LED_B, fm.fpioa.GPIO1, force=True)

led_r = GPIO(GPIO.GPIO0, GPIO.OUT)
led_g = GPIO(GPIO.GPIOHS0, GPIO.OUT)
led_b = GPIO(GPIO.GPIO1, GPIO.OUT)

i = 0
status = 0
while i<50:
    led_r.value(status)
    utime.sleep_ms(500)
    led_g.value(status)
    utime.sleep_ms(500)
    led_b.value(status)
    utime.sleep_ms(500)
    i+=1
    status = 0 if (status==1) else 1

fm.unregister(board_info.LED_R, fm.fpioa.GPIO0)
fm.unregister(board_info.LED_G, fm.fpioa.GPIOHS0)
fm.unregister(board_info.LED_B, fm.fpioa.GPIO1)

