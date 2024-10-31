## pjfinal-proweb-20242
## Curso de Ciências da Computação
# Disciplina Programação WEB
# Professor: Msc Francisco Carlos Lima Pereira
# Início: 31/10/2024
## Descrição da Atividade

Este repositório foi criado como parte de uma atividade da disciplina de **Programação Web** do curso de **Ciência da Computação** na **Universidade Estadual de Roraima (UERR)**. O objetivo da atividade é desenvolver um sistema web utilizando **Python** e **Django**, aplicando boas práticas de desenvolvimento, incluindo versionamento com **Git**, organização de repositório e implementação de funcionalidades essenciais para um sistema web dinâmico.

## Objetivos do Projeto

O projeto visa consolidar o aprendizado nas seguintes áreas:
- **Modelagem de Dados**: Criar e relacionar classes de modelo no Django para estruturar as principais entidades do sistema.
- **Desenvolvimento de Interface**: Criar templates HTML e utilizar o sistema de templates do Django para organizar e estruturar a interface de usuário.
- **Autenticação e Controle de Acesso**: Implementar controle de acesso para restringir funcionalidades a usuários autenticados, utilizando o `@login_required`.
- **Integração com GitHub**: Gerenciar o código-fonte e a colaboração entre membros do grupo com o Git, mantendo o repositório atualizado com commits e sincronizações frequentes.

## Estrutura do Projeto

O projeto segue a estrutura recomendada para projetos Django:

```plaintext
nome_do_projeto/
├── app_name/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── nome_do_projeto/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── README.md
```

## Funcionalidades do Sistema

1. **Modelos e Relacionamentos**: Estruturação de classes de modelo (`Model`) para as entidades principais do sistema.
2. **Administração**: Configuração do Django Admin para gerenciamento de dados do sistema.
3. **Formulários e Templates**: Criação de formulários para interagir com as entidades e templates HTML para exibição dos dados.
4. **Autenticação**: Controle de acesso com login/logout e restrição de acesso a áreas específicas.
5. **Organização de Código**: Manter o repositório estruturado e versionado no GitHub, com commits bem descritos e regulares.

## Aplicativos (Projetos) a Serem Desenvolvidos

Cada grupo desenvolverá um dos seguintes aplicativos, explorando a criação de modelos, templates, formulários, administração e controle de acesso:

1. **Sistema de Biblioteca Online**: Para gerenciamento de livros, autores, alunos e reservas.
2. **Plataforma de Ensino a Distância**: Onde alunos podem se matricular em cursos, acessar aulas e interagir com professores.
3. **Sistema de Gestão de Projetos**: Para organizar tarefas, equipes e progresso dos projetos.
4. **Sistema de Reserva de Salas de Reunião**: Permite o agendamento de salas de reunião por funcionários.
5. **Sistema de Controle Acadêmico**: Para gerenciar informações de notas e frequência dos alunos.
6. **Sistema de Compras e Vendas Online**: Plataforma de e-commerce para gerenciamento de produtos, clientes e pedidos.
7. **Sistema de Gerenciamento de Eventos**: Onde usuários podem criar e gerenciar eventos com convidados.
8. **Sistema de Monitoramento de Veículos**: Controle de entrada e saída de veículos em um estacionamento.
9. **Sistema de Feedback de Produtos**: Para clientes avaliarem e comentarem sobre produtos comprados.
10. **Sistema de Blog com Comentários**: Onde usuários podem criar posts e interagir com comentários.
11. **Sistema de Gerenciamento de Consultório Médico**: Para controle de consultas, pacientes e prontuários médicos.
12. **Sistema de Gerenciamento de Imóveis para Locação**: Para gestão de contratos, imóveis e inquilinos.

## Tecnologias e Ferramentas

Para a implementação do projeto, serão utilizados os seguintes aplicativos e ferramentas:

1. **Django**: Principal framework web em Python, utilizado para gerenciar a estrutura de dados, lógica de negócios e autenticação do sistema.
2. **Django Admin**: Interface de administração integrada ao Django, que facilita o gerenciamento de dados e usuários.
3. **HTML/CSS e Bootstrap**: Para criação dos templates e estilização das páginas, usando o mecanismo de templates do Django para uma interface consistente e responsiva.
4. **Django Forms**: Para criar e gerenciar formulários de forma segura e integrada com os modelos, facilitando as operações CRUD (criar, ler, atualizar, deletar) dos dados do sistema.
5. **VSCode**: Ambiente de desenvolvimento integrado (IDE) para codificação e depuração.
6. **Git e GitHub**: Para controle de versão e colaboração, onde o código será versionado e compartilhado entre os membros do grupo.
7. **SQLite (ou PostgreSQL)**: Banco de dados utilizado para armazenamento e consulta de dados, permitindo testes locais e facilitando a migração para um banco de dados mais robusto em produção, como o PostgreSQL.

## Colaboração

Para colaboração, siga os passos abaixo:
1. Clone o repositório para seu ambiente local.
2. Crie uma nova branch para desenvolver suas alterações.
3. Envie um **Pull Request** para revisão, garantindo que o código esteja atualizado e funcional.
4. Todos os commits devem seguir a boa prática de descrever as alterações realizadas.
