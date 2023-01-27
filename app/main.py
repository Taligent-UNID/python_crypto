import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as mb
from rsa_encryption import create_pair_keys


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
        )
        self.label_frame1.pack()

        def filename_path():
            filename = filedialog.askdirectory()
            if filename:
                self.label_directory_frame1.config(text=filename)
                self.button_generate_frame1.config(state='enabled')
                self.filename = filename

        self.button_directory_frame1 = ttk.Button(
            self.frame1,
            text='Select Directory..',
            command=filename_path
        )
        self.button_directory_frame1.pack()

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
        )
        self.button_generate_frame1.pack()

        # Frame 2 
        
        
        
        

        
        
        
        
        
        

        
        
        
        
        

        
        
        

        
        
        
        
        
        

        
        
        
        





if __name__ == '__main__':
    app = MainApp()
    app.mainloop()