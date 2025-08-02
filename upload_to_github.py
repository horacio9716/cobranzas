import os
import subprocess

# Configurá tu información personal de GitHub
GITHUB_USERNAME = "horacio9716"
REPO_NAME = "cobranzas"
COMMIT_MESSAGE = "subida automática desde Termux"
TOKEN_FILE = os.path.expanduser("~/.git_token")

# Ruta del proyecto local
PROJECT_PATH = os.path.expanduser("~/cobranzas")

# Leer token desde archivo seguro
with open(TOKEN_FILE, "r") as f:
    TOKEN = f.read().strip()

# URL con token embebido
REPO_URL = f"https://{TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"

# Comandos git para subir automáticamente
commands = [
    f"cd {PROJECT_PATH}",
    "git init",
    f"git remote remove origin || true",
    f"git remote add origin {REPO_URL}",
    "git add .",
    f"git commit -m \"{COMMIT_MESSAGE}\"",
    "git branch -M main",
    "git push -u origin main --force"
]

# Ejecutar comandos uno por uno
for cmd in commands:
    print(f"\n>> Ejecutando: {cmd}")
    subprocess.run(cmd, shell=True, check=True)
