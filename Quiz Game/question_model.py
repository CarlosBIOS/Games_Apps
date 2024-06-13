class Question:

    def __init__(self, text: str, answer: str):
        self.text: str = text
        self.answer: str = answer

    def __str__(self):
        return 'Cria um objeto, onde os atributos text and answer é respetivamente a pergunta e a solução'
