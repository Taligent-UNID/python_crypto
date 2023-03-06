import typer
from app.rsa_encryption import *
from pathlib import Path
from typing  import Optional

app = typer.Typer()

# Hola mundo

@app.command()
def new_keys(src: Optional[str] = typer.Option(None,prompt="Nombre de Carpeta ['/credentials']")):
    home = str(Path.home())
    if src is None:
        src = '/credentials'
        filepath = Path(home + src)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        create_pair_keys(filepath)
    elif src.is_dir():
        src = '/credentials'
        filename = home + src
        create_pair_keys(filename)


@app.command()
def encrypt(user_name: str):
    print(f"Deleting user: {user_name}")

@app.command()
def decrypt(user_name: str):
    print(f"Deleting user: {user_name}")

@app.command()
def generate():
    print('New Password Generated : ', generate_password())

if __name__ == "__main__":
    app()