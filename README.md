# Sistema Petshop - API de Gerenciamento de Vacinas

API RESTful para gerenciamento completo de uma clínica veterinária, incluindo cadastro de veterinários, tutores, pets e controle de vacinação.

## Funcionalidades

- **Autenticação JWT**: Sistema completo com tokens armazenados em HTTPOnly cookies
- **Gestão de Usuários**: Cadastro e autenticação de veterinários e tutores
- **Cadastro de Pets**: Registro completo dos animais vinculados aos tutores
- **Controle de Vacinas**: Histórico e registro de vacinação
- **Permissões Granulares**: Diferentes níveis de acesso para veterinários e tutores
- **Documentação Interativa**: Interface Swagger UI integrada

## Tecnologias utilizadas

- **Python 3.14** + **Django 6.0.2**
- **Django REST Framework** - Construção da API
- **SimpleJWT** - Autenticação com tokens JWT em HTTPOnly cookies
- **SQLite** - Banco de dados
- **drf-spectacular** - Documentação automática da API
- **django-environ** - Gerenciamento de variáveis de ambiente
- **django-debug-toolbar** - Monitoramento e otimização de queries

## Instalação

### Pré-requisitos
- Python 3.12 ou superior
- pip

### Passo a passo

1. Clone o repositório
   ```
   git clone https://github.com/viniciuseugenio/sistema-petshop.git
   cd sistema-petshop
   ```

2. Crie o ambiente virtual
   
   Linux/Mac:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
   
   Windows:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instale as dependências
   ```
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente
   ```
   cp .env-example .env
   ```
   Edite o arquivo `.env` com suas configurações

5. Execute as migrations
   ```
   python manage.py migrate
   ```

6. Crie um superusuário
   ```
   python manage.py createsuperuser
   ```

7. Inicie o servidor
   ```
   python manage.py runserver
   ```

A API estará disponível em `http://localhost:8000`

## Documentação

Para acessar a documentação completa e interativa da API, acesse o endpoint:
- **Swagger UI**: `http://localhost:8000/api/schema/swagger-ui/`
- **Arquivo OpenAPI**: `schema.yml` (raiz do projeto)

## Estrutura do Projeto

```
sistema-petshop/
├── apps/
│   ├── accounts/       # Autenticação e gerenciamento de usuários
│   ├── veterinarios/   # Gestão de veterinários
│   ├── tutores/        # Gestão de tutores
│   ├── pets/           # Cadastro de animais
│   ├── vacinas/        # Controle de vacinação
│   ├── permissions.py  # Permissões customizadas
│   └── utils.py        # Utilitários compartilhados
├── CORE/               # Configurações do Django
├── manage.py
├── requirements.txt
└── schema.yml
```

## Sistema de Permissões

A API implementa um modelo baseado em roles:

- **Tutores**: Podem visualizar dados dos próprios pets e histórico de vacinas (somente leitura)
- **Veterinários**: Podem criar e gerenciar pets, tutores e registros de vacinação
- **Admin**: Acesso total ao sistema

## Decisões Técnicas

### Arquitetura
- Separação em apps Django para melhor organização e manutenibilidade
- Uso de `select_related()` para otimização de queries
- Models Tutor e Veterinário com relação OneToOne ao User padrão do Django

### Segurança
- Tokens JWT armazenados em HTTPOnly cookies para proteção contra ataques como XSS
- Permissões customizadas para controle granular de acesso
- Variáveis de ambiente para dados sensíveis

### Documentação
- Exemplos completos em todos os endpoints
- Schemas OpenAPI para importação em ferramentas como Postman
- Descrições detalhadas na interface Swagger
