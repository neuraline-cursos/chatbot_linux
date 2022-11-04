from Neuraline.ObjectiveAI.chatbot import Chatbot
from tkinter import *
from tkinter import ttk
from threading import Thread
chatbot = Chatbot()
chatbot.loadModel("model")
title, answer = "Chatbot", ""
try:
	temp = str(chatbot.title_name).strip()
	if len(temp) > 0: title = temp
except: pass
try: 
	inputs_name = chatbot.inputs_name
	if len(inputs_name) <= 0: inputs_name = [""]
except: inputs_name = [""]
def talk(phrase="", result=False):
	try:
		global answer
		if result: individual, line = "BOT", "\n\n"
		else: individual, line = "YOU", "\n"
		answer += f"[{individual}]: {phrase}"+line
		txt_result.config(state=NORMAL)
		txt_result.delete(1.0, END)
		txt_result.insert(INSERT, str(answer))
		txt_result.see(END)
		txt_result.config(state=DISABLED)
		txt_question.delete(0, END)
		lbl_title.config(text=title)
		txt_question.focus()
		if not result: return phrase
	except: error()
def predict():
	def _loading():
		lbl_title.config(text="loading...")
		btn_predict.focus()
	def _predict():
		question = talk(str(txt_question.get()).strip())
		result = chatbot.conversation(external_user_id=1, question=question)
		print(f"RESULT: {result}")
		talk(str(result[0]["answer"]).strip(), True)
	try: Thread(target=_loading).start(), Thread(target=_predict).start()
	except: error()
def error():
	try:
		txt_result.config(state=NORMAL)
		txt_result.delete(1.0, END)
		txt_result.insert(INSERT, "")
		txt_result.config(state=DISABLED)
		lbl_title.config(text=title)
		btn_predict.focus()
	except: pass
def clear():
	try:
		global answer
		answer = ""
		txt_question.delete(0, END)
		txt_result.config(state=NORMAL)
		txt_result.delete(1.0, END)
		txt_result.insert(INSERT, "")
		txt_result.config(state=DISABLED)
		txt_question.focus()
	except: pass
window = Tk()
window.title(f"Neuraline - {title}")
window.configure(bg="white")
lbl_title = Label(window, text=title, bg="white", font="Helvetica 8 bold", relief=FLAT)
lbl_title.place(x=50, y=5)
txt_result = Text(window, width=68, height=18, relief=RIDGE)
txt_result.place(x=50, y=30)
txt_result.config(state=DISABLED)
txt_question = Entry(window, width=51, relief=RIDGE)
txt_question.place(x=50, y=330)
txt_question.insert(0, str(inputs_name[0]).strip())
txt_question.focus_set()
btn_predict = Button(window, width=5, text="Send", command=predict, bg="#007BFF", fg="white", relief=GROOVE)
btn_predict.place(x=465, y=330)
btn_clear = Button(window, width=5, text="Clear", command=clear, bg="white", fg="#212529", relief=GROOVE)
btn_clear.place(x=533, y=330)
width, height = 650, 400
window.geometry(f"{width}x{height}+100+100")
window.resizable(0, 0)
window.mainloop()
