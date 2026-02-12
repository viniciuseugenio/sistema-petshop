# Sistema de Vacinas - Petshop

Uma API RESTful onde você pode gerenciar veterinários, tutores, pets e vacinas. A aplicação contem um sistema completo de autentição por meio de JWT tokens, que são armazenados por meio de HTTPOnly cookies. Além disso, a API tem endpoints para criação, listagem, deletaçao e atualização de todos os models, com sistema de permissões para acessá-las.

## Tecnologias utilizadas
- Python 3.14 + Django REST Framework
- djangorestframework-simple_jwt com views customizadas para armazenar os tokens em HTTPOnly cookies
- Banco de dados nativo do Django, que é o SQLite
- drf-spectacular para documentação da API
- django-environ para manuseamento das variáveis de ambiente
- django-debug-toolbar para visualizar quais queries precisam de otimização

## Instruções para rodar na sua máquina
1. Faça a clonagem do repositório
   ```
   git clone https://github.com/viniciuseugenio/sistema-petshop.git (ou utilize SSH)
   cd sistema-petshop
   ```
   
2. Crie e ative o ambiente virtual
   
   Para Linux:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
   Para Windows:
   ```
   python -m venv venv
   venv\Scripts\active
   ```
   
4. Instale as dependências
   ```
   pip install -r requirements.txt
   ```
   
5. Configure as variáveis de ambiente
   - Copie o .env-example para um novo arquivo .env e insira os valores corretos.

6. Rode as migrations
   ```
   python manage.py migrate
   ```
   
7. Crie o seu superuser
   ```
   python manage.py createsuperuser
   ```
   
8. E por fim, rode o servidor
   ```
   python manage.py runserver
   ```

   Ao rodar o servidor, toda a documentação da API estará em /api/schema/swagger-ui/, ou, caso prefira, o arquivo `schema.yml` está no root do projeto e você pode usá-lo no seu aplicativo de preferência.
   

## Breve explicação de decisões técnicas
- Para facilitar a leitura e visualização do código e das suas funcionalidades, resolvi separar as funcionalidades de pet, veterinário, tutor e vacinas em apps diferentes e colocá-los dentro de uma pasta `apps/` que os armazena, para que a base da pasta não fique muito poluida com as pastas dos apps. 
- Para não ter muita complexidade neste projeto, optei por deixar o model de User como o padrão do Django, mas criar ambos os modelos de Veterinario e Tutor, que tem como campo OneToOne, o User. Os dois modelos tem apenas um campo adicional, que é o celular, mas poderiamos adicionar mais campos, como CPF, CRMV (específico do veterinário), endereço, e outros.
- Para o sistema de autenticação, tenho como padrão em meus projetos utilizar JWT tokens que são armazenados em HTTPOnly cookies, pois essa configuração garante mais segurança ao website, evitando ataques como XSS.
Criei diversas permissões customizadas, que podem ser vistas em `permissions.py`.
- A maneira como as permissões estão estruturadas são baseadas na seguinte imaginação: Temos uma clínica veterinária, e o tutor tem acesso aos registros dos seus pets e das vacinas que foram aplicadas neles. Ele tem permissão somente para visualizar, mas não editar dados. O veterinário fica responsável pela criação do pet, do tutor, e de fazer os registros de vacina.
- Para otimizar as queries, utilizei sempre o `.select_related()`, já que as relações são de um para um, sempre.
- A documentação da API tem todos os examples para que não haja confusão na hora de testar os endpoints. Apenas importe o .yml para o Postman, por exemplo, e o esqueleto do body está preenchido. No Swagger UI, as endpoints possuem uma descrição para facilitar a compreensão de quem está vendo. Também configurei uma extension para que fique explicito que a autenticação é por meio de HTTPOnly cookies.
