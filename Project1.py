import tkinter as tk
from tkinter import messagebox

class BankersAlgorithmGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Banker's Algorithm")
        
        # Labels
        tk.Label(root, text="Total Resources:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Available Resources:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(root, text="Current Allocation:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(root, text="Maximum Need:").grid(row=3, column=0, padx=10, pady=5)
        
        # Entry fields
        self.total_resources_entry = tk.Entry(root)
        self.total_resources_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.available_resources_entry = tk.Entry(root)
        self.available_resources_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.current_allocation_entry = tk.Text(root, width=30, height=8)
        self.current_allocation_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.maximum_need_entry = tk.Text(root, width=30, height=8)
        self.maximum_need_entry.grid(row=3, column=1, padx=10, pady=5)
        
        # Buttons
        self.check_button = tk.Button(root, text="Check Safety", command=self.check_safety)
        self.check_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    
    def parse_input(self):
        try:
            total_resources = list(map(int, self.total_resources_entry.get().strip().split()))
            available_resources = list(map(int, self.available_resources_entry.get().strip().split()))
            current_allocation = [list(map(int, row.strip().split())) for row in self.current_allocation_entry.get("1.0", tk.END).strip().split('\n')]
            maximum_need = [list(map(int, row.strip().split())) for row in self.maximum_need_entry.get("1.0", tk.END).strip().split('\n')]
            
            return total_resources, available_resources, current_allocation, maximum_need
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input format. Please enter valid numbers.")
    
    def check_safety(self):
        input_data = self.parse_input()
        if input_data:
            total_resources, available_resources, current_allocation, maximum_need = input_data

        # Initialize the necessary variables
            work = available_resources.copy()
            finish = [False] * len(current_allocation)
            need = [[maximum_need[i][j] - current_allocation[i][j] for j in range(len(total_resources))] for i in range(len(current_allocation))]
            safe_sequence = []

        # Find a process that can be executed
            def find_process():
                for i in range(len(current_allocation)):
                    if not finish[i] and all(need[i][j] <= work[j] for j in range(len(total_resources))):
                        return i
                return None

        # Execute the Banker's algorithm
            while True:
                process = find_process()

                if process is None:
                    break

            # Execute the process and release its resources
                finish[process] = True
                work = [work[j] + current_allocation[process][j] for j in range(len(total_resources))]
                safe_sequence.append(process)

            if all(finish):
                messagebox.showinfo("System Safety", "The system is in a safe state.")
            else:
                messagebox.showwarning("System Safety", "The system is in an unsafe state.")


# Create the Tkinter window
root = tk.Tk()

# Create the BankersAlgorithmGUI object
bankers_gui = BankersAlgorithmGUI(root)

# Start the Tkinter event loop
root.mainloop()