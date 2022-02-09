from tkinter import *
from tkinter import ttk

global saisiestart, saisieend, saisiestop
saisiestart.delete(0, END)
saisieend.delete(0, END)
saisiestop.delete(0, END)
root = Tk()
start = ttk.Frame(root, padding=5)
end = ttk.Frame(root, padding=10)
stop = ttk.Frame(root, padding=15)
start.grid()
end.grid()
stop.grid()
ttk.Label(start, text="Entrez heure de début").grid(column=1, row=1)
ttk.Label(end, text="Entrez heure de fin").grid(column=3, row=1)
ttk.Label(stop, text="Entrez temps de pause (en minutes)").grid(column=5, row=1)
saisiestart = Entry(start, bd=3)
saisieend = Entry(end, bd=3)
saisiestop = Entry(stop, bd=3)
saisiestart.get()
saisiestart.insert(0, s1)

saisieend.get()
saisieend.insert(0, s2)

saisiestop.get()
saisiestop.insert(0, s3)


quit = ttk.Frame(root, padding=5)
quit.grid()
ttk.Button(quit, text="Quitter", command=root.destroy).grid(column=10, row=10)
root.mainloop()
