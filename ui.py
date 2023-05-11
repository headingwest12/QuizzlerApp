from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # canvas
        self.canvas = Canvas(width=300, height=250, bg="White")
        self.question_text = self.canvas.create_text(150, 125, text=f"Question", font=("Ariel", 20, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # buttons
        right_image = PhotoImage(file="./images/true.png")
        wrong_image = PhotoImage(file="./images/false.png")
        self.right_button = Button(image=right_image, bg=THEME_COLOR, highlightthickness=0, command=self.return_true)
        self.right_button.grid(row=2, column=0)
        self.false_button = Button(image=wrong_image, bg=THEME_COLOR, highlightthickness=0, command=self.return_false)
        self.false_button.grid(row=2, column=1)
        # label
        self.score_label = Label(text=f"Sore: {self.quiz.score}", bg=THEME_COLOR, fg="White")
        self.score_label.grid(row=0, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")

        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of quiz")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def return_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def return_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)

