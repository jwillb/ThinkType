import keyboard as kb
from time import sleep

def toggle_led(state):
    led = open("/sys/kernel/debug/ec/ec0/io", "wb")
    led.seek(12)

    if state:
        led.write(b"\x8a")  # LED On
    else:
        led.write(b"\x0a")  # LED Off

    led.flush()

esc_count = 0

def blink_led():
    toggle_led(True)
    sleep(0.1)
    toggle_led(False)

keys_list = ["Enter", "Space", "Tab", "Shift", "Alt", "Backspace", "Delete", "esc"]

while True:
    if kb.is_pressed(keys_list[0]):
        blink_led()
    elif kb.is_pressed(keys_list[1]):
        blink_led()
    elif kb.is_pressed(keys_list[2]):
        blink_led()
    elif kb.is_pressed(keys_list[3]):
        blink_led()
    elif kb.is_pressed(keys_list[4]):
        blink_led()
    elif kb.is_pressed(keys_list[5]):
        blink_led()
    elif kb.is_pressed(keys_list[6]):
        blink_led()
    elif kb.is_pressed(keys_list[7]):
        esc_count += 1

    if esc_count <= 5 and kb.is_pressed(keys_list):
        esc_count = 0
    elif esc_count == 5:
        exit()
