import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Máy tính bỏ túi")
    root.geometry("400x600")
    root.resizable(False, False)
    
    expression = ""
    
    colors = {
        "display_bg": "#FFFFFF",
        "display_fg": "#000000",
        "button_bg": "#F0F0F0",
        "button_fg": "#000000",
        "equals_bg": "#4CAF50",
        "equals_fg": "#FFFFFF",
        "clear_bg": "#f44336",
        "clear_fg": "#FFFFFF",
    }
    display_font = font.Font(family="Arial", size=32, weight="bold")
    button_font = font.Font(family="Arial", size=18)
    
    def on_button_click(char):
        nonlocal expression
        if char == '=':
            calculate()
        else:
            expression += str(char)
            display_var.set(expression)

    def clear_display():
        nonlocal expression
        expression = ""
        display_var.set(expression)

    def calculate():
        nonlocal expression
        try:
            result = str(eval(expression))
            display_var.set(result)
            expression = result
        except (SyntaxError, ZeroDivisionError):
            display_var.set("Lỗi")
            expression = ""
    display_frame = tk.Frame(root, bg=colors["display_bg"])
    display_frame.pack(expand=True, fill="both")

    display_var = tk.StringVar()
    display_entry = tk.Entry(display_frame,
                             textvariable=display_var,
                             font=display_font,
                             bg=colors["display_bg"],
                             fg=colors["display_fg"],
                             justify="right",
                             bd=0,
                             state="readonly")
    display_entry.pack(expand=True, fill="both", padx=10, pady=20)

    buttons_frame = tk.Frame(root)
    buttons_frame.pack(expand=True, fill="both")

    for i in range(5):
        buttons_frame.rowconfigure(i, weight=1)
    for i in range(4):
        buttons_frame.columnconfigure(i, weight=1)

    # Danh sách các nút
    buttons = [
        ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
        ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
        ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
        ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
    ]

    # Dùng vòng lặp để tạo các nút
    for (text, row, col) in buttons:
        if text == '=':
            bg_color = colors["equals_bg"]
            fg_color = colors["equals_fg"]
        else:
            bg_color = colors["button_bg"]
            fg_color = colors["button_fg"]

        button = tk.Button(buttons_frame,
                           text=text,
                           font=button_font,
                           bg=bg_color,
                           fg=fg_color,
                           relief="ridge",
                           bd=1,
                           command=lambda t=text: on_button_click(t))
        button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

    clear_button = tk.Button(buttons_frame,
                             text="Xóa",
                             font=button_font,
                             bg=colors["clear_bg"],
                             fg=colors["clear_fg"],
                             relief="ridge",
                             bd=1,
                             command=clear_display)
    clear_button.grid(row=4, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

    root.mainloop()


if __name__ == "__main__":
    main()
