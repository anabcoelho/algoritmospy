from tkinter import *
import random

janela = Tk()
bt = []
m = []
x = [22, 22, 20, 0, 0, "n"]  # x,y,c,bombas,spc,lose


def bomba(i, g):
    lucas = bt[x[1] * i + g]
    if lucas["bg"] != "#DCDCDC" and x[5] == "n":
        if lucas["bg"] != "#ff0000":
            lucas["bg"] = "#ff0000"
            x[3] -= 1

            r["text"] = "Bombas: " + str(x[3])
        else:
            lucas["bg"] = "#000000"
            x[3] += 1
            r["text"] = "Bombas: " + str(x[3])


def clicou(i, g, c):
    c.append([i, g])
    ssss = 1
    st = []
    if m[i][g] == 1 and bt[i * x[1] + g]["bg"] != "#ff0000" and x[5] == "n":
        r["text"] = "Perdeu"
        x[5] = "s"
        for j in range(x[0]):
            for z in range(x[1]):
                if m[j][z] == 1:
                    bt[x[1] * j + z]["bg"] = "#ffffff"
    elif m[i][g] == 0 and bt[i * x[1] + g]["bg"] != "#ff0000" and bt[x[1] * i + g]["bg"] != "#DCDCDC" and x[5] == "n":
        b = 0
        for j in range(-1, 2):
            v = i + j
            for z in range(-1, 2):
                f = z + g
                if j != 0 or z != 0:
                    if v >= 0 and f >= 0 and v < len(m) and f < len(m[0]):
                        if m[v][f] == 1:
                            b += 1
        for j in range(-1, 2):
            v = i + j
            for z in range(-1, 2):
                f = z + g
                if j != 0 or z != 0:
                    if v >= 0 and f >= 0 and v < len(m) and f < len(m[0]):
                        if ((j == 0 and z == 1) or (j == 0 and z == -1) or (j == -1 and z == 0) or (
                                j == 1 and z == 0) and (m[i + j][g + z] == 0) or b == 0):
                            st = [v, f]
                            l = False
                            for k in range(len(c)):
                                if st == c[k]:
                                    l = True
                            if l == False and b == 0:
                                c.append(st)
                                clicou(v, f, c)
                            st = []

        bt[x[1] * i + g]["bg"] = "#DCDCDC"
        x[4] -= 1
        if b == 0: b = ""
        bt[x[1] * i + g]["text"] = b
        r["text"] = "Bombas: " + str(x[3])
        if x[4] <= 0 and x[5] == "n":
            r["text"] = "Ganhou!"
            x[5] = "s"
    return 0


for i in range(x[0]):
    m.append([])
    for g in range(x[1]):
        if random.randint(1, 100) <= x[2]:
            m[-1].append(1)
            x[3] += 1
        else:
            m[-1].append(0)
        bt.append(Button(janela, width="3", height="1"))
        bt[-1].grid(row=i, column=g + 1)
        bt[-1].bind('<Button-1>', lambda a=None, i=i, g=g: clicou(i, g, []))
        bt[-1].bind('<Button-3>', lambda a=None, i=i, g=g: bomba(i, g))
        bt[-1]["bg"] = "#000000"
x[4] = (x[0] * x[1]) - x[3]

r = Label(janela, text="Bombas: " + str(x[3]))
r.grid(row=x[0], column=0)
janela.mainloop()