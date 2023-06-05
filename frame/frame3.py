import tkinter as tk
import json

class Frame3(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=256, height=500, bd=10, relief='ridge')
        self.parent = parent
        self.dropitem1_count = tk.IntVar()
        self.dropitem2_count = tk.IntVar()
        self.dropitem3_count = tk.IntVar()
        self.dropitem4_count = tk.IntVar()
        self.dropitem5_count = tk.IntVar()

        # BOSS
        self.boss_img = tk.PhotoImage(file='./picture/Proto_Bahamut.png')
        boss_label = tk.Label(self, image=self.boss_img)
        boss_label.pack()

        # 物品1
        dropitem1_img = tk.PhotoImage(file='./picture/Gold_Brick.png')
        dropitem1_label = tk.Label(self, image=dropitem1_img)
        dropitem1_label.pack()
        dropitem1_count_label = tk.Label(self, textvariable=self.dropitem1_count)
        dropitem1_count_label.pack()
        dropitem1_button = tk.Button(self, text="+1", command=lambda: self.increase_count(self.dropitem1_count))
        dropitem1_button.pack()

        # 物品2
        dropitem2_img = tk.PhotoImage(file='./picture/urblack.png')
        dropitem2_label = tk.Label(self, image=dropitem2_img)
        dropitem2_label.pack()
        dropitem2_count_label = tk.Label(self, textvariable=self.dropitem2_count)
        dropitem2_count_label.pack()
        dropitem2_button = tk.Button(self, text="+1", command=lambda: self.increase_count(self.dropitem2_count))
        dropitem2_button.pack()

        # 物品3
        dropitem3_img = tk.PhotoImage(file='./picture/nexttime.png')
        dropitem3_label = tk.Label(self, image=dropitem3_img)
        dropitem3_label.pack()
        dropitem3_count_label = tk.Label(self, textvariable=self.dropitem3_count)
        dropitem3_count_label.pack()
        dropitem3_button = tk.Button(self, text="+1", command=lambda: self.increase_count(self.dropitem3_count))
        dropitem3_button.pack()

        # 物品4
        dropitem4_img = tk.PhotoImage(file='./picture/losegoldagain.png')
        dropitem4_label = tk.Label(self, image=dropitem4_img)
        dropitem4_label.pack()
        dropitem4_count_label = tk.Label(self, textvariable=self.dropitem4_count)
        dropitem4_count_label.pack()
        dropitem4_button = tk.Button(self, text="+1", command=lambda: self.increase_count(self.dropitem4_count))
        dropitem4_button.pack()

        # 物品5
        dropitem5_img = tk.PhotoImage(file='./picture/apicsofshit.png')
        dropitem5_label = tk.Label(self, image=dropitem5_img)
        dropitem5_label.pack()
        dropitem5_count_label = tk.Label(self, textvariable=self.dropitem5_count)
        dropitem5_count_label.pack()
        dropitem5_button = tk.Button(self, text="+1", command=lambda: self.increase_count(self.dropitem5_count))
        dropitem5_button.pack()

        # 计算概率标签
        self.probability_labels = []
        self.drop_items = [
            {'name': '金塊', 'image': dropitem1_img},
            {'name': '榮冠', 'image': dropitem2_img},
            {'name': '霸者', 'image': dropitem3_img},
            {'name': '至極', 'image': dropitem4_img},
            {'name': '垃圾', 'image': dropitem5_img}
        ]

        for item in self.drop_items:
            probability_label = tk.Label(self, text='')
            probability_label.pack()
            self.probability_labels.append(probability_label)

        self.calculate_probability()
        self.load_counts('counts3.txt')

    def increase_count(self, count_var):
        count_var.set(count_var.get() + 1)
        self.calculate_probability()
        self.save_counts('counts3.txt')

    def calculate_probability(self):
        counts = [
            self.dropitem1_count.get(),
            self.dropitem2_count.get(),
            self.dropitem3_count.get(),
            self.dropitem4_count.get(),
            self.dropitem5_count.get()
        ]
        total_count = sum(counts)
        probabilities = [count / total_count * 100 if total_count != 0 else 0 for count in counts]
        for label, probability, item in zip(self.probability_labels, probabilities, self.drop_items):
            label.config(text=f"{item['name']} ({probability:.2f}%)")

    def save_counts(self, filename):
        counts = {
            'dropitem1_count': self.dropitem1_count.get(),
            'dropitem2_count': self.dropitem2_count.get(),
            'dropitem3_count': self.dropitem3_count.get(),
            'dropitem4_count': self.dropitem4_count.get(),
            'dropitem5_count': self.dropitem5_count.get()
        }

        with open(filename, 'w') as file:
            json.dump(counts, file)

    def load_counts(self, filename):
        try:
            with open(filename, 'r') as file:
                try:
                    counts = json.load(file)

                    # Assign the loaded counts to the count variables
                    self.dropitem1_count.set(counts.get('dropitem1_count', 0))
                    self.dropitem2_count.set(counts.get('dropitem2_count', 0))
                    self.dropitem3_count.set(counts.get('dropitem3_count', 0))
                    self.dropitem4_count.set(counts.get('dropitem4_count', 0))
                    self.dropitem5_count.set(counts.get('dropitem5_count', 0))
                except json.JSONDecodeError:
                    # Handle the case when the file is empty or contains invalid JSON
                    pass
        except FileNotFoundError:
            pass
