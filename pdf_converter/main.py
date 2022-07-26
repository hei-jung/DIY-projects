from pdf_generator import pdf_generator
import init_ui as ui
import tkinter as tk
import make_widgets as widgets

if __name__ == '__main__':
    root = tk.Tk()
    app = ui.AppWindow(root)
    widgets.make(app)
    app.mainloop()
