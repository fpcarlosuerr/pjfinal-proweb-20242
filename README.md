# pjfinal-proweb-20242
# Curso de Ciências da Computação
# Disciplina Programação WEB
# Professor: Msc Francisco Carlos Lima Pereira

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
