import tkinter as tk
from tkinter import font

try:
    from app.cong import phep_cong
    #from tru import phep_tru
    #from nhan import phep_nhan
    #from chia import phep_chia
except ImportError as e:
    print(f"LỖI: Không thể import các module tính toán. Hãy chắc chắn các file cong.py, tru.py,... tồn tại.")
    print(f"Chi tiết lỗi: {e}")
    exit()

def main():
    root = tk.Tk()
    root.title("Máy tính bỏ túi")
    root.geometry("400x600")
    root.resizable(False, False)

    colors = {
        "display_bg": "#FFFFFF", "display_fg": "#000000",
        "button_bg": "#F0F0F0", "button_fg": "#000000",
        "equals_bg": "#4CAF50", "equals_fg": "#FFFFFF",
        "clear_bg": "#f44336", "clear_fg": "#FFFFFF",
    }
    display_font = font.Font(family="Arial", size=32, weight="bold")
    button_font = font.Font(family="Arial", size=18)

    display_var = tk.StringVar()


    def on_button_click(char):
        current_text = display_var.get()
        if current_text == "Lỗi":
            current_text = ""
        display_var.set(current_text + str(char))

    def clear_display():
        display_var.set("")

    def handle_equals():
        expression = display_var.get()
        result = ""
        
        try:
            if '+' in expression:
                parts = expression.split('+')
                numbers = [float(p) for p in parts]
                result = phep_cong(*numbers)
            
            elif '-' in expression:
                parts = expression.split('-', 1)
                num1, num2 = float(parts[0]), float(parts[1])
                result = phep_tru(num1, num2)
                
            elif '*' in expression:
                parts = expression.split('*', 1)
                num1, num2 = float(parts[0]), float(parts[1])
                result = phep_nhan(num1, num2)

            elif '/' in expression:
                parts = expression.split('/', 1)
                num1, num2 = float(parts[0]), float(parts[1])
                result = phep_chia(num1, num2)
            else:
                result = expression

            if isinstance(result, float):
                if result.is_integer():
                    display_var.set(str(int(result)))
                else:
                    display_var.set(str(round(result, 8)))
            else:
                display_var.set(str(result))

        except Exception as e:
            print(f"Lỗi tính toán: {e}")
            display_var.set("Lỗi")

    display_frame = tk.Frame(root, bg=colors["display_bg"])
    display_frame.pack(expand=True, fill="both")
    display_entry = tk.Entry(display_frame, textvariable=display_var, font=display_font,
                             bg=colors["display_bg"], fg=colors["display_fg"],
                             justify="right", bd=0, state="readonly")
    display_entry.pack(expand=True, fill="both", padx=10, pady=20)

    buttons_frame = tk.Frame(root)
    buttons_frame.pack(expand=True, fill="both")
    for i in range(5): buttons_frame.rowconfigure(i, weight=1)
    for i in range(4): buttons_frame.columnconfigure(i, weight=1)

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]
    
    row, col = 0, 0
    for text in buttons:
        if text == '=':
            bg, fg, cmd = colors["equals_bg"], colors["equals_fg"], handle_equals
        else:
            bg, fg = colors["button_bg"], colors["button_fg"]
            cmd = lambda t=text: on_button_click(t)

        button = tk.Button(buttons_frame, text=text, font=button_font, bg=bg, fg=fg,
                           relief="ridge", bd=1, command=cmd)
        button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        
        col += 1
        if col > 3:
            col = 0
            row += 1

    clear_button = tk.Button(buttons_frame, text="Xóa", font=button_font,
                             bg=colors["clear_bg"], fg=colors["clear_fg"],
                             relief="ridge", bd=1, command=clear_display)
    clear_button.grid(row=4, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

    root.mainloop()


if __name__ == "__main__":
    main()
