# Ceaser Cipher
# Esta codificação foi usada no busted e basicamente a letra avanca n casas. Por exemplo, Carlos -> Fduosv
# (andou 3 casas)

def encode_or_decode(word: str) -> str:
    while True:
        if word in ('encode', 'decode'):
            return word
        word: str = input('Please write encode or decode: ').casefold().strip()


def is_word(texto: str) -> str:
    while True:
        if texto.isalpha():
            return texto
        texto: str = input('Please write a word or a sentece: ').casefold().strip()


def is_number(number: str) -> int:
    while True:
        if number.isdecimal() and int(number) >= 0:
            return int(number) - 26 * (int(number) // 27)

        number: str = input('Please choose a correct number: ')


def yes_or_no(resposta: str) -> str:
    """Gets a `yes` or `no` answer from the user in a case-insensitive loop."""
    while True:
        if resposta in ('yes', 'no'):
            return resposta
        resposta: str = input("Please write 'yes' or 'no': ").casefold().strip()


def caesar_cipher(direcao: str, sentence: str, salto: int) -> str:
    """
    Performs Caesar cipher encryption or decryption on the provided text.
    :param direcao: `encode` or `decode` to specify the operation.
    :param sentence: The text to `encrypt` or `decrypt`.
    :param salto:  The number of positions to `salto` the letters.
    :return:
        The encrypted or decrypted text.
    """
    new_words: str = ''

    for letter in sentence:
        if direcao == 'encode':
            new_words += (alphabet * 2)[alphabet.index(letter) + salto]

        else:
            new_words += (alphabet * 2)[alphabet.index(letter) - salto]

    return new_words


if __name__ == '__main__':

    alphabet: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y', 'z']

    logo: str = """           
     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                88             88                                 
               ""             88                                 
                              88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                  88                                             
                  88           
    """
    answer = ''

    print(logo)

    while answer != 'no':
        direction: str = encode_or_decode(input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
                                          .casefold().strip())
        text: str = is_word(input("Type your message:\n").casefold().strip())
        shift: int = is_number(input("Type the shift number:\n"))

        new_word: str = caesar_cipher(direction, text, shift)

        print(f"Here's the decoded result: {new_word}")

        answer: str = yes_or_no(input("Type 'yes' if you want to go again. Otherwise type 'no': ").casefold().strip())

    else:
        print('\nGoodbye!!')
