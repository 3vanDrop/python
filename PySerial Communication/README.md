# Description
serial_communication_script.py has been created to demonstrate pyserial usage communication between two serial ports. Find usage examples & instructions below. 

# Requirements
### Python
- Using python 3+

### PIP
- Pip installed and ready to use.

# Virtual Setup and Usage
****
### Setup Virtual Serial Port Driver
1. Download **Virtual Serial Port software demo** from its official website: https://www.virtual-serial-port.org/vspd-post-download.html and Install it.
2. Open **Virtual Serial Port** and Under **Create a bundle of serial ports** section select **Pair** option.
3. Select two available ports below **Virtual ports to pair** and click on **Create** button.
4. Confirm new ports created are listed in Device Manager. (optional, script takes care of this)

### Install the requirements
```Shell
pip install pyserial
```

### Serial Communication Script usage
```Shell
serial_communication_script.py [serial_device_to_write] [serial_device_to_read] [optional, reading timeout]

        Usage Example 1:
        e.g. serial_communication_script.py COM1 COM2 30
        Where COM1 = serial port to write, COM2 = serial port to listen & timeout specified is an integer 30.

        Usage Example 2:
        e.g. serial_communication_script.py COM1 COM2
        Where COM1 = serial port to write, COM2 = serial port to listen & timeout is NOT specified, so default TIMEOUT = 20 is taken.
``` 

### Output from a successful script execution
```Shell
C:\[WORKING_DIR]> py .\serial_communication_script.py COM1 COM2
Successfully connected to 'COM1'!
Successfully connected to 'COM2'!
SerialPortReader.run() - Listening to 'COM2' for 20 seconds.
Tx: [COM1] 0 - Hello World!
Rx: [COM2] 0 - Hello World!
Tx: [COM1] 1 - Hello World!
Rx: [COM2] 1 - Hello World!
Tx: [COM1] 2 - Hello World!
Rx: [COM2] 2 - Hello World!
Tx: [COM1] 3 - Hello World!
Rx: [COM2] 3 - Hello World!
Tx: [COM1] 4 - Hello World!
Rx: [COM2] 4 - Hello World!
Tx: [COM1] 5 - Hello World!
Rx: [COM2] 5 - Hello World!
Tx: [COM1] 6 - Hello World!
Rx: [COM2] 6 - Hello World!
Tx: [COM1] 7 - Hello World!
Rx: [COM2] 7 - Hello World!
Tx: [COM1] 8 - Hello World!
Rx: [COM2] 8 - Hello World!
Tx: [COM1] 9 - Hello World!
Rx: [COM2] 9 - Hello World!
SerialPortReader.run() - 20s timeout has been reached!
```
