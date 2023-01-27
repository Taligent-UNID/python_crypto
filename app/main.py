import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as mb
from rsa_encryption import create_pair_keys,generate_password
import pyperclip as pc

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # UI options
        paddings = {'padx': 5, 'pady': 10}

        # configure the root window
        self.title('Secure Delivery of Credentials - Taligent')
        self.geometry('800x800')
        self.config(bg='white')
        self.iconbitmap('app/images/taligent.ico')

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
        self.label.grid(row=0,column=0,columnspan=2,**paddings)

        # Frame 1 Generate Key Pair
        self.frame1 = ttk.Frame(self)
        self.frame1.config(width=400,height=400)
        self.frame1.grid(row=1,column=0)

        self.label_frame1 = ttk.Label(
            self.frame1,
            text='Generate Key Pair',
            style='Headings.TLabel'
        ).pack()

        def filename_path_frame1():
            filename = filedialog.askdirectory()
            if filename:
                self.label_directory_frame1.config(text=filename)
                self.button_generate_frame1.config(state='enabled')
                self.filename = filename

        self.button_directory_frame1 = ttk.Button(
            self.frame1,
            text='Save keys pair..',
            command=filename_path_frame1
        ).pack()

        self.label_directory_frame1 = ttk.Label(
            self.frame1,
            text='Path Save As Keys..'
        )
        self.label_directory_frame1.pack()

        def generate_keys_message():
            create_pair_keys(self.filename)
            mb.showinfo('SDC','Credenciales creadas...')
            self.label_directory_frame1.config(text='Path Save As Keys..')
            self.button_generate_frame1.config(state='disabled')

        self.button_generate_frame1 = ttk.Button(
            self.frame1,
            text='Generate',
            state='disabled',
            command=generate_keys_message
        ).pack()

        # Frame 2 Generate Password Random
        self.frame2 = ttk.Frame(self)
        self.frame2.config(width=400,height=400)
        self.frame2.grid(row=1,column=1)

        self.title_frame2 = ttk.Label(
            self.frame2,
            text='Generate Password Random',
            style='Headings.TLabel'
        ).pack()

        self.label_password_frame2 = ttk.Label(
            self.frame2,
            text='Password generated random...'
        )

        def generate_password_label():
            password = generate_password()
            self.label_password_frame2.config(text=password)
            pc.copy(password)
            mb.showinfo('SDC','Password generada y copiada...')

        self.button_generate_pass_frame2 = ttk.Button(
            self.frame2,
            text='Generate',
            command=generate_password_label
        ).pack()

        self.label_password_frame2.pack()

        self.button_copy_pass_frame2 = ttk.Button(
            self.frame2,
            text='Copy',
            command=lambda: pc.copy(self.label_password_frame2['text'])
        ).pack()
    
        # Frame 3 Encrypt Password
        self.frame3 = ttk.Frame(self)
        self.frame3.config(width=400,height=400)
        self.frame3.grid(row=2,column=0)

        self.title_frame3 = ttk.Label(
            self.frame3,
            text='Generate File Encrypt',
            style='Headings.TLabel'
        ).pack()

        def filename_path_frame3():
            filename = filedialog.askdirectory()
            if filename:
                self.label_directory_frame3.config(text=filename,textvariable=filename)
                if self.label_private_key_frame3['textvariable']:
                    self.button_generate_frame3.config(state='enabled')
                self.filename = filename

        self.button_directory_frame3 = ttk.Button(
            self.frame3,
            text='Save file encrypt..',
            command=filename_path_frame3
        ).pack()

        self.label_directory_frame3 = ttk.Label(
            self.frame3,
            text='Path Save as file encrypt..'
        )
        self.label_directory_frame3.pack()

        def search_private_key():
            filename = filedialog.askopenfilename()
            self.label_private_key_frame3.config(text=filename,textvariable=filename)
            if self.label_directory_frame3['textvariable']:
                self.button_private_key_frame3.config(state='enabled')

        self.button_private_key_frame3 = ttk.Button(
            self.frame3,
            text='Select private key...',
            command=search_private_key
        )
        self.button_private_key_frame3.pack()

        self.label_private_key_frame3 = ttk.Label(
            self.frame3,
            text='Path private key...'
        )
        self.label_private_key_frame3.pack()

        self.button_generate_frame3 = ttk.Button(
            self.frame3,
            text='Generate',
            state='disabled'
        ).pack()


if __name__ == '__main__':
    app = MainApp()
    app.mainloop()