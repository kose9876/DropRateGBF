import tkinter as tk
import json

class Frame1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=300, height=500, bd=10, relief='ridge')
        self.parent = parent
        self.waterchip_count = tk.IntVar()
        self.waterchipdu_count = tk.IntVar()
        self.waterchiptr_count = tk.IntVar()
        self.waterknife_count = tk.IntVar()
        self.hourglass_count = tk.IntVar()

        # 機神圖片
        self.boss_img = tk.PhotoImage(file='./picture/diasppora.png')
        boss_label = tk.Label(self, image=self.boss_img)
        boss_label.pack()

        # 水晶芯片
        waterchip_img = tk.PhotoImage(file='./picture/waterchip.png')
        waterchip_label = tk.Label(self, image=waterchip_img)
        waterchip_label.pack()
        waterchip_count_label = tk.Label(self, textvariable=self.waterchip_count)
        waterchip_count_label.pack()
        waterchip_button = tk.Button(self, text="+1", command=lambda: self.increase_count(self.waterchip_count))
        waterchip_button.pack()

        # 晶片X2
        waterchipdu_img = tk.PhotoImage(file='./picture/waterchipdu.png')
        waterchipdu_label = tk.Label(self, image=waterchipdu_img)
        waterchipdu_label.pack()
        waterchipdu_count_label = tk.Label(self, textvariable=self.waterchipdu_count)
        waterchipdu_count_label.pack()
        waterchipdu_button = tk.Button(self, text="+1", command=lambda: self.increase_count(self.waterchipdu_count))
        waterchipdu_button.pack()

        # 晶片X3
        waterchiptr_img = tk.PhotoImage(file='./picture/waterchiptr.png')
        waterchiptr_label = tk.Label(self, image=waterchiptr_img)
        waterchiptr_label.pack()
        waterchiptr_count_label = tk.Label(self, textvariable=self.waterchiptr_count)
        waterchiptr_count_label.pack()
        waterchiptr_button = tk.Button(self, text="+1", command=lambda: self.increase_count(self.waterchiptr_count))
        waterchiptr_button.pack()

        # G神刀
        waterknife_img = tk.PhotoImage(file='./picture/waterknife.png')
        waterknife_label = tk.Label(self, image=waterknife_img)
        waterknife_label.pack()
        waterknife_count_label = tk.Label(self, textvariable=self.waterknife_count)
        waterknife_count_label.pack()
        waterknife_button = tk.Button(self, text="+1", command=lambda: self.increase_count(self.waterknife_count))
        waterknife_button.pack()

        # 沙漏
        hourglass_img = tk.PhotoImage(file='./picture/hourglass.png')
        hourglass_label = tk.Label(self, image=hourglass_img)
        hourglass_label.pack()
        hourglass_count_label = tk.Label(self, textvariable=self.hourglass_count)
        hourglass_count_label.pack()
        hourglass_button = tk.Button(self, text="+1", command=lambda: self.increase_count(self.hourglass_count))
        hourglass_button.pack()

        # 計算機率標籤
        probability_labels = []
        drop_items = [
            {'name': '晶片X3', 'image': waterchip_img},
            {'name': '晶片X2', 'image': waterchipdu_img},
            {'name': '晶片X3', 'image': waterchiptr_img},
            {'name': '機神刀', 'image': waterknife_img},
            {'name': '沙漏', 'image': hourglass_img}
        ]

        for item in drop_items:
            probability_label = tk.Label(self, text='')
            probability_label.pack()
            probability_labels.append(probability_label)

        self.probability_labels = probability_labels
        self.drop_items = drop_items

        self.calculate_probability()
        self.load_counts('counts.txt')

    def increase_count(self, count_var):
        count_var.set(count_var.get() + 1)
        self.calculate_probability()
        self.save_counts('counts.txt')

    def calculate_probability(self):
        counts = [
            self.waterchip_count.get(),
            self.waterchipdu_count.get(),
            self.waterchiptr_count.get(),
            self.waterknife_count.get(),
            self.hourglass_count.get()
        ]
        total_count = sum(counts)
        probabilities = [count / total_count * 100 if total_count != 0 else 0 for count in counts]

        for label, probability, item in zip(self.probability_labels, probabilities, self.drop_items):
            label.config(text=f"{item['name']} ({probability:.2f}%)")

    def save_counts(self, filename):
        counts = {
            'waterchip_count': self.waterchip_count.get(),
            'waterchipdu_count': self.waterchipdu_count.get(),
            'waterchiptr_count': self.waterchiptr_count.get(),
            'waterknife_count': self.waterknife_count.get(),
            'hourglass_count': self.hourglass_count.get()
        }

        with open(filename, 'w') as file:
            json.dump(counts, file)

    def load_counts(self, filename):
        try:
            with open(filename, 'r') as file:
                counts = json.load(file)
                self.waterchip_count.set(counts.get('waterchip_count', 0))
                self.waterchipdu_count.set(counts.get('waterchipdu_count', 0))
                self.waterchiptr_count.set(counts.get('waterchiptr_count', 0))
                self.waterknife_count.set(counts.get('waterknife_count', 0))
                self.hourglass_count.set(counts.get('hourglass_count', 0))
        except FileNotFoundError:
            print("無法找到計數檔案。")
