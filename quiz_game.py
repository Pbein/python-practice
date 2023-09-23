class Question:
    def __init__ (self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions_prompts = [
        "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n",
        "What color are bannanas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n",
]

questions = [
        Question(questions_prompts[0], "a"),
        Question(questions_prompts[1], "c"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} correct.")

run_quiz(questions)
