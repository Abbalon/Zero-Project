from time import sleep

from digi.xbee.devices import ZigBeeDevice
from gpiozero import Servo, LED
from gpiozero.pins.pigpio import PiGPIOFactory

# Declaración de los pines que vamos a usar
servo_pin = 18
ok_led_pin = 25
warn_led_pin = 26
error_led_pin = 6
monitor_led_pin = 16

factory = PiGPIOFactory(host='192.168.10.15')
# Seteamos el pin de datos del servo  un puerto PWM
servo = Servo(servo_pin, pin_factory=factory)
# Seteo de los pines
ok_led = LED(ok_led_pin, pin_factory=factory)
warn_led = LED(warn_led_pin, pin_factory=factory)
error_led = LED(error_led_pin, pin_factory=factory)
monitor_led = LED(monitor_led_pin, pin_factory=factory)
#Configuramos la antena Xbee
# Comando para escanear puertos {dmesg | grep tty}
# se accede a traves de RS232 masterport
xbee = ZigBeeDevice("dev/tty")

print("Empezamos")

for x in range(5):
    ok_led.blink(1, 1, 5)
    warn_led.blink(1, 1, 5)
    error_led.blink(1, 1, 5)
    monitor_led.blink(1, 1, 5)
    print(servo.value)
    servo.min()
    print(servo.value)
    sleep(5)
    servo.mid()
    sleep(5)
    servo.max()
    sleep(5)
    print(x)

print("e voila")
