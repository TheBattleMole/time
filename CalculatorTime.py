import tkinter as tk



def tren():
    num1 = int(number1_entry.get())
    if tren.get() =="":
        num2 = 0
    else:
        num2 = int(tren.get())
    res = num1 + num2
    tren.delete(0, 'end')
    number1_entry.delete(0, 'end')
    hours = res // 60
    minutes = res % 60
    tren.config(text = "gh")

# def kontr():
#     num1 = int(number1_entry.get())
#     if kontr.get() =="":
#         num2 = 0
#     else:
#         num2 = int(kontr.get())
#     res = num1 + num2
#     kontr.delete(0, 'end')
#     number1_entry.delete(0, 'end')
#     kontr.insert(0, res)




window = tk.Tk()
window.title("Калькулятор")
window.geometry("350x350")
window.resizable(False, False)

button_tren = tk.Button(window, bg="red", width=3, height=2, command = tren)
button_tren.place(x=100, y=75)
button_kontr = tk.Button(window, bg="blue", width=3, height=2)
button_kontr.place(x=140, y=75)
button_mul = tk.Button(window, bg="green", width=3, height=2)
button_mul.place(x=180, y=75)
button_div = tk.Button(window, bg="grey", width=3, height=2)
button_div.place(x=220, y=75)

number1_entry = tk.Entry(window, width=24)
number1_entry.place(x=100, y=50)
tren = tk.Entry(window, width=15)
tren.place(x=150, y=175)
kontr = tk.Entry(window, width=15)
kontr.place(x=150, y=200)
instr = tk.Entry(window, width=15)
instr.place(x=150, y=225)
v_sostave = tk.Entry(window, width=15)
v_sostave.place(x=150, y=250)

number1 = tk.Label(window, text = "Введите минуты:")
number1.place(x=100, y=25)
tren_entry = tk.Label(window, text = "Тренировочный:")
tren_entry.place(x=50, y=175)
kontr_entry = tk.Label(window, text = "Контрольный:")
kontr_entry.place(x=50, y=200)
instr_entry = tk.Label(window, text = "Инструкторский:")
instr_entry.place(x=50, y=225)
v_sostave_entry = tk.Label(window, text = "В сост. экипажа:")
v_sostave_entry.place(x=50, y=250)

window.mainloop()