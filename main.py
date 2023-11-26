import winsound
from tkinter import messagebox, Tk, PhotoImage, Canvas, Frame, Entry, Button, Label
from keygen import KeyGeneration


# Закрыть окно программы
def close():
    window.destroy()


# Обработать возможные исключения и при их отсутствии сгенерировать ключ
def generate():
    number = argument.get()
    try:
        int(number)
        if number[0] == "0":
            messagebox.showwarning("Error", "A number cannot start from zero!")
        elif len(number) != 6:
            messagebox.showwarning("Error", "A number must be SIX-DIGIT!")
        else:
            lbl_result.configure(text=KeyGeneration(number))
    except ValueError:
        messagebox.showwarning("Error", "Please enter a NUMBER!")


# Смена фоновых изображений
def animate_frame(frame=0):
    bg_img.create_image(0, 0, image=bg_img_list[frame], anchor="nw")
    window.after(10000, animate_frame, (frame + 1) % len(bg_img_list))


# Создать окно
window = Tk()
window.geometry("576x384")
window.title("Key generator")

# Создать список имен файлов фоновых изображений и разместить фоновое изображение
bg_img_list = [PhotoImage(file=f"{i+1}.png") for i in range(4)]
bg_img = Canvas(window, width=576, height=384)
bg_img.pack()

# Создать виджет с полем для ввода и кнопками
frame1 = Frame(window)
frame1.place(relx=0.5, rely=0.33, anchor="s")

lbl_input = Label(frame1, text="Enter a six-digit number:")
lbl_input.grid(column=1, row=0, padx=10, pady=5)

argument = Entry(frame1, width=10, justify="center")
argument.focus()
argument.grid(column=1, row=1, padx=10, pady=10)

btn_gen = Button(frame1, text="Generate", command=generate)
btn_gen.grid(column=1, row=2, sticky="e", padx=10, pady=10)
btn_exit = Button(frame1, text="Cancel", command=close)
btn_exit.grid(column=1, row=2, sticky="w", padx=10, pady=10)

# Создать виджет для вывода результата
frame2 = Frame(window)
frame2.place(relx=0.5, rely=0.85, anchor="n")

lbl_key = Label(frame2, text="Your key is:", font=("Arial", 10))
lbl_key.grid(column=1, row=2)
lbl_result = Label(frame2, text="Not generated yet.", font=("Arial", 10))
lbl_result.grid(column=2, row=2)

# Включить проигрывание фоновой мелодии
winsound.PlaySound(
    "forzatheme.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP
)

# Запустить анимацию фоновых изображений
animate_frame()

window.mainloop()
