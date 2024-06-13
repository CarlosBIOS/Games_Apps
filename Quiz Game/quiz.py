from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def question_bank(data: list):
    question_list: list = []
    for question in data:
        question_list.append(Question(question['text'], question['answer']))

    return question_list


def main():
    question_list: list = question_bank(question_data)
    print('Welcome to the Quiz!')
    QuizBrain(question_list).quiz()

    print('Acabou o quiz:)')


if __name__ == '__main__':
    main()
