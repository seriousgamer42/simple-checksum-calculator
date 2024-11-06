import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import tkinter.messagebox as messagebox

class ChecksumCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Checksum Calculator")
        self.root.geometry("400x500")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Input area
        ttk.Label(main_frame, text="Enter text to calculate checksum:", 
                 font=('Arial', 10, 'bold')).grid(row=0, column=0, pady=5, sticky=tk.W)
        
        # Scrolled text widget for input
        self.input_text = scrolledtext.ScrolledText(main_frame, width=40, height=10)
        self.input_text.grid(row=1, column=0, pady=5)
        
        # Calculate button
        self.calc_button = ttk.Button(main_frame, text="Calculate Checksum",
                                    command=self.calculate_checksum)
        self.calc_button.grid(row=2, column=0, pady=10)
        
        # Results area
        result_frame = ttk.LabelFrame(main_frame, text="Results", padding="5")
        result_frame.grid(row=3, column=0, pady=10, sticky=(tk.W, tk.E))
        
        # Decimal result
        ttk.Label(result_frame, text="Decimal:").grid(row=0, column=0, padx=5, sticky=tk.W)
        self.decimal_result = ttk.Label(result_frame, text="--")
        self.decimal_result.grid(row=0, column=1, padx=5, sticky=tk.W)
        
        # Hexadecimal result
        ttk.Label(result_frame, text="Hexadecimal:").grid(row=1, column=0, padx=5, sticky=tk.W)
        self.hex_result = ttk.Label(result_frame, text="--")
        self.hex_result.grid(row=1, column=1, padx=5, sticky=tk.W)
        
        # Binary result
        ttk.Label(result_frame, text="Binary:").grid(row=2, column=0, padx=5, sticky=tk.W)
        self.binary_result = ttk.Label(result_frame, text="--")
        self.binary_result.grid(row=2, column=1, padx=5, sticky=tk.W)
        
        # Clear button
        self.clear_button = ttk.Button(main_frame, text="Clear",
                                     command=self.clear_all)
        self.clear_button.grid(row=4, column=0, pady=10)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(main_frame, textvariable=self.status_var,
                                  relief=tk.SUNKEN)
        self.status_bar.grid(row=5, column=0, sticky=(tk.W, tk.E))
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

    def simple_checksum(self, data):
        try:
            checksum = 0
            for char in data:
                checksum += ord(char)  # Add the ASCII value of each character
            checksum &= 0xFF  # Keep only the least significant 8 bits
            return checksum
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating checksum: {str(e)}")
            return None

    def calculate_checksum(self):
        data = self.input_text.get("1.0", tk.END).strip()
        if not data:
            self.status_var.set("Please enter some text first!")
            return
        
        checksum = self.simple_checksum(data)
        if checksum is not None:
            # Update results
            self.decimal_result.config(text=str(checksum))
            self.hex_result.config(text=f"0x{checksum:02X}")
            self.binary_result.config(text=f"0b{checksum:08b}")
            self.status_var.set(f"Checksum calculated successfully for {len(data)} characters")

    def clear_all(self):
        self.input_text.delete("1.0", tk.END)
        self.decimal_result.config(text="--")
        self.hex_result.config(text="--")
        self.binary_result.config(text="--")
        self.status_var.set("")

def main():
    root = tk.Tk()
    app = ChecksumCalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()