import tkinter

main_window = tkinter.Tk()
main_window.title('Calculator')
main_window.geometry('250x400+600+200')
main_window['padx'] = 25

buttons_frame = tkinter.Frame(main_window)
buttons_frame.grid(row=1, column=0, columnspan=2)
buttons_frame.config(borderwidth=2, relief='sunken')


z = 1
for i in range(1,4):
    for x in range(1,4):
        tkinter.Button(buttons_frame, text=z).grid(row=5 - i, column=x-1, sticky='ew')
        z += 1

tkinter.Button(buttons_frame, text=0).grid(row=5, column=0)
tkinter.Button(buttons_frame, text='=').grid(row=5, column=1, columnspan=2, sticky='ew')
tkinter.Button(buttons_frame, text='CE').grid(row=1, column=1, sticky='ew')
tkinter.Button(buttons_frame, text='C').grid(row=1, column=0, sticky='ew')

z = 2
for l in ('+', '-', '*', '/'):
    tkinter.Button(buttons_frame, text=l).grid(row=z, column=3, sticky='ew')
    z += 1

tkinter.Entry(buttons_frame).grid(row=0, column=0, columnspan=4)

main_window.mainloop()