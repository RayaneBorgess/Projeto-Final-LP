### README.md

# Sistema de Gestão de Notas Escolares

Este projeto consiste no desenvolvimento de um sistema de gestão de notas escolares utilizando Python e a biblioteca FastAPI. O objetivo principal é permitir que professores registrem as notas dos alunos e realizem consultas sobre seus desempenhos.

## Estrutura do Projeto

A estrutura do projeto foi organizada da seguinte forma:

```
.
├── dados
│   └── db.py
├── modelos
│   ├── aluno.py
│   └── nota.py
├── roteadores
│   ├── alunos.py
│   └── notas.py
├── validacoes
│   └── aluno.py
├── main.py
└── README.md
```

### Decisões de Estrutura de Arquivos

- **dados/db.py**: Este arquivo contém funções para ler e salvar dados dos alunos em um arquivo JSON. A escolha de usar um arquivo JSON em vez de um banco de dados foi feita para simplificar o desenvolvimento inicial, permitindo persistência de dados sem a necessidade de configuração de um banco de dados.

- **modelos/aluno.py** e **modelos/nota.py**: Esses arquivos definem as classes `Aluno` e `Nota`, respectivamente. A separação em arquivos distintos facilita a manutenção e o entendimento do código, além de promover a modularização.

- **roteadores/alunos.py** e **roteadores/notas.py**: Esses arquivos definem os endpoints da API relacionados aos alunos e às notas. A separação em diferentes roteadores permite uma melhor organização e escalabilidade do código, facilitando a adição de novos endpoints no futuro.

- **validacoes/aluno.py**: Este arquivo contém funções de validação para garantir que os dados dos alunos estejam corretos antes de serem persistidos. A separação das validações em um arquivo específico ajuda a manter o código limpo e organizado.

- **main.py**: Arquivo principal que inicializa a aplicação FastAPI e inclui os roteadores.

### Pacotes Utilizados

- **FastAPI**: Escolhemos FastAPI por ser uma biblioteca moderna e rápida para a construção de APIs com Python. Ela facilita a criação de endpoints, a validação de dados e a documentação automática da API.

- **Uvicorn**: Uvicorn é um servidor ASGI de alto desempenho, usado para executar aplicações FastAPI. Ele é essencial para o desenvolvimento e a implantação de aplicações web assíncronas.

### Uso de UUID

Optamos por usar UUIDs (Identificadores Universalmente Únicos) para os IDs dos alunos. Isso garante que cada aluno tenha um identificador único, reduzindo a chance de colisões de IDs e simplificando a gestão dos dados. UUIDs são especialmente úteis em sistemas distribuídos onde a geração de IDs únicos deve ser garantida sem coordenação central.

### Decisões de Projeto

- **Persistência de Dados em JSON**: Escolhemos usar arquivos JSON para persistir os dados dos alunos. Essa decisão simplifica o armazenamento e a leitura dos dados, evitando a complexidade de configurar e gerenciar um banco de dados relacional ou NoSQL.

- **Arredondamento de Notas**: As notas dos alunos são arredondadas para uma casa decimal para padronizar a apresentação dos dados e evitar problemas com precisão numérica.

- **Validação de Dados**: Implementamos validações para garantir que todas as disciplinas tenham notas e que essas notas estejam no intervalo correto (0 a 10). Isso evita a inserção de dados inconsistentes no sistema.

Esta estrutura modular e organizada do projeto facilita a manutenção, a escalabilidade e a adição de novas funcionalidades no futuro, garantindo um código limpo e de fácil entendimento.