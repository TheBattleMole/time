import tkinter as tk

def tren():
    num1 = int(number1_entry.get())
    if tren.get() =="":
        num2 = 0
    else:
        num2 = int(tren_m.get())
    if tren.get() =="":
        num3 = 0
    else:
        num3 = int(tren.get())
    res = num1 + num2 +num3*60
    tren.delete(0, 'end')
    tren_m.delete(0, "end")
    number1_entry.delete(0, 'end')
    hours = res // 60
    minutes = res % 60
    tren.insert(0, hours)
    tren_m.insert(0, minutes)


def kontr():
    num1 = int(number1_entry.get())
    if kontr.get() =="":
        num2 = 0
    else:
        num2 = int(kontr_m.get())
    if kontr.get() =="":
        num3 = 0
    else:
        num3 = int(kontr.get())
    res = num1 + num2 +num3*60
    kontr.delete(0, 'end')
    kontr_m.delete(0, "end")
    number1_entry.delete(0, 'end')
    hours = res // 60
    minutes = res % 60
    kontr.insert(0, hours)
    kontr_m.insert(0, minutes)


def instr():
    num1 = int(number1_entry.get())
    if instr.get() =="":
        num2 = 0
    else:
        num2 = int(instr_m.get())
    if instr.get() =="":
        num3 = 0
    else:
        num3 = int(instr.get())
    res = num1 + num2 +num3*60
    instr.delete(0, 'end')
    instr_m.delete(0, "end")
    number1_entry.delete(0, 'end')
    hours = res // 60
    minutes = res % 60
    instr.insert(0, hours)
    instr_m.insert(0, minutes)


def v_sostave():
    num1 = int(number1_entry.get())
    if v_sostave.get() == "":
        num2 = 0
    else:
        num2 = int(v_sostave_m.get())
    if v_sostave.get() == "":
        num3 = 0
    else:
        num3 = int(v_sostave.get())
    res = num1 + num2 + num3 * 60
    v_sostave.delete(0, 'end')
    v_sostave_m.delete(0, "end")
    number1_entry.delete(0, 'end')
    hours = res // 60
    minutes = res % 60
    v_sostave.insert(0, hours)
    v_sostave_m.insert(0, minutes)


def itog():
    if tren.get() == "":
        tren1 = 0
    else:
        tren1 = int(tren.get())
    if tren_m.get() == "":
        tren2 = 0
    else:
        tren2 = int(tren_m.get())
    if kontr.get() == "":
        kontr1 = 0
    else:
        kontr1 = int(kontr.get())
    if kontr_m.get() == "":
        kontr2 = 0
    else:
        kontr2 = int(kontr_m.get())
    if instr.get() == "":
        instr1 = 0
    else:
        instr1 = int(instr.get())
    if instr_m.get() == "":
        instr2 = 0
    else:
        instr2 = int(instr_m.get())
    if v_sostave.get() == "":
        v_sostave1 = 0
    else:
        v_sostave1 = int(v_sostave.get())
    if v_sostave_m.get() == "":
        v_sostave2 = 0
    else:
        v_sostave2 = int(v_sostave_m.get())
    res = tren1*60 + tren2 + kontr1*60 + kontr2 + instr1*60 + instr2 + v_sostave1*60 + v_sostave2
    itog.delete(0, 'end')
    itog_m.delete(0, "end")
    hours = res // 60
    minutes = res % 60
    itog.insert(0, hours)
    itog_m.insert(0, minutes)



window = tk.Tk()
window.title("Калькулятор")
window.geometry("350x350")
window.resizable(False, False)

button_tren = tk.Button(window, bg="red", width=3, height=2, command = tren)
button_tren.place(x=100, y=75)
button_kontr = tk.Button(window, bg="blue", width=3, height=2, command = kontr)
button_kontr.place(x=140, y=75)
button_mul = tk.Button(window, bg="green", width=3, height=2, command = instr)
button_mul.place(x=180, y=75)
button_div = tk.Button(window, bg="grey", width=3, height=2, command = v_sostave)
button_div.place(x=220, y=75)

number1_entry = tk.Entry(window, width=24)
number1_entry.place(x=100, y=50)
tren = tk.Entry(window, width=4)
tren.place(x=150, y=175)
tren_m = tk.Entry(window, width=7)
tren_m.place(x=200, y=175)
kontr = tk.Entry(window, width=4)
kontr.place(x=150, y=200)
kontr_m = tk.Entry(window, width=7)
kontr_m.place(x=200, y=200)
instr = tk.Entry(window, width=4)
instr.place(x=150, y=225)
instr_m = tk.Entry(window, width=7)
instr_m.place(x=200, y=225)
v_sostave = tk.Entry(window, width=4)
v_sostave.place(x=150, y=250)
v_sostave_m = tk.Entry(window, width=7)
v_sostave_m.place(x=200, y=250)
itog = tk.Entry(window, width=4)
itog.place(x=150, y=300)
itog_m = tk.Entry(window, width=7)
itog_m.place(x=200, y=300)

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
h_m = tk.Label(window, text = "ч.")
h_m.place(x=175, y=175)
h_m1 = tk.Label(window, text = "ч.")
h_m1.place(x=175, y=200)
h_m2 = tk.Label(window, text = "ч.")
h_m2.place(x=175, y=225)
h_m3 = tk.Label(window, text = "ч.")
h_m3.place(x=175, y=250)
h_m4 = tk.Label(window, text = "мин.")
h_m4.place(x=250, y=175)
h_m5 = tk.Label(window, text = "мин.")
h_m5.place(x=250, y=200)
h_m6 = tk.Label(window, text = "мин.")
h_m6.place(x=250, y=225)
h_m7 = tk.Label(window, text = "мин.")
h_m7.place(x=250, y=250)
h_m8 = tk.Label(window, text = "ч.")
h_m8.place(x=175, y=300)
h_m9 = tk.Label(window, text = "мин.")
h_m9.place(x=250, y=300)
window.mainloop()