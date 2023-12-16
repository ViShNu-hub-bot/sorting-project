import tkinter as tk
from tkinter import messagebox
import random
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import inspect

class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer Developed by vishnukanth")

        self.data = []
        self.fig, self.ax = Figure(figsize=(6, 4), dpi=100), None
        self.canvas = None
        self.text_area = None
        self.explanation_var = tk.StringVar()
        self.animation_speed = 500

        self.input_label = tk.Label(root, text="Enter numbers (comma-separated):")
        self.input_label.pack()

        self.input_entry = tk.Entry(root)
        self.input_entry.pack()

        self.sort_button = tk.Button(root, text="Sort", command=self.sort)
        self.sort_button.pack()

        self.algorithms = {
            "Bubble Sort": self.bubble_sort,
            "Selection Sort": self.selection_sort,
            "Insertion Sort": self.insertion_sort,
            "Merge Sort": self.merge_sort,
            "Quick Sort": self.quick_sort,
            "Heap Sort": self.heap_sort,
            "Radix Sort": self.radix_sort,
        }

        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("Bubble Sort")

        self.algorithm_menu = tk.OptionMenu(root, self.algorithm_var, *self.algorithms.keys())
        self.algorithm_menu.pack()

        self.text_area = tk.Text(root, height=10, width=50, wrap="word")
        self.text_area.pack()

        self.definition_area = tk.Text(root, height=10, width=50, wrap="word")
        self.definition_area.pack()

        # Definitions for each sorting algorithm
        self.algorithm_definitions = {
            "Bubble Sort": "Bubble Sort:\nCompare adjacent elements and swap if they are in the wrong order. Repeat the process until the list is sorted.",
            "Selection Sort": "Selection Sort:\nFind the minimum element in the unsorted part of the list. Swap it with the first element of the unsorted part. Repeat until the entire list is sorted.",
            "Insertion Sort": "Insertion Sort:\nBuild a sorted sequence gradually by repeatedly taking elements from the unsorted part and inserting them into their correct position in the sorted part.",
            "Merge Sort": "Merge Sort:\nDivide the unsorted list into n sublists, each containing one element. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining.",
            "Quick Sort": "Quick Sort:\nChoose a pivot element and partition the array around the pivot. Recursively sort the subarrays on either side of the pivot.",
            "Heap Sort": "Heap Sort:\nBuild a max heap from the array. Extract elements from the heap one by one to get a sorted array.",
            "Radix Sort": "Radix Sort:\nSort the elements by individual digits. Starting from the least significant digit to the most significant digit."
        }

    def sort(self):
        input_data = self.input_entry.get()
        try:
            self.data = [int(x) for x in input_data.split(",")]
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter comma-separated integers.")
            return

        algorithm = self.algorithm_var.get()
        sort_function = self.algorithms[algorithm]
        code = self.get_algorithm_code(sort_function)

        # Clear previous code
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.config(state=tk.DISABLED)

        # Insert new code
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, code)
        self.text_area.config(state=tk.DISABLED)

        # Display definition
        self.definition_area.config(state=tk.NORMAL)
        self.definition_area.delete(1.0, tk.END)
        self.definition_area.insert(tk.END, self.algorithm_definitions[algorithm])
        self.definition_area.config(state=tk.DISABLED)

        self.visualize_sort(sort_function)

    def visualize_sort(self, sort_function):
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)
        self.ax.bar(range(len(self.data)), self.data, color='blue')
        self.canvas.draw()

        # Call the selected sorting algorithm
        sort_function()

        # Draw the sorted bars
        self.ax.bar(range(len(self.data)), self.data, color='green')
        self.canvas.draw()

    def update_plot(self, text=None):
        self.ax.clear()
        self.ax.bar(range(len(self.data)), self.data, color='blue')
        if text:
            self.ax.text(0.5, 1.08, text, horizontalalignment='center', verticalalignment='center', transform=self.ax.transAxes)
        self.canvas.draw()
        self.root.update()
        time.sleep(self.animation_speed / 1000)

    def bubble_sort(self):
        """
        Bubble Sort:
        Compare adjacent elements and swap if they are in the wrong order.
        Repeat the process until the list is sorted.
        """
        n = len(self.data)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    text = f"Iteration: {i + 1}, Swapping: {self.data[j]} and {self.data[j+1]}"
                    self.update_plot(text)

    def selection_sort(self):
        """
        Selection Sort:
        Find the minimum element in the unsorted part of the list.
        Swap it with the first element of the unsorted part.
        Repeat until the entire list is sorted.
        """
        n = len(self.data)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = j
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            text = f"Iteration: {i + 1}, Swapping: {self.data[i]} and {self.data[min_index]}"
            self.update_plot(text)

    def insertion_sort(self):
        """
        Insertion Sort:
        Build a sorted sequence gradually by repeatedly taking elements
        from the unsorted part and inserting them into their correct position in the sorted part.
        """
        n = len(self.data)
        for i in range(1, n):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key
            text = f"Iteration: {i}, Key: {key}, Shifting: {self.data[j]} to {j + 1}"
            self.update_plot(text)

    def merge_sort(self):
        """
        Merge Sort:
        Divide the unsorted list into n sublists, each containing one element.
        Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining.
        """
        if len(self.data) > 1:
            mid = len(self.data) // 2
            left_half = self.data[:mid]
            right_half = self.data[mid:]

            self.data = self.merge_sort_helper(left_half) + self.merge_sort_helper(right_half)
            text = "Merging: {} and {}".format(left_half, right_half)
            self.update_plot(text)

    def merge_sort_helper(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            data = self.merge_sort_helper(left_half) + self.merge_sort_helper(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1

        return data

    def quick_sort(self):
        """
        Quick Sort:
        Choose a pivot element and partition the array around the pivot.
        Recursively sort the subarrays on either side of the pivot.
        """
        self.quick_sort_helper(0, len(self.data) - 1)

    def quick_sort_helper(self, low, high):
        if low < high:
            pivot_index = self.partition(low, high)
            self.quick_sort_helper(low, pivot_index - 1)
            self.quick_sort_helper(pivot_index + 1, high)

    def partition(self, low, high):
        pivot = self.data[high]
        i = low - 1
        for j in range(low, high):
            if self.data[j] <= pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        text = f"Pivot: {pivot}, Partitioning: {self.data[low:high + 1]}"
        self.update_plot(text)

    def heap_sort(self):
        """
        Heap Sort:
        Build a max heap from the array.
        Extract elements from the heap one by one to get a sorted array.
        """
        n = len(self.data)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]
            text = f"Extracting Max: {self.data[i]}, Remaining Heap: {self.data[:i]}"
            self.update_plot(text)
            self.heapify(i, 0)

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.data[left] > self.data[largest]:
            largest = left

        if right < n and self.data[right] > self.data[largest]:
            largest = right

        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            text = f"Swapping: {self.data[i]} and {self.data[largest]}, Heap: {self.data}"
            self.update_plot(text)
            self.heapify(n, largest)

    def radix_sort(self):
        """
        Radix Sort:
        Sort the elements by individual digits.
        Starting from the least significant digit to the most significant digit.
        """
        max_num = max(self.data)
        exp = 1

        while max_num // exp > 0:
            self.counting_sort(exp)
            exp *= 10

    def counting_sort(self, exp):
        n = len(self.data)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = self.data[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = self.data[i] // exp
            output[count[index % 10] - 1] = self.data[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            self.data[i] = output[i]
        text = f"Sorting by digit {exp}: {self.data}"
        self.update_plot(text)

    def get_algorithm_code(self, algorithm):
        # Get the source code of the selected algorithm function
        source_code = inspect.getsource(algorithm)
        return source_code

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root)

    app.canvas = FigureCanvasTkAgg(app.fig, master=root)
    app.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    app.root.mainloop()
