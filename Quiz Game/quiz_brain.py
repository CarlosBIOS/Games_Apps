class QuizBrain:

    def __init__(self, question: list):
        self.question = question
        self.score = 0

    def __str__(self):
        return 'Vai analisar a resposta do usuário'

    def quiz(self):
        for index, question_object in enumerate(self.question):
            answer: str = (input(f'Q.{index + 1}: {question_object.text.replace('.', '?')}: (True/False)').title().
                           strip())

            if answer == question_object.answer:
                print('Muito bem, acertaste!')
                self.score += 1
            else:
                print(f'Sorry, its {question_object.answer}!')

            print(f'Your score: {self.score}\n')
