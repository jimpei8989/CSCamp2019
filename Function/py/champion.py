class Champion:
    def __init__(self):
        self.name = 'Teemo'
        self.atk = 54.0
        self.hp = 528.0

        x = 3
        y = 4
        z = 5
        self.lucky_num = x * y * z

    def speak(self):
        def SiriSays(s):
            print('Siri Says:', s)
        SiriSays('Captain Teemo on duty')

def main():
    teemo = Champion()
    print(type(teemo))

    teemo.speak()

main()
