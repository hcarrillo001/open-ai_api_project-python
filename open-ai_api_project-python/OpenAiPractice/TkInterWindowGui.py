import tkinter as tk
import openai

#key will be score in a file names my_secretkey.py
from sk import my_sk


class TkinterWindowGui:

    def __init__(self):

        self.userinput = ""
        self.chatgptresponse = ""
        self.root = tk.Tk()

        self.root.geometry("800x500")
        self.root.title("ChatGPT Practice")

        self.label = tk.Label(self.root,text="GPT Practice", font=('Arial', 18))
        self.label.pack(padx=10,pady=10)

        self.userinputlabel = tk.Label(self.root, text="Ask ChatGPT Anything Below and Click Enter", font=('Arial', 15))
        self.userinputlabel.pack(padx=10, pady=20)

        self.entry = tk.Entry(self.root,width=100,font=('Arial',18))
        self.entry.pack(padx=10,pady=10)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)

        self.button1 = tk.Button(self.buttonframe, text="Enter", font=('Arial', 18), command=self.enter_button_press)
        self.button1.grid(row=0, column=0, sticky=tk.W + tk.E)
        self.button2 = tk.Button(self.buttonframe, text="Clear", font=('Arial', 18), command=self.clear_button_press)
        self.button2.grid(row=0, column=1, sticky=tk.W + tk.E)
        self.buttonframe.pack()


        #text box to display the chatGPT answer
        self.answerlabel = tk.Label(self.root,text="GPT Answer", font=('Arial', 15))
        self.answerlabel.pack(padx=10,pady=20)
        self.answertextbox = tk.Text(self.root,height=90,width=90,font=('Arial',18))
        self.answertextbox.pack(padx=10,pady=10)


        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        print("hello world")

    def enter_button_press(self):
        self.userinput = self.entry.get()
        print(self.userinput)

        # import key from file or you can just copy and past it here as a string
        openai.api_key = my_sk

        # chat completion
        # https://platform.openai.com/docs/guides/text?api-mode=responses

        # role is the user
        # content is the prompt you are sending to chatgpt
        #other models gpt-4o or gpt-3.5-turbo
        chat_completion = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": self.userinput}])

        #Add user input then ansser
        self.response = "\n" + self.userinput + "\n\n" + chat_completion.choices[0].message.content + "\n"
        self.answertextbox.insert("1.0",self.response)

        print(self.response)

    def clear_button_press(self):
        self.entry.delete(0,tk.END)

    def on_closing(self):
        self.root.destroy()

TkinterWindowGui()
