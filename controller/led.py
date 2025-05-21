import serial
import time
from serial.tools import list_ports

def list_com_ports():
    """
    Returns a list of available COM port names.
    """
    return [port.device for port in list_ports.comports()]

def open_com_port(port_name, baudrate=9600, timeout=12):
    ser = serial.Serial(port_name, baudrate=baudrate, timeout=timeout)
    time.sleep(1)
    return ser

def close_com_port(ser):
    if ser.is_open:
        ser.close()
        print(f"Closed COM port: {ser.name}")
    else:
        print(f"COM port {ser.name} is already closed.")

def send_command(ser, command):
    if ser.is_open:
        ser.write(command.encode('ascii'))
        print(f"Sent command: {command}")
        response = ser.read_until(b'\r')
        print(f"Received response: {response.decode('ascii').strip('\r')}")
    else:
        print(f"COM port {ser.name} is not open. Cannot send command.")
        raise Exception("COM port is not open.")

# Example usage
if __name__ == "__main__":
    ser = open_com_port('COM12')
    print(ser.is_open)
    send_command(ser, 'LX,0,100,01000\r')
    # send_command(ser, 'RS\r')
    close_com_port(ser)
