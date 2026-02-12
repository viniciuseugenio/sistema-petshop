# Eugepet - Sistema de Vacinas

Uma API RESTful onde você pode gerenciar veterinários, tutores, pets e vacinas. A aplicação contem um sistema completo de autentição por meio de JWT tokens, que são armazenados por meio de HTTPOnly cookies. Além disso, a API tem endpoints para criação, listagem, deletaçao e atualização de todos os models, com sistema de permissões para acessá-las.

## Tecnologias utilizadas
- Python 3.14 + Django REST Framework
- SimpleJWT com views customizadas para armazenar os tokens em HTTPOnly cookies
- Banco de dados nativo do Django, que é o SQLite
- drf-spectacular para documentação da API
- django-environ para manuseamento das variáveis de ambiente

## Instruções para rodar na sua máquina
1. Faça a clonagem do repositório
   ```
   bash
   git clone https://github.com/viniciuseugenio/sistema-petshop.git
   cd sistema-petshop
   ```
   
2. Crie e ative o ambiente virtual
   ```
   bash
   python -m venv venv
   source venv/bin/activate (venv\Scripts\Activate no Windows)
   ```
   
3. Instale as dependências
   ```
   bash
   pip install -r requirements.txt
   ```
   
4. Configure as variáveis de ambiente
   - Copie o .env-example para um novo file .env e insira os valores corretos.

5. Rode as migrations
   ```
   bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   
6. Crie o seu superuser
   ```
   bash
   python manage.py createsuperuser
   ```
   
7. E por fim, rode o servidor
   ```
   python manage.py runserver
   ```

   Ao rodar o servidor, toda a documentação da API estará em /api/schema/swagger-ui/, ou caso prefira, veja a collection no Postman: https://viniciuseugeniovhe-2734122.postman.co/workspace/Vin%C3%ADcius-Eug%C3%AAnio's-Workspace~aa81761c-ebb1-4277-8306-02d21e1f30aa/collection/48728992-fad475ea-51d2-4f5c-ad18-1ae07c592241?action=share&source=copy-link&creator=48728992
