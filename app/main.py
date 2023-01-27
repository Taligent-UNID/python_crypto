import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # UI options
        paddings = {'padx': 5, 'pady': 10}

        # configure the root window
        self.title('Secure Delivery of Credentials - Taligent')
        self.geometry('800x800')
        self.config(bg='white')
        self.iconbitmap('images/taligent.ico')

        # Styles
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        #Style Buttons
        self.style.configure(
            'TButton',
            font=('Roboto 12'),
            background='#F4A91C',
            width=20
        )
        self.style.map(
            "TButton",
            background=[("active", "#EB7522")]
        )
        #Style Headings Label
        self.style.configure(
            'Headings.TLabel',
            font=('Roboto 15'),
        )

        # Label
        self.label = ttk.Label(text='Secure Delivery of Credentials')
        self.label.config(
            font=('Roboto 20 bold'),
            background='white',
            foreground='#EB7522'
        )
        self.label.pack(**paddings)

        # Frame Generate Key Pair
        self.frame1 = ttk.Frame(self)
        self.frame1.config(width=400,height=400)
        self.frame1.pack(side='left')
        self.frame1.pack(anchor='ne')

        self.label_frame1 = ttk.Label(
            self.frame1,
            text='Generate Key Pair',
            style='Headings.TLabel'
        )
        self.label_frame1.pack()

        self.button_frame1 = ttk.Button(
            self.frame1,
            text='Generate Key Pair',
        )
        self.button_frame1.pack()

        def filename_path():
            filename = filedialog.askdirectory()
            self.label_directory_frame1.config(text=filename)

        self.button_directory_frame1 = ttk.Button(
            self.frame1,
            text='Select Directory..',
            command=filename_path
        )
        self.button_directory_frame1.pack(side='left')

        self.label_directory_frame1 = ttk.Label(
            text='...'
        )
        self.label_directory_frame1.pack(side='right')





if __name__ == '__main__':
    app = MainApp()
    app.mainloop()