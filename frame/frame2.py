import tkinter as tk
import json

class Frame2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=256, height=500, bd=10, relief='sunken')
        self.parent = parent
        self.grape_count = tk.IntVar()
        self.grapedu_count = tk.IntVar()
        self.grapetr_count = tk.IntVar()
        self.sbsword_count = tk.IntVar()
        self.hourglass_count = tk.IntVar()

        # 老7圖片
        self.boss_img = tk.PhotoImage(file='./picture/seofon.png')
        boss_label = tk.Label(self, image=self.boss_img)
        boss_label.pack()

        # 葡萄1
        grape_img = tk.PhotoImage(file='./picture/grape.png')
        grape_label = tk.Label(self, image=grape_img)
        grape_label.pack()
        grape_count_label = tk.Label(self, textvariable=self.grape_count)
        grape_count_label.pack()
        grape_button = tk.Button(self, text="+1", command=lambda: self.increase_count(self.grape_count))
        grape_button.pack()

        # 葡萄2 grapedu
        grapedu_img = tk.PhotoImage(file='./picture/grapedu.png')
        grapedu_label = tk.Label(self, image=grapedu_img)
        grapedu_label.pack()
        grapedu_count_label = tk.Label(self, textvariable=self.grapedu_count)
        grapedu_count_label.pack()
        grapedu_button = tk.Button(self, text="+1", command=lambda: self.increase_count(self.grapedu_count))
        grapedu_button.pack()

        # 葡萄3 grapetr
        grapetr_img = tk.PhotoImage(file='./picture/grapetr.png')
        grapetr_label = tk.Label(self, image=grapetr_img)
        grapetr_label.pack()
        grapetr_count_label = tk.Label(self, textvariable=self.grapetr_count)
        grapetr_count_label.pack()
        grapetr_button = tk.Button(self, text="+1", command=lambda: self.increase_count(self.grapetr_count))
        grapetr_button.pack()

        # 七劍
        sbsword_img = tk.PhotoImage(file='./picture/sbsword.png')
        sbsword_label = tk.Label(self, image=sbsword_img)
        sbsword_label.pack()
        sbsword_count_label = tk.Label(self, textvariable=self.sbsword_count)
        sbsword_count_label.pack()
        sbsword_button = tk.Button(self, text="+1", command=lambda: self.increase_count(self.sbsword_count))
        sbsword_button.pack()

        # 沙漏
        hourglass_img = tk.PhotoImage(file='./picture/hourglassresize.png')
        hourglass_label = tk.Label(self, image=hourglass_img)
        hourglass_label.pack()
        hourglass_count_label = tk.Label(self, textvariable=self.hourglass_count)
        hourglass_count_label.pack()
        hourglass_button = tk.Button(self, text="+1", command=lambda: self.increase_count(self.hourglass_count))
        hourglass_button.pack()

        # 计算概率标签
        self.probability_labels = []
        self.drop_items = [
            {'name': '葡萄X3', 'image': grape_img},
            {'name': '葡萄X2', 'image': grapedu_img},
            {'name': '葡萄X3', 'image': grapetr_img},
            {'name': '七劍', 'image': sbsword_img},
            {'name': '沙漏', 'image': hourglass_img}
        ]

        for item in self.drop_items:
            probability_label = tk.Label(self, text='')
            probability_label.pack()
            self.probability_labels.append(probability_label)

        self.calculate_probability()
        self.load_counts('counts2.txt')

    def increase_count(self, count_var):
        count_var.set(count_var.get() + 1)
        self.calculate_probability()
        self.save_counts('counts2.txt')

    def calculate_probability(self):
        counts = [
            self.grape_count.get(),
            self.grapedu_count.get(),
            self.grapetr_count.get(),
            self.sbsword_count.get(),
            self.hourglass_count.get()
        ]
        total_count = sum(counts)
        probabilities = [count / total_count * 100 if total_count != 0 else 0 for count in counts]
        for label, probability, item in zip(self.probability_labels, probabilities, self.drop_items):
            label.config(text=f"{item['name']} ({probability:.2f}%)")

    def save_counts(self, filename):
        counts = {
            'grape_count': self.grape_count.get(),
            'grapedu_count': self.grapedu_count.get(),
            'grapetr_count': self.grapetr_count.get(),
            'sbsword_count': self.sbsword_count.get(),
            'hourglass_count': self.hourglass_count.get()
        }

        with open(filename, 'w') as file:
            json.dump(counts, file)

    def load_counts(self, filename):
        try:
            with open(filename, 'r') as file:
                try:
                    counts = json.load(file)

                    # Assign the loaded counts to the count variables
                    self.grape_count.set(counts.get('grape_count', 0))
                    self.grapedu_count.set(counts.get('grapedu_count', 0))
                    self.grapetr_count.set(counts.get('grapetr_count', 0))
                    self.sbsword_count.set(counts.get('sbsword_count', 0))
                    self.hourglass_count.set(counts.get('hourglass_count', 0))
                except json.JSONDecodeError:
                    # Handle the case when the file is empty or contains invalid JSON
                    pass
        except FileNotFoundError:
            pass
