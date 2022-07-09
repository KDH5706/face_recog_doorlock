import RPi.GPIO as GPIO 
import time

# 사용할 GPIO핀의 번호를 선정합니다.
led_pin = 14
button_pin = 15

# boolean 변수 설정 
light_on = False
 # 불필요한 warning 제거
GPIO.setwarnings(False) 
# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM) 
# 버튼 핀의 IN/OUT 설정 , PULL DOWN 설정 
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
# LED 핀을 출력모드로 설정
GPIO.setup(led_pin, GPIO.OUT)

# button_callback 함수를 정의합니다.
def button_callback(channel):
    global light_on    # Global 변수선언 
    print("Button pushed!")
    if light_on == False:  # LED 불이 꺼져있을때 
        GPIO.output(led_pin,1)   # LED ON 
        print("LED ON!")
    else:                                # LED 불이 져있을때 
        GPIO.output(led_pin,0)  # LED OFF
        print("LED OFF!")
    light_on = not light_on  # False <=> True


# Event 방식으로 핀의 Rising 신호를 감지하면 button_callback 함수를 실행합니다.
# 300ms 바운스타임을 설정하여 잘못된 신호를 방지합니다.
GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_callback, bouncetime=300)

while 1: time.sleep(0.1) # 0.1초 딜레이