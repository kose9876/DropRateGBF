import tkinter as tk
from frame.frame1 import Frame1
from frame.frame2 import Frame2


window = tk.Tk()
window.title('機神系列沙漏武器掉落率統計機')
window.geometry('720x800')
window.resizable(False, False)

frame1 = Frame1(window)
frame1.grid(row=0,column=1)
frame1.load_counts('counts.txt')
frame1.save_counts('counts.txt')
frame2 = Frame2(window)
frame2.grid(row=0,column=2)
frame2.load_counts('counts2.txt')
frame2.save_counts('counts2.txt')


window.mainloop()
