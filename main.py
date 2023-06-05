import tkinter as tk
from frame.frame1 import Frame1
from frame.frame2 import Frame2
from frame.frame3 import Frame3
from frame.frame4 import Frame4
from frame.frame5 import Frame5
from frame.frame6 import Frame6

window = tk.Tk()
window.title('機神系列沙漏武器掉落率統計機')
window.geometry('1000x730')
window.resizable(False, False)

frame1 = Frame1(window)
frame1.grid(row=0,column=1)
frame1.load_counts('counts.txt')
frame1.save_counts('counts.txt')

frame2 = Frame2(window)
frame2.grid(row=0,column=2)
frame2.load_counts('counts2.txt')
frame2.save_counts('counts2.txt')

frame3 = Frame3(window)
frame3.grid(row=0,column=3)
frame3.load_counts('counts3.txt')
frame3.save_counts('counts3.txt')

frame4 = Frame4(window)
frame4.grid(row=0,column=4,sticky=tk.N)
frame4.load_counts('counts4.txt')
frame4.save_counts('counts4.txt')

frame5 = Frame5(window) 
frame5.grid(row=0,column=5,sticky=tk.N)
frame5.load_counts('counts5.txt')
frame5.save_counts('counts5.txt')

frame6 = Frame6(window) 
frame6.grid(row=0,column=6,sticky=tk.N)
frame6.load_counts('counts6.txt')
frame6.save_counts('counts6.txt')

superass_img = tk.PhotoImage(file='./picture/superass.png')
dropitem2_label = tk.Label(image=superass_img)
dropitem2_label.place(x=500,y=475)

window.mainloop()
