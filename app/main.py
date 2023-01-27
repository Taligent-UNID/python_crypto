import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as mb
from rsa_encryption import create_pair_keys,generate_password,encrypt_password,decrypt_password
import pyperclip as pc
from pathlib import Path

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # UI options
        paddings = {'padx': 5, 'pady': 10}
        padTitles = {'padx': 10,'pady': 5}
        padButtons = {'padx': 2,'pady':2}

        # configure the root window
        self.title('Secure Delivery of Credentials - Taligent')
        self.config(bg='white')
        self.iconbitmap('app/images/taligent.ico')
        self.resizable(False, False) 
        window_height = 500
        window_width = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        
        # layout all of the main containers
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
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
            background='white'
        )
        self.style.configure(
            'Subheadings.TLabel',
            font=('Roboto 11'),
            background='white'
        )
        # Style Frames
        self.style.configure(
            'TFrame',
            background='white'
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
        self.frame1.config(width=250,height=250)
        self.frame1.grid(row=1,column=0,sticky='ne')

        self.label_frame1 = ttk.Label(
            self.frame1,
            text='Generate Key Pair',
            style='Headings.TLabel'
        ).pack(**padTitles)

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
        ).pack(**padButtons)

        self.label_directory_frame1 = ttk.Label(
            self.frame1,
            text='Path Save As Keys..',
            style='Subheadings.TLabel'
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
        )
        self.button_generate_frame1.pack(**padButtons)

        # Frame 2 Generate Password Random
        self.frame2 = ttk.Frame(self)
        self.frame2.config(width=250,height=250)
        self.frame2.grid(row=1,column=1,sticky='nw')

        self.title_frame2 = ttk.Label(
            self.frame2,
            text='Generate Password Random',
            style='Headings.TLabel'
        ).pack(**padTitles)

        self.label_password_frame2 = ttk.Label(
            self.frame2,
            text='Password generated random...',
            style='Subheadings.TLabel'
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
        ).pack(**padButtons)

        self.label_password_frame2.pack()

        self.button_copy_pass_frame2 = ttk.Button(
            self.frame2,
            text='Copy',
            command=lambda: pc.copy(self.label_password_frame2['text'])
        ).pack(**padButtons)
    
        # Frame 3 Encrypt Password
        self.frame3 = ttk.Frame(self)
        self.frame3.config(width=250,height=250)
        self.frame3.grid(row=2,column=0,sticky='se')

        self.title_frame3 = ttk.Label(
            self.frame3,
            text='Generate File Encrypt',
            style='Headings.TLabel'
        ).pack(side='top',anchor='n',**padTitles)

        def filename_path_frame3():
            filename = filedialog.askdirectory()
            if filename:
                self.label_directory_frame3.config(text=filename)
                self.filename = filename

        self.button_directory_frame3 = ttk.Button(
            self.frame3,
            text='Save file encrypt..',
            command=filename_path_frame3
        ).pack(side='top',**padButtons)

        self.label_directory_frame3 = ttk.Label(
            self.frame3,
            text='Path Save as file encrypt..',
            style='Subheadings.TLabel'
        )
        self.label_directory_frame3.pack(side='top')

        def search_public_key():
            filename = filedialog.askopenfilename()
            self.label_public_key_frame3.config(text=filename)

        self.button_public_key_frame3 = ttk.Button(
            self.frame3,
            text='Select public key...',
            command=search_public_key
        )
        self.button_public_key_frame3.pack(side='top',**padButtons)

        self.label_public_key_frame3 = ttk.Label(
            self.frame3,
            text='Path public key...',
            style='Subheadings.TLabel'
        )
        self.label_public_key_frame3.pack(side='top')

        def temp_text(e):
            self.entry_password_frame3.delete(0,"end")

        self.entry_password_frame3 = ttk.Entry(
            self.frame3,
            width=30
        )
        self.entry_password_frame3.pack(side='top')
        self.entry_password_frame3.insert(0, "Password...")
        self.entry_password_frame3.bind("<FocusIn>", temp_text)

        def generated_file_encrypt():
            validate = []
            self.label_directory_frame3['text'] = self.label_directory_frame3['text'].replace('/','\\')
            if str(Path.home()) not in str(self.label_directory_frame3['text']):
                mb.showerror('SDC','Seleccionar carpeta de guardado de archivo encriptado')
            else:
                validate.append(True)
            if 'public_key.pem' not in self.label_public_key_frame3['text']:
                mb.showerror('SDC','Falta clave publica')
            else:
                validate.append(True)
            if len(self.entry_password_frame3.get()) < 20:
                mb.showerror('SDC','Contraseña muy corta')
            else:
                validate.append(True)
            if len(validate) == 3:
                encrypt_password(
                    self.label_public_key_frame3['text'],
                    bytes(self.entry_password_frame3.get(),'UTF-8'),
                    self.label_directory_frame3['text']
                )
                mb.showinfo('SDC','Archivo encriptado generado')
                self.label_public_key_frame3.config(text='Path public key...')
                self.entry_password_frame3.delete(0,'')
                self.entry_password_frame3.insert(0,'Password...')
                self.label_directory_frame3.config(text='Path Save as file encrypt..')
                validate = []

        self.button_generate_frame3 = ttk.Button(
            self.frame3,
            text='Generate',
            command=generated_file_encrypt
        )
        self.button_generate_frame3.pack(side='top',**padButtons)

        # Frame 4 Decrypt File
        self.frame4 = ttk.Frame(self)
        self.frame4.config(width=250,height=250)
        self.frame4.grid(row=2,column=1,sticky='sw')
        self.title_frame4 = ttk.Label(
            self.frame4,
            text='Generate Decrypt Password',
            style='Headings.TLabel'
        ).pack(side='top',**padTitles)

        def filename_path_frame4():
            filename = filedialog.askopenfilename()
            if filename:
                self.label_directory_frame4.config(text=filename)
                self.filename = filename

        self.button_directory_frame4 = ttk.Button(
            self.frame4,
            text='Open file encrypt..',
            command=filename_path_frame4
        ).pack(**padButtons)

        self.label_directory_frame4 = ttk.Label(
            self.frame4,
            text='Path file encrypt..',
            style='Subheadings.TLabel'
        )
        self.label_directory_frame4.pack()

        def search_private_key():
            filename = filedialog.askopenfilename()
            self.label_private_key_frame4.config(text=filename)

        self.button_private_key_frame4 = ttk.Button(
            self.frame4,
            text='Select private key...',
            command=search_private_key
        ).pack(**padButtons)

        self.label_private_key_frame4 = ttk.Label(
            self.frame4,
            text='Path private key...',
            style='Subheadings.TLabel'
        )
        self.label_private_key_frame4.pack()

        self.label_password_frame4 = ttk.Label(
            self.frame4,
            text='Password decrypt...',
            style='Subheadings.TLabel'
        )
        def generate_decrypt_password():
            validate = []
            if 'file_encrypted.txt' not in str(self.label_directory_frame4['text']):
                mb.showerror('SDC','Falta archivo encriptado')
            else:
                validate.append(True)
            if 'private_key.pem' not in self.label_private_key_frame4['text']:
                mb.showerror('SDC','Falta clave privada')
            else:
                validate.append(True)
            if len(validate) == 2:
                decrypted = decrypt_password(
                    self.label_private_key_frame4['text'],
                    self.label_directory_frame4['text']
                )
                self.label_password_frame4.config(text=decrypted)
                pc.copy(decrypted.decode('utf-8'))
                mb.showinfo('SDC','Password desencriptada y copiada...')
                self.label_directory_frame4.config(text='Path file encrypt..')
                self.label_private_key_frame4.config(text='Path private key...')
                validate = []

        self.button_generate_pass_frame4 = ttk.Button(
            self.frame4,
            text='Generate',
            command=generate_decrypt_password
        ).pack(**padButtons)
        self.label_password_frame4.pack()

        self.button_copy_pass_frame4 = ttk.Button(
            self.frame4,
            text='Copy',
            command=lambda: pc.copy(self.label_password_frame4['text'])
        ).pack(**padButtons)

if __name__ == '__main__':
    app = MainApp()
    app.mainloop()