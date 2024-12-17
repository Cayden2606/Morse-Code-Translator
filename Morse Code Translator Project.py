import sys
import time
from AADFramework.ArduinoComponents import DigitalInput, DigitalOutput, ControlBoard

controller = ControlBoard('/dev/cu.usbmodem141301')
buzzer = controller.buildDigitalOutput(12, 'buzzer')
led = controller.buildDigitalOutput(5, 'led')
button_morse = controller.buildDigitalInput(2, 'button_morse')
button_space = controller.buildDigitalInput(4, 'button_space')
button_trans = controller.buildDigitalInput(3, 'button_trans')
button_delete = controller.buildDigitalInput(6, 'button_delete')

xMotor = controller.buildServoMotor(8, 'xMotor')
xMotor.homePos = 180
xMotor.minAngle = 0
xMotor.maxAngle = 180

yMotor = controller.buildServoMotor(9, 'yMotor')
yMotor.homePos = 180
yMotor.minAngle = 0
yMotor.maxAngle = 180

zMotor = controller.buildServoMotor(10, 'zMotor')
zMotor.homePos = 180
zMotor.minAngle = 0
zMotor.maxAngle = 180

dMotor = controller.buildServoMotor(11, 'bMotor')
dMotor.homePos = 180
dMotor.minAngle = 0
dMotor.maxAngle = 180

morse_code_mapping = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.',
                      '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----',
                      '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', 'ㅤ']
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
motor_alpha_angle = {'A': ["xMotor", 170], 'B': ["xMotor", 150], 'C': ["xMotor", 130], 'D': ["xMotor", 110],
                     'E': ["xMotor", 90], 'F': ["xMotor", 70], 'G': ["xMotor", 50], 'H': ["xMotor", 30],
                     'I': ["xMotor", 10], 'J': ["yMotor", 170], 'K': ["yMotor", 150], 'L': ["yMotor", 130],
                     'M': ["yMotor", 110], 'N': ["yMotor", 90], 'O': ["yMotor", 70], 'P': ["yMotor", 50],
                     'Q': ["yMotor", 30], 'R': ["yMotor", 10], 'S': ["zMotor", 170], 'T': ["zMotor", 150],
                     'U': ["zMotor", 130], 'V': ["zMotor", 110], 'W': ["zMotor", 90], 'X': ["zMotor", 70],
                     'Y': ["zMotor", 50], 'Z': ["zMotor", 30], '0': ["zMotor", 10], '1': ["dMotor", 170],
                     '2': ["dMotor", 150], '3': ["dMotor", 130], '4': ["dMotor", 110], '5': ["dMotor", 90],
                     '6': ["dMotor", 70], '7': ["dMotor", 50], '8': ["dMotor", 30], '9': ["dMotor", 10]}
buzzer_sound = []
buzzer_wait = []
code_lst = []
text_lst = []
code = ''

controller.start()

xMotor.threadTurnTo(xMotor.homePos, 5)
yMotor.threadTurnTo(yMotor.homePos, 5)
zMotor.threadTurnTo(zMotor.homePos, 5)
dMotor.threadTurnTo(dMotor.homePos, 5)


def input_morse():
    global code
    global buzzer_sound
    global buzzer_wait
    while True:
        butt = button_morse.detect()
        butt_space = button_space.detect()
        butt_del = button_delete.detect()

        if butt:  # Counts when button is pressed
            start_time = time.time()
            while button_morse.detect():
                pass
            elapsed_time = time.time() - start_time
            if elapsed_time <= 0.5:
                code += '.'
                buzzer.turnOn()
                led.turnOn()
                time.sleep(0.2)
                buzzer.turnOff()
                led.turnOff()

            else:  # Long press
                code += '-'
                buzzer.turnOn()
                led.turnOn()
                time.sleep(0.5)
                buzzer.turnOff()
                led.turnOff()

        if butt_space:  # When the button is pressed
            start_time = time.time()
            while button_space.detect():  # Wait for the button to be released
                pass
            elapsed_time = time.time() - start_time
            if elapsed_time <= 0.5:  # Short press
                code += ' '

            else:  # Long press
                code += ' ㅤ '

        if butt_del:
            code = code[:-1]
            time.sleep(0.1)

        sys.stdout.write(f"\rMorse Code: {code}")
        sys.stdout.flush()
        time.sleep(0.16)

        if button_trans.detect():
            break


