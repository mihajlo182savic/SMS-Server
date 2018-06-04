import serial
from curses import ascii
from time import gmtime, strftime, sleep
import sys
from utils import log

class SMS:
    def __init__(self, baudrate=115200, device="/dev/ttyUSB0", pin=2391):
        self.modem = serial.Serial(device, baudrate, timeout=5)
        print "[INFO ] Starting connection with modem at " + device + "..."

        self.modem.write(b'AT\r')
        self.getresponse(0)
        response = self.modem.read(4)
        if "OK" in response:
            print "[INFO ] Connected successfully."
            self.changeToTextMode()
            log("warning", "modem", "Konekcija sa modemom uspesno uspostavljena")
        elif "NO CARRIER" in response:
            log("danger", "error", "Na SIM katici nema 3G konekcije")
            print "[ERROR] There is no 3G connection! :/"
        else:
            log("danger", "error", "Doslo je do greske prilikom postavljanja modema")
            print "[ERROR] Something went wrong :("

    def send(self, receiver, message):
        if receiver is not None and message is not None:
            print "[DEBUG] Sending SMS with details: "
            print "Reciever: %s" % receiver
            print "Message: %s" % message
            print "Time: %s" % strftime("%Y-%m-%d %H:%M:%S", gmtime())

            self.modem.write(b'AT+CMGS="%s"\r' % receiver)
            sleep(0.5)
            self.modem.write(b'%s\r' % message)
            sleep(0.5)
            self.modem.write(ascii.ctrl('z'))
            sleep(0.5)
            response = self.modem.readlines()
            if "+CMGS" in response[-3]:
                print "[INFO ] SMS sent successfully!"
            	log("success", "sms", "Poruka sa sledecim detaljima je uspesno poslata", more="Primalac: %s Poruka: %s" % (receiver, message))
            else:
                print "[ERROR] Something went wrong while sending SMS!"
            	log("danger", "sms", "Doslo je do greske prilikom slanja poruke", more="Primalac: %s Poruka: %s" % (receiver, message))
        else:
            print ""

  

    def changeToTextMode(self):
        print "[INFO ] Setting module to text mode"
        self.modem.write(b'AT+CMGF=1\r')
        response = self.getresponse(1)
        if "OK" in response:
            print "[INFO ] Text Mode activated."
        else:
            print "[ERROR] Could not set modem to text mode."

    def disconnect(self):
        self.modem.close()

    def getresponse(self, skip):
        for lines in range(0, skip):
            while True:
                ch = self.modem.read(1)
                if ch == '\r':
                    break
        buf = ""
        while True:
            ch = self.modem.read(1)
            if ch == '\r':
                break
            buf += ch
        return buf


phone = SMS()
phone.send("0648550254", "hehexd")
