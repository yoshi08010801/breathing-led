import RPi.GPIO as GPIO
import time

LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, 100)
pwm.start(0)

try:
    while True:
        
    #フェードイン
        for duty in range(0, 101, 5):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.05)
            
        #フェードアウト
        for duty in range(100, -1, -5):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.05)
except keyboardInterrupt:
    print("終了します")
        
finally:
    pwm.stop()
    GPIO.cleanup()