@echo off
echo Parando o container...
docker stop roblab-instancia
echo Removendo container antigo...
docker rm roblab-instancia
echo Removendo imagem antiga...
docker rmi roblab-brain
echo Construindo nova imagem (Sem Cache)...
docker build --no-cache -t roblab-brain .
echo Subindo o novo container com VOLUME...
docker run -d --name roblab-instancia -v "%cd%:/app" roblab-brain
echo Processo concluido! O RobLab esta atualizado.
pause

-----------------


# 1. Para e remove o container atual
docker stop roblab-instancia
docker rm roblab-instancia

# 2. Remove a imagem antiga para garantir que o novo app.py seja lido
docker rmi roblab-brain

# 3. Build limpo
docker build --no-cache -t roblab-brain .

# 4. Sobe com o Volume (Use aspas para evitar erro de caminho)
docker run -d --name roblab-instancia -v "C:\DevEnv\MVP-RobLAb:/app" roblab-brain