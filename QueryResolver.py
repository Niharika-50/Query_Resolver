import openai
import tkinter as tk

api_key="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"
openai.api_key = api_key

window = tk.Tk()
window.title("QUERY RESOLVER")

conversation_text = tk.Text(window, height=30, width=120)
conversation_text.pack()

user_input= tk.Entry(window, width=90)
user_input.pack()

def send_message():
    user_message = user_input.get()
    conversation_text.insert(tk.END, "You: " + user_message + "\n")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=conversation_text.get("1.0",tk.END),
        max_tokens=400

    )
    bot_reply = response.choices[0].text
    conversation_text.insert(tk.END, "QUERY RESOLVER: "+bot_reply+ "\n")
    user_input.delete(0, tk.END)

send_button = tk.Button(window, text = "send" , command = send_message)
send_button.pack()

window.mainloop()