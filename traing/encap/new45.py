class Aadhar:
    def __init__(self, name, aadhar_number, dob, finger_print, retina):
        self.name = name
        self.aadhar_number = aadhar_number
        self.dob = dob
        self.finger_print = finger_print
        self.__retina = retina

    def info(self):
        print(f"retina:{self.__retina},aadharno:{self.aadhar_number}")

    def getRetena(self):
        return self.__retina

var=Aadhar("yash",243544,"10-apr-2004","jhgfrbb","ret1")
var.info()
var.getRetena()

