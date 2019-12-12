import sensor
import image
import lcd
import time

clock = time.clock()
#lcd.direction(lcd.YX_RLUD)
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(1)
sensor.set_hmirror(1)
sensor.run(1)
sensor.skip_frames(30)
#sensor.set_brightness(17)
while True:
    clock.tick()
    img = sensor.snapshot()
    res = img.find_qrcodes()
    fps =clock.fps()
    if len(res) > 0:
        #img.draw_string(2,2, res[0].payload(), color=(0,128,0), scale=2)
        tupleboxa = res[0].rect()
        img.draw_string(40,20, res[0].payload(), (236,36,36),scale=1.5)
        img.draw_rectangle(tupleboxa,(236,36,36))
        print(res[0].payload())
    lcd.display(img)

