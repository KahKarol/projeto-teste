import datetime
import pytz
import os

# Define a hora atual
tz = pytz.timezone('America/Sao_Paulo')
agora = datetime.datetime.now(tz)
data_hora = agora.strftime("%d/%m/%Y às %H:%M:%S")

readme_path = "README.md"
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        linhas = f.readlines()
else:
    linhas = ["# Meu Projeto\n"]

# Atualiza status
nova_linha = f"\n🕒 **Última execução:** {data_hora}\n"

# Verifica se já existe o status para substituir
encontrado = False
for i, linha in enumerate(linhas):
    if "Última execução do pipeline" in linha:
        linhas[i] = nova_linha
        encontrado = True
        break

if not encontrado:
    linhas.append(nova_linha)

# Salva o arquivo
with open(readme_path, "w", encoding="utf-8") as f:
    f.writelines(linhas)