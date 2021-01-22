import re

# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code

# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"
    return message

def is_help_command(user_input):

    if user_input.isalpha() and user_input.upper() in ['HELP', 'H']:
        return True
    else:
        return False
#========================= 인코딩 파트 ========================================
def is_validated_english_sentence(user_input): #영문장이 유효한 문장인지 체크
    result = False
    only_eng = "".join(re.findall('[A-Za-z.,!?]', user_input))
    if only_eng == user_input.strip().replace(" ",""):
        if re.sub('[.,!?]','',only_eng) != "": #check empty str
            result = True

    return result

def get_cleaned_english_sentence(raw_english_sentence):#유효한 영문장을 대상으로 전처리

    if re.findall('[.,!?]', raw_english_sentence):
        raw_english_sentence = re.sub('[.,!?]', '', raw_english_sentence).strip()

    else:
        raw_english_sentence = raw_english_sentence.strip()
    
    return raw_english_sentence


def encoding_character(english_character):
    """
    Input:
        - english_character : 문자열값으로 알파벳 한 글자의 입력이 보장됨
    Output:
        - get_morse_code_dict 함수의 반환 값으로 인해 변환된 모스부호 문자열값
    """
    morse_code_dict = get_morse_code_dict()
    return morse_code_dict.get(english_character)


def encoding_sentence(english_sentence):
    morse = get_cleaned_english_sentence(english_sentence).upper()
    morse = list(morse)

    result = ''
    for i in range(0, len(morse)):
        if morse[i] == ' ' and morse[i+1] == ' ':
            pass
        elif morse[i] == ' ' and morse[i+1] != ' ':
            result += ' '
        else:
            result += str(encoding_character(morse[i]))
            result += ' '
    
    result = result.strip()
    return result

#========================== 인코딩 파트 ========================================

#========================== 디코딩 파트 ========================================
def is_validated_morse_code(user_input):

    codes = user_input.split()
    reverse_code_dict = dict(map(reversed, get_morse_code_dict().items()))

    for code in codes:
        if reverse_code_dict.get(code):
            pass
        else:
            return False

    return True
def decoding_character(morse_character):
    # 기존 딕셔너리의 key와 value를 reverse 시켜서 값을 빼온다.
    reverse_code_dict = dict(map(reversed, get_morse_code_dict().items()))
    return reverse_code_dict.get(morse_character)

def decoding_sentence(morse_sentence):
    morse = morse_sentence
    morse = morse.split(' ')
    
    result = ''
    for i in range(len(morse)):
        if morse[i] == '':
            result += ' '
        else:
            result += str(decoding_character(morse[i]))

    return result
#========================== 디코딩 파트 ========================================
decoding_sentence("--. --.  --. -  -  -  - . . . .")
def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    flag = True
    while flag:
        user_input = input("Input your message(H- Help, 0- Exit): ")

        if user_input == '0':
            break
        elif is_help_command(user_input):
            message = get_help_message()
            print(message)
        elif is_validated_english_sentence(user_input):
            result = encoding_sentence(user_input)
            print(result)
        elif is_validated_morse_code(user_input):
            result = decoding_sentence(user_input)
            print(result)
        elif user_input == ' ':
            print("Wrong Input")
        else:
            print("Wrong Input")
    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")