import requests
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x400")
window.title("Chuck Norris Jokes")
window['bg'] = "lightblue"


def get_chucks_jokes():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        data = response.json()
        messagebox.showinfo("Chuck Norris Jokes", data["value"])
    except requests.exceptions.ConnectionError as x:
        messagebox.showerror("Error", "Lost connection")


btn = Button(window, text="Get Jokes", command=get_chucks_jokes, borderwidth=5, bg="violet")
btn.place(x=150, y=150)


window.mainloop()