def text_to_morse(text):
    morse_code = ''
    for char in text:
        if char.upper() in alphabet:
            position = alphabet.index(char.upper())
            morse_code += morse_code_mapping[position] + ' '
        else:
            morse_code += char
    return morse_code


def morse_to_text(morse_code):
    text = ''
    morse_code = morse_code.split(' ')
    if morse_code[-1] == '':
        morse_code = morse_code[:-1]
    for code in morse_code:
        if code in morse_code_mapping:
            morse_index = morse_code_mapping.index(code)
            text += alphabet[morse_index]
        else:
            text = '\nSorry you did not enter morse code.'
    return text


print(f"\n{'*' * 50}\n*{'Morse Code Translator':^48}{'*':>}\n{'*' * 50}\n\nMorse Button ----------- Morse Code to "
      f"text\nSpace Button ----------- Text to Morse Code\n\n{'*' * 50}\n")

while True:
    if button_morse.detect():

        time.sleep(0.5)
        input_morse()
        morse_code = code
        decoded_text = morse_to_text(morse_code)
        print(f"\nDecoded Text: {decoded_text}\n")

        if decoded_text != '\nSorry you did not enter morse code.':
            code_lst.append(code)
            code_lst = code.split(" ")
            for char in morse_code:
                text_lst.append(char)

            for i in text_lst:
                if i == '.':
                    buzzer_sound.append(0.2)
                elif i == '-':
                    buzzer_sound.append(0.5)
            code_lst.append(morse_code)
            code_lst = morse_code.split(" ")
            for i in range(len(code_lst)):

                for g in range(len(code_lst[i]) - 1):
                    buzzer_wait.append(0.1)
                buzzer_wait.append(0.25)

            for i in range(len(buzzer_sound)):
                buzzer.turnOn()
                led.turnOn()
                time.sleep(buzzer_sound[i])
                buzzer.turnOff()
                led.turnOff()
                time.sleep(buzzer_wait[i])

            for i in range(len(decoded_text)):
                if decoded_text[i] == ' ':
                    time.sleep(0.25)
                    print(decoded_text[i])

                elif decoded_text[i] == 'ㅤ':
                    continue

                elif decoded_text[i] in motor_alpha_angle:
                    if motor_alpha_angle[decoded_text[i]][0] == 'xMotor':
                        xMotor.turnTo(motor_alpha_angle[decoded_text[i]][1], 5)
                        time.sleep(1)
                        xMotor.turnTo(xMotor.homePos, 5)
                    elif motor_alpha_angle[decoded_text[i]][0] == 'yMotor':
                        yMotor.turnTo(motor_alpha_angle[decoded_text[i]][1], 5)
                        time.sleep(1)
                        yMotor.turnTo(yMotor.homePos, 5)
                    elif motor_alpha_angle[decoded_text[i]][0] == 'zMotor':
                        zMotor.turnTo(motor_alpha_angle[decoded_text[i]][1], 5)
                        time.sleep(1)
                        zMotor.turnTo(zMotor.homePos, 5)
                    elif motor_alpha_angle[decoded_text[i]][0] == 'dMotor':
                        dMotor.turnTo(motor_alpha_angle[decoded_text[i]][1], 5)
                        time.sleep(1)
                        dMotor.turnTo(dMotor.homePos, 5)
                    else:
                        continue
        print("\nThank you for using my Morse Code Translator.\n")
        break

    elif button_space.detect():
        code = input("Input text: ")
        morse_code = text_to_morse(code)
        print("Morse Code:", morse_code)

        for char in morse_code:
            text_lst.append(char)

        for i in text_lst:
            if i == '.':
                buzzer_sound.append(0.2)
            elif i == '-':
                buzzer_sound.append(0.5)

        code_lst.append(morse_code)
        code_lst = morse_code.split(" ")
        for i in range(len(code_lst)):

            for g in range(len(code_lst[i])-1):
                buzzer_wait.append(0.1)
            buzzer_wait.append(0.25)

        for i in range(len(buzzer_sound)):
            buzzer.turnOn()
            led.turnOn()
            time.sleep(buzzer_sound[i])
            buzzer.turnOff()
            led.turnOff()
            time.sleep(buzzer_wait[i])

        print("\nThank you for using my Morse Code Translator.\n")
        break
controller.shutdown()