class mobile:

    def __init__self(self):
        pass

    def calling(self):
        print("invoking calling functiom")

    def sms(self):
        print("invoking sms Method")

    def games(self):
        print("invoking games")

class vivo_y21e(mobile):

    def cam(self):
        print("invoking can method")

    def music(self):
        print("invoking music method")

    def video_call(self):
        print("invoking video call")

vivo=vivo_y21e()
vivo.music()
vivo.cam()
vivo.video_call()
vivo.games()