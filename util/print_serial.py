import sys
import time
import serial
import serial.tools.list_ports

def setupSerial():
    ser = serial.Serial(
        port="/ttyAMA0sdfjksdfh",
        baudrate=57600,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS,
        timeout=0.1
    )

    ser.isOpen()
    return ser    

def main():
    ser = setupSerial()

    while True:
        time.sleep(0.01)
        out = ser.readline()
        out = str(out)[2:-5]

        if out != '':
            print(out)

if __name__ == "__main__":
    main()