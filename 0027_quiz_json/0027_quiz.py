import json

points = 0

def show_question(question):
    print("\n"+question["pytanie"])
    print("a:", question["A"])
    print("b:", question["B"])
    print("c:", question["C"])
    print("d:", question["D"])
    print()

    answer = input("Którą odpowiedź wybierasz?")

with open("quiz.json") as json_file:
    questions = json.load(json_file)

    for i in range(0, len(questions)):
        print(show_question[i])