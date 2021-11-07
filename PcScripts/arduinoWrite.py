import serial
from PcScripts import TextToOutput as t
import time

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=1)

string = input("Enter a string: ")
l = t.textToOutput(string)
print(l)

time.sleep(0.5)
for i in l:
    send = str(i)
    delay = 0.1

    if send == "2" or send == "3":                      # choose the delay value
        delay = .6
    elif send != "1":                                   # can only be 6 or 7 if not 2 or 3
        delay = 3

    arduino.write(bytes(send, 'utf-8'))
    data = arduino.readline().decode('utf-8')

    print(str(time.ctime()) + ' SENT: {}'.format(send))
    print(str(time.ctime()) + ' RCVD: {}'.format(data))
    time.sleep(delay * 0.25)                           # Blink LED

arduino.write(bytes("1", 'utf-8'))
data = arduino.readline().decode('utf-8')
print(str(time.ctime()) + ' SENT: {}'.format("1"))
print(str(time.ctime()) + ' RCVD: {}'.format(data))           # LED kill sequence after code executes