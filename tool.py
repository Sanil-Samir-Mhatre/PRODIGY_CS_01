import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    
    return result

def process_text(mode):
    text = text_entry.get("1.0", tk.END).strip()
    shift = shift_entry.get()
    
    if not shift.isdigit():
        messagebox.showerror("Input Error", "Shift value must be a number!")
        return
    
    shift = int(shift)
    result = caesar_cipher(text, shift, mode)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state=tk.DISABLED)

def clear_input():
    text_entry.delete("1.0", tk.END)

def clear_output():
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)

def exit_app():
    root.destroy()

# Modernized GUI
root = tk.Tk()
root.title("Caesar Cipher Encryption & Decryption")
root.geometry("800x600")
root.configure(bg="#2c3e50")  # Dark background color

# Heading
heading = tk.Label(root, text="Caesar Cipher Tool", font=("Arial", 28, "bold"), bg="#2c3e50", fg="#ecf0f1")
heading.pack(pady=20)

# Input Text
text_label = tk.Label(root, text="Enter Text:", font=("Arial", 16), bg="#2c3e50", fg="#ecf0f1")
text_label.pack()
text_entry = tk.Text(root, height=5, width=60, font=("Arial", 14), bg="#34495e", fg="#ecf0f1", insertbackground="#ecf0f1")
text_entry.pack(pady=10)

# Shift Value
shift_label = tk.Label(root, text="Shift Value:", font=("Arial", 16), bg="#2c3e50", fg="#ecf0f1")
shift_label.pack()
shift_entry = tk.Entry(root, font=("Arial", 14), width=10, bg="#34495e", fg="#ecf0f1", insertbackground="#ecf0f1")
shift_entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=20)

encrypt_button = tk.Button(button_frame, text="Encrypt", font=("Arial", 14), bg="#1abc9c", fg="white", command=lambda: process_text("encrypt"))
encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = tk.Button(button_frame, text="Decrypt", font=("Arial", 14), bg="#3498db", fg="white", command=lambda: process_text("decrypt"))
decrypt_button.grid(row=0, column=1, padx=10)

clear_input_button = tk.Button(button_frame, text="Clear Input", font=("Arial", 14), bg="black", fg="white", command=clear_input)
clear_input_button.grid(row=0, column=2, padx=10)

clear_output_button = tk.Button(button_frame, text="Clear Output", font=("Arial", 14), bg="black", fg="white", command=clear_output)
clear_output_button.grid(row=0, column=3, padx=10)

exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 14), bg="#e74c3c", fg="white", command=exit_app)
exit_button.grid(row=0, column=4, padx=10)

# Output Text
output_label = tk.Label(root, text="Result:", font=("Arial", 16), bg="#2c3e50", fg="#ecf0f1")
output_label.pack()
output_text = tk.Text(root, height=5, width=60, font=("Arial", 14), bg="#34495e", fg="#ecf0f1", state=tk.DISABLED)
output_text.pack(pady=10)

root.mainloop()
