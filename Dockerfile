# Escolha a imagem base (uma imagem Python oficial)
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /App

# Copie o restante do código do seu projeto para o diretório de trabalho
COPY brute_force.py .

# Defina o comando de execução do seu script
CMD ["python", "./brute_force.py"]
