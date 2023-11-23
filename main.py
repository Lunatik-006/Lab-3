import tkinter as tk
from tkinter import messagebox
from keygen import keyGeneration


def close():
    window.destroy()


def generate():
    number=argument.get()
    if number[0] == '0':
        tk.messagebox.showwarning('Error', 'A number cannot start from zero!')
    elif len(number)!=6:
        tk.messagebox.showwarning('Error', 'A number must be SIX-DIGIT!')
    else:
        lbl_result.configure(text=keyGeneration(number))


window = tk.Tk()
window.geometry('576x384')
bg_img = tk.PhotoImage(file='forzapic1.png')

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame1 = tk.Frame(window)
frame1.place(relx=0.5, rely=0.33, anchor='s')

lbl_input = tk.Label(frame1, text='Enter a six-digit number:')
lbl_input.grid(column=1,row=0, padx=10, pady=5)

argument = tk.Entry(frame1, width=10,justify='center')
argument.focus()
argument.grid(column=1, row=1, padx=10, pady=10)

btn_gen = tk.Button(frame1, text='Generate', command=generate)
btn_gen.grid(column=1, row=2, sticky='e', padx=10, pady=10)
btn_exit = tk.Button(frame1, text='Cancel', command=close)
btn_exit.grid(column=1, row=2, sticky='w', padx=10, pady=10)

frame2 = tk.Frame(window)
frame2.place(relx=0.5, rely=0.85, anchor='n')

lbl_key = tk.Label(frame2, text='Your key is:', font=('Arial', 10))
lbl_key.grid(column=1, row=2)
lbl_result = tk.Label(frame2, text='None yet.', font=('Arial', 10))
lbl_result.grid(column=2, row=2)
window.mainloop()