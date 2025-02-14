import os
import subprocess
import sys

def run_command(command):
    """Executa um comando no terminal."""
    try:
        print(f"Executando: {command}")
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar comando: {e}")
        print(e.stderr)
        sys.exit(1)

def install_dependencies():
    """Instala as dependências necessárias."""
    print("📦 Atualizando sistema e instalando dependências básicas...")
    run_command("pkg update -y && pkg upgrade -y")
    run_command("pkg install git nodejs npm python -y")

def clone_repository(repo_url, folder_name):
    """Clona o repositório do bot."""
    print(f"📂 Clonando repositório: {repo_url}")
    if not os.path.exists(folder_name):
        run_command(f"git clone {repo_url} {folder_name}")
    else:
        print(f"A pasta '{folder_name}' já existe. Pulando clonagem.")
    os.chdir(folder_name)

def install_node_dependencies():
    """Instala as dependências do projeto Node.js."""
    print("⬇️ Instalando dependências do projeto Node.js...")
    run_command("npm install")

def create_env_file():
    """Cria o arquivo .env com placeholders."""
    env_content = """TELEGRAM_BOT_TOKEN=SEU_TOKEN_TELEGRAM
GITHUB_TOKEN=SEU_TOKEN_GITHUB
REPO_OWNER=SEU_NOME_DE_USUARIO_GITHUB
REPO_NAME=NOME_DO_REPOSITORIO
"""
    print("📝 Criando arquivo .env...")
    with open(".env", "w") as env_file:
        env_file.write(env_content)
    print("✅ Arquivo .env criado! Substitua os valores pelas suas credenciais.")

def start_bot():
    """Inicia o bot."""
    print("🚀 Iniciando o bot...")
    run_command("node index.js")

def main():
    # URL do repositório
    repo_url = "https://github.com/leticiasafu/Whbotmyrepo.git"
    folder_name = "whatsapp-bot"

    # Passo 1: Instalar dependências
    install_dependencies()

    # Passo 2: Clonar o repositório
    clone_repository(repo_url, folder_name)

    # Passo 3: Instalar dependências do Node.js
    install_node_dependencies()

    # Passo 4: Criar arquivo .env
    create_env_file()

    # Passo 5: Iniciar o bot
    start_bot()

if __name__ == "__main__":
    main()
