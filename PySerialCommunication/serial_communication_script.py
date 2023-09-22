"""Serial Communication between two ports by Evan Tirado"""
from serial import Serial, serialutil
import serial.tools.list_ports as list_ports
import threading
import time
import sys


class SerialPortException(Exception):
    """SerialPortException"""


class SerialPort(threading.Thread):
    """SerialPort Class"""
    DEFAULT_BAUDRATE = 9600

    def __init__(self, port: str, baudrate: int = DEFAULT_BAUDRATE):
        """Init Serial port thread instance

        :param port: str, serial port
        :param baudrate: int, optional serial port baudrate
        """
        threading.Thread.__init__(self)

        self.port = port
        self.baudrate = baudrate
        self.serial_port = self._open_port(port, baudrate=baudrate)

    def _open_port(self, port: str, baudrate: int):
        """Open port with current settings. This may throw a
        SerialPortException if the port cannot be opened.

        :param port: str, serial port
        :param baudrate: int, optional serial port baudrate
        """
        try:
            _open_port = Serial(port)
            self._print_stdout(f"Successfully connected to '{port}'!")

            return _open_port
        except serialutil.SerialException as err:
            error_str = (f"Unable to connect to '{port}:{baudrate}'! "
                         f"Make sure port is available and try again. {err}")
            raise SerialPortException(error_str)

    def _print_stdout(self, text):
        """print_stdout

        :param text: str, text to be sent to stdout
        """
        if "\n" not in text:
            text += "\n"
        sys.stdout.write(text)
        sys.stdout.flush()

    def write(self, data: str):
        """Output the given byte string over the serial port"""
        try:
            self._print_stdout(f"Tx: [{self.serial_port.port}] {data}")
            if "\n" not in data:
                data += "\n"
            self.serial_port.write(bytes(data, encoding="ascii"))
        except serialutil.SerialException as err:
            self._print_stdout(f"Unable to write '{data}' on Serial port:"
                               f"'{self.serial_port.port}'. - {err}")

    def read_until(self):
        """Read until an expected sequence is found ('\n' by default), the size
        is exceeded or until timeout occurs.

        :returns rx: str, data from serial port
        """
        try:
            rx = str(self.serial_port.read_until(), encoding="utf-8")
            self._print_stdout(f"Rx: [{self.serial_port.port}] {rx}")
            return rx
        except serialutil.SerialException as err:
            self._print_stdout(f"ERROR - Unable to listen Serial port "
                                f"'{self.serial_port.port}'. {err}")


class SerialPortReader(SerialPort):
    """SerialPortReader"""

    DEFAULT_TIMEOUT = 15  # seconds
    DEFAULT_RATE = 0.02  # check buffer rate in seconds

    def __init__(self, port, timeout: int = DEFAULT_TIMEOUT,
                 rate_s: int = DEFAULT_RATE, *args, **kwargs):
        """SerialPortReader.__init__
        :param timeout: port listen timeout, 'DEFAULT_TIMEOUT' by default.
        :param rate_s: refresh rate to read serial buffer,
            'DEFAULT_RATE' by default
        """
        super().__init__(port, *args, **kwargs)
        self.timeout = timeout
        self.rate_s = rate_s

    def run(self):
        """Run listening loop until timeout occurs
        """
        init_time = time.monotonic()
        self._print_stdout(f"{self.__class__.__name__}.run() - Listening to "
                           f"'{self.port}' for {self.timeout} seconds.")
        while (self.timeout == 0 or self.serial_port.in_waiting or
               (time.monotonic() - init_time) < self.timeout):
            if self.serial_port.in_waiting:
                self.read_until()

            time.sleep(self.rate_s)

        self._print_stdout(f"{self.__class__.__name__}.run() - {self.timeout}s"
                           " timeout has been reached!")


def check_port_availability(*ports):
    """Exit script if any port is not available"""
    available_ports = [p.device for p in list_ports.comports()]
    for port in ports:
        if port not in available_ports:
            sys.exit(f"ERROR - {port} is not available. "
                     f"{available_ports}")


def help():
    """Print out script usage"""
    script_name = __file__.split("\\")[-1]
    print("PySerial Challenge - Serial Communication Script\n\n"
          f"\tUSAGE: {script_name} <serial_device_to_write> "
          "<serial_device_to_read> <optional, reading timeout>\n\n",
          f"\te.g. {script_name} COM1 COM2 30\n\tWhere COM1 = serial port to "
          "write, COM2 = serial port to listen & timeout specified is an "
          "integer 30.\n\n"
          "\n\tNOTE: This script is CASE SENSITIVE, make sure to specify "
          "serial ports exactly as listed on your Device Manager.\n")


def main():
    LISTEN_TIMEOUT = 20  # default timeout
    TX_MESSAGE = "Hello World!"  # fixed str

    # 1st & 2nd argument are required to specify ports to
    # write & listen, respectively.
    if len(sys.argv) < 3:
        help()
        sys.exit("ERROR - At least 2 ports need to be specified to run "
                 "this script...")

    # 3rd argument is Optional to specify timeout,
    # default is given by LISTEN_TIMEOUT
    if len(sys.argv) > 3:
        try:
            LISTEN_TIMEOUT = int(sys.argv[3])
        except ValueError:
            help()
            sys.exit("ERROR - Timeout must be an integer. Current specified "
                     f"timeout: {sys.argv[3]}")

    # Check if ports are available
    port_1, port_2 = sys.argv[1], sys.argv[2]
    check_port_availability(port_1, port_2)

    com1 = SerialPort(port_1)
    com2_reader = SerialPortReader(port_2, timeout=LISTEN_TIMEOUT)

    com2_reader.start()

    for i in range(10):
        com1.write(f"{i} - {TX_MESSAGE}")
        time.sleep(1)


if __name__ == "__main__":
    main()
