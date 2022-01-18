class gpioMaster:
    

    gpioId = 0

    def __init__(self, pinNumber):
        import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library 
        
        self.pinNumber = pinNumber
        self.gpioId = gpioMaster.gpioId
        gpioMaster.gpioId += 1

        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BOARD) # Use physical pin numbering


