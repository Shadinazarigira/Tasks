import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.geometry("185x260")
root.title("Calculator")


entry = tk.Entry(root, font=("Arial", 10), borderwidth=2, relief="ridge")
entry.grid(row=0, column=0, columnspan=20, padx=20, pady=10)

buttons = [
    '<-','CE','C','sqrt',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0','.','+', '='
    ]

row_val = 1
col_val = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font=("boldArial", 14), width=3, height=1,bg='purple',fg='white')
    button.grid(row=row_val, column=col_val, padx=1, pady=1)
    button.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
root.mainloop()

