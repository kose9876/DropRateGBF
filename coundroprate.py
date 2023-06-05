import tkinter as tk

window = tk.Tk()
window.title('機神系列沙漏武器掉落率統計機')
window.geometry('1800x600')
window.resizable(False, False)
#window.iconbitmap('icon.ico')

#區塊1 機神
frame1 = tk.Frame(window, width=256, height=500,bd=10,relief='sunken')
frame1.pack(side=tk.LEFT, padx=10, pady=10)
#diapora img
Diasporadrimg = tk.PhotoImage(file='diasppora.png')
Diasporadr = tk.Label(frame1,image=Diasporadrimg)
Diasporadr.pack()


waterchipimg =tk.PhotoImage(file='waterchip.png')
waterchip = tk.Label(frame1,image=waterchipimg)
waterchip.pack()


waterchipduimg =tk.PhotoImage(file='waterchipdu.png')
waterchipdu = tk.Label(frame1,image=waterchipduimg)
waterchipdu.pack()


iwaterchiptrimg =tk.PhotoImage(file='waterchiptr.png')
waterchiptr = tk.Label(frame1,image=iwaterchiptrimg)
waterchiptr.pack()


waterknifeimg =tk.PhotoImage(file='waterknife.png')
waterknife = tk.Label(frame1,image=waterknifeimg)
waterknife.pack()


hourglassimg = tk.PhotoImage(file='hourglass.png')
hourglass = tk.Label(frame1,image=hourglassimg)
hourglass.pack()



window.mainloop()