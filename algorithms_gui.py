# algorithms_gui.py
import tkinter as tk
from tkinter import ttk
from algrom import *

class SortingApp:
    def __init__(self, master):
        self.master = master
        master.title("Algorithm Visualizer")

        self.label_numbers = tk.Label(master, text="Enter numbers (comma-separated):")
        self.label_numbers.pack()

        self.entry_numbers = tk.Entry(master)
        self.entry_numbers.pack()

        self.label_algorithm = tk.Label(master, text="Choose Algorithm Category:")
        self.label_algorithm.pack()

        self.algo_category_var = tk.StringVar()
        self.algo_category_dropdown = ttk.Combobox(master, textvariable=self.algo_category_var)
        self.algo_category_dropdown['values'] = ('Sorting Algorithms', 'Searching Algorithms', 'Tree Algorithms')
        self.algo_category_dropdown.pack()
        self.algo_category_dropdown.bind("<<ComboboxSelected>>", self.update_algorithm_dropdown)

        self.label_algorithm_type = tk.Label(master, text="Choose Algorithm:")
        self.label_algorithm_type.pack()

        self.algo_var = tk.StringVar()
        self.algo_dropdown = ttk.Combobox(master, textvariable=self.algo_var)
        self.algo_dropdown.pack()

        self.sort_button = tk.Button(master, text="Run Algorithm", command=self.run_algorithm)
        self.sort_button.pack()

    def update_algorithm_dropdown(self, event):
        selected_category = self.algo_category_var.get()
        algorithms = {
            'Sorting Algorithms': ['Bubble Sort', 'Binary Search'],
            'Searching Algorithms': ['Binary Search'],
            'Tree Algorithms': ['Inorder Traversal']
        }

        if selected_category in algorithms:
            self.algo_dropdown['values'] = algorithms[selected_category]
            self.algo_dropdown.set(algorithms[selected_category][0])
        else:
            self.algo_dropdown.set("")

    def run_algorithm(self):
        try:
            input_values = list(map(int, self.entry_numbers.get().split(',')))
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
            return

        algorithm_category = self.algo_category_var.get()
        algorithm_type = self.algo_var.get()

        if algorithm_category == 'Sorting Algorithms':
            self.run_sorting_algorithm(algorithm_type, input_values)
        elif algorithm_category == 'Searching Algorithms':
            self.run_searching_algorithm(algorithm_type, input_values)
        elif algorithm_category == 'Tree Algorithms':
            self.run_tree_algorithm(algorithm_type, input_values)

    def run_sorting_algorithm(self, algorithm_type, input_values):
        algorithms = {
            'Bubble Sort': bubble_sort,
            'Binary Search': binary_search
        }
        if algorithm_type in algorithms:
            algorithms[algorithm_type](input_values)
            print(f"Sorted values: {input_values}")
        else:
            print("Invalid sorting algorithm selected.")

    def run_searching_algorithm(self, algorithm_type, input_values):
        algorithms = {
            'Binary Search': binary_search
        }
        try:
            target = int(input("Enter the target value: "))
        except ValueError:
            print("Invalid target value. Please enter a number.")
            return

        if algorithm_type in algorithms:
            result = algorithms[algorithm_type](input_values, target)
            if result != -1:
                print(f"Target found at index: {result}")
            else:
                print("Target not found.")
        else:
            print("Invalid searching algorithm selected.")

    def run_tree_algorithm(self, algorithm_type, input_values):
        if algorithm_type == 'Inorder Traversal':
            # Replace this with your Inorder Traversal implementation
            print("Running Inorder Traversal")
        else:
            print("Invalid tree algorithm selected.")

def main():
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
