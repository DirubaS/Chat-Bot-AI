"""pip install tkinkter"""
import tkinter as tk
from tkinter import scrolledtext


def send_message():
    user_input = entry.get().lower()
    conversation.insert(tk.END, f"\nYou: {user_input}\n")

    # Chatbot responses
    if "hello" in user_input or "hi" in user_input:
        bot_response = "Bot: Hello! How can I help you today?"

    elif "help" in user_input:
        bot_response = (
            "Bot: Sure, I'm here to assist you. What do you need help with?\n"
            "Here are the list of commands that you can use: [create account], [balance], [view balance]"
        )

    elif "create account" in user_input:
        bot_response = "Bot: Great! Let's start the account creation process. Please provide the necessary details."

    elif "balance" in user_input or "view balance" in user_input:
        bot_response = "Bot: Sure, let me check your account balance for you."

    else:
        bot_response = (
            "Bot: I'm sorry, I didn't quite catch that. How can I assist you?"
        )

    conversation.insert(tk.END, f"{bot_response}\n")
    entry.delete(0, tk.END)


# Tkinter setup
root = tk.Tk()
root.title("Diruba's ChatBot")

# Chat history display
conversation = scrolledtext.ScrolledText(root, width=50, height=20, wrap=tk.WORD)
conversation.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# User input entry
entry = tk.Entry(root, width=50)
entry.grid(row=1, column=0, padx=10, pady=10)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Run the Tkinter main loop
root.mainloop()
