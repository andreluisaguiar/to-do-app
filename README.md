# To-Do App

## Sumário

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
  - [Usuário Comum](#usuário-comum)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura das Telas](#estrutura-das-telas)
- [Configuração e Execução](#configuração-e-execução)
  - [Clonando o Repositório](#clonando-o-repositório)
  - [Criando e Ativando o Ambiente Virtual](#criando-e-ativando-o-ambiente-virtual)
  - [Instalando Dependências](#instalando-dependências)
  - [Configurando Variáveis de Ambiente](#configurando-variáveis-de-ambiente)
  - [Executando a Aplicação](#executando-a-aplicação)
- [Capturas de Tela](#capturas-de-tela)
- [Licença](#licença)

---

## Descrição

O **To-Do App** é um gerenciador de tarefas desenvolvido com Flask, que permite aos usuários criar, visualizar, editar e excluir tarefas de forma simples e eficiente. Usuários autenticados podem organizar suas tarefas em categorias e marcar tarefas como concluídas. Usuários administradores podem gerenciar todas as tarefas e usuários do sistema.

---

## Funcionalidades

### Usuário Comum

- Cadastro de novo usuário
- Login e logout
- Criação de tarefas
- Visualização de tarefas
- Exclusão de tarefas
- Marcar tarefas como concluídas ou pendentes

---

## Tecnologias Utilizadas

- **Back-end:** Flask, Flask-Login, Flask-SQLAlchemy, Flask-Migrate, Flask-Bcrypt
- **Front-end:** Jinja, HTML, CSS, Bootstrap 
- **Banco de Dados:** PostgreSQL (produção)

---

## Estrutura das Telas

- **Tela de Boas-Vindas:** Mensagem inicial e redirecionamento para cadastro/login
- **Tela de Cadastro:** Registro de novos usuários
- **Tela de Login:** Autenticação de usuários
- **Tela Principal/Home:** Listagem de tarefas do usuário

---
## Configuração e Execução

### Clonando o Repositório

```bash
git clone https://github.com/andreluisaguiar/to-do-app.git
cd to-do-app
```

### Criando e Ativando o Ambiente Virtual

#### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Instalando Dependências

```bash
pip install -r requirements.txt
```

### Configurando Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
SECRET_KEY=sua_chave_secreta_aqui
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
```

Substitua os valores conforme sua configuração local.

### Executando a Aplicação

```bash
flask db upgrade  # Executa as migrações do banco de dados
flask run         # Inicia o servidor Flask
```
A aplicação estará acessível em [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Capturas de Tela

> Adicione imagens das principais telas do sistema, por exemplo:

- **Tela Inicial**  
  ![Tela Principal](./app/static/images/tela_inicial.png)

- **Tela de Cadastro**  
  ![Tela Principal](./app/static/images/registro.png)

- **Tela de Login**  
  ![Tela de Login](./app/static/images/login.png)

- **Tela Principal**  
  ![Tela Principal](./app/static/images/dashboard1.png)
  ![Tela Principal](./app/static/images/dashboard2.png)

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).