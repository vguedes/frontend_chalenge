# Desafio Frontend

## Observações importantes
1. Se organizar para rabalhar até no máximo **6 horas** nesse projeto.

1. Adicione comentários, arquivos, explicações da sua forma de pensar e, principalmente, do que não tiver tempo de implementar.

## Descrição

1. Crie um novo projeto ReactJS usando o comando npx create-react-app my-app (certifique-se de ter o Node.js instalado em sua máquina).

1. Crie um componente de classe chamado "ToDoList" que renderize uma lista de tarefas. Cada tarefa deve ter um título e uma descrição. Integrar com a listagem de Todos da API provida no desafio (ver documentação da API).

1. Crie um componente de classe chamado "AddToDo" que renderize um formulário para adicionar uma nova tarefa à lista. O formulário deve ter campos para o título e a descrição da tarefa.

1. Adicione um botão "Adicionar" ao formulário que, quando clicado, adicionará a nova tarefa à lista. Integrar com a adição de Todos da API provida no desafio (ver documentação da API).

1. Adicione um botão "Excluir" a cada item da lista de tarefas. Quando clicado, ele deve remover a tarefa correspondente da lista. Integrar com a exclusão de Todos da API provida no desafio (ver documentação da API).

1. Adicione a funcionalidade de edição para cada tarefa da lista. Quando um usuário clicar em um item da lista, ele deve ser capaz de editar o título e a descrição da tarefa. Integrar com a edição de Todos da API provida no desafio (ver documentação da API).

1. Adicione a capacidade de marcar uma tarefa como "concluída". Quando uma tarefa é marcada como concluída, ela deve ser exibida de forma diferente (por exemplo, riscada ou com um ícone de marca de seleção). Integrar com a edição de Todos da API provida no desafio (ver documentação da API).

1. Adicione a funcionalidade de filtro para a lista de tarefas. Os usuários devem ser capazes de filtrar as tarefas por título e/ou descrição. A API não tem essa funcionalidade, fazer localmente.

## A API do desafio
### Descrição
1. É uma apicação python que usa Django, DRF e sqlite.
1. Roda em docker (ver diretório).

### Executando
1. Criação do banco
No container executar `./manage.py migrate`
1. Criação de super usuário da aplicação
No container executar `./manage.py createsuperuser`

### Visualiando a documentação da aplicação
- Acessar [http://localhost:8000/api/](http://localhost:8000/api/)
- **Observação:** Ao clicar/acessar http://localhost:8000/api/todos/`, acessa uma página que pode fazer CRUD nos Todos.

## Enviando o desafio
1. Subir em sua conta pessoal o repo clonado do original e compartilhar com o criador do repo do desafio (@vguedes) no Github.
1. Contactar o/a tech recruiter e informar que concluiu o desafio.

## Dúvidas
Contactar o/a tech recruiter,.
