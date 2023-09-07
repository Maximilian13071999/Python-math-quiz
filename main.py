import json
import random

player_data = {
    "scores": 0,
    "correct": 0
}

class Question:
    def __init__(self, text, difficulty, answer):
        self.text = text
        self.difficulty = difficulty
        self.answer = answer.lower()
        self.is_used = False
    def get_points(self):
        return self.difficulty * 10
    def is_correct(self, user_answer):
        return self.answer == user_answer.lower()
    def build_question(self):
        print(f"Вопрос: {self.text}")
        print(f"Сложность: {self.difficulty}/5")
    def build_positive_feedback(self):
        player_data["scores"] += self.get_points()
        player_data["correct"] += 1
        print(f"Ответ верный. Получено {self.get_points()} баллов.\n")
    def build_negative_feedback(self):
        print(f"Ответ неверный, верный ответ {self.answer}.\n")

def get_stats(number_of_questions):
    correct = player_data["correct"]
    scores = player_data["scores"]
    print("Вот и всё!")
    print(f"Отвечено {correct} из {number_of_questions - correct}")
    print(f"Набрано баллов: {scores}")

def load_data():
    questions = []
    with open("questions.txt", encoding="utf-8") as json_file:
        data = json.load(json_file)
    for item in data:
        quest = Question(item["question"], int(item["difficulty"]), item["answer"])
        questions.append(quest)
    questions = random.sample(questions, len(questions))
    return questions

def game():
    questions = load_data()
    for question in questions:
        question.build_question()
        if question.is_correct(input()):
            question.build_positive_feedback()
        else:
            question.build_negative_feedback()
    get_stats(len(questions))

game()



