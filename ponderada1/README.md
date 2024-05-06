<h2>Atividade 1 | Desenvolvimento de API de gerenciamento de tarefas</h2>

O presente diretório é destinado à entrega da atividade referente à criação de uma API síncrona com nível de maturidade 2. Ela deve ser capaz de fazer a autenticação do usuário e permitir que ele crie, leia, atualize e delete tarefas.

<h2>Implementação</h2>

Primeiramente, foi desenvolvido um script <code>main.py</code> utilizando Flask, um framework de desenvolvimento web em Python. O código representa uma API síncrona com duas possíveis rotas, das quais uma permite a autenticação de usuário, bem como a realização das operações de CRUD.

Posteriormente à importação das bibliotecas e módulos necessários, a aplicação Flask é instanciada, assim como um banco de dados SQLite, que utiliza o framework SQLAlchemy como ORM. Além disso, é apresentada a extensão do Flask que fornece suporte para autenticação HTTP.

A classe <code>Task</code> define o modelo de dados para uma tarefa, que possui os atributos <i>id</i>, <i>título</i>, <i>descrição</i> e o campo booleano <i>done</i>. O dicionário <code>users</code>, por outro lado, apresenta um exemplo de credenciais para autenticação de usuário, uma vez que esse processo será necessário para o acesso à rota de operações com tarefas.

Por fim, são definidas as rotas da aplicação. A rota <code>/</code> apresenta uma mensagem inicial solicitando que seja acessada a rota <code>tasks</code> para que seja realizada a autenticação do usuário e para que sejam consultadas as tarefas da lista. Também é possível, por meio da rota, realizar as operações de CRUD: leitura, adição, atualização e deleção de tarefas. Tais operações são definidas nas rotas posteriores, de modo que todas solicitem a autenticação por meio do método <code>@auth.login_required</code>. Para todos os casos, são inseridos os status codes correspondentes para quando a operação não for bem-sucedida, indicando que a API criada possui nível de maturidade 2.

<h3>Insomnia Collection</h3>

A fim de testar a autenticação de usuário e as operações de CRUD, a API foi testada por meio do Insomnia, uma aplicação de cliente REST que simplifica o processo de teste e depuração de APIs. Com a finalidade de manter registro dos testes, encontra-se no presente diretório a collection correspondente, a qual pode ser acessada por meio do arquivo <code>insomnia-collection.json</code> ou <code>insomnia-collection.yaml</code>.

<h3>Documentação OpenAPI</h3>

A fim de documentar a API, foi utilizada a estrutura do Swagger. A documentação encontrada em <code>swagger.yaml</code> descreve todas as operações disponíveis na API, incluindo detalhes sobre os endpoints, os parâmetros necessários, os códigos de resposta e os modelos de dados utilizados.

<h3>Dockerização</h3>

A API desenvolvida, bem como suas dependências, foram encapsuladas em um container Docker. Para isso, foi criada uma <code>Dockerfile</code> na raiz do projeto, a qual contém todas as instruções necessárias para construir a imagem da aplicação.

<h2>Execução</h2>

Para executar o projeto, será necessário realizar o download do código-fonte da aplicação, contido no diretório <code>src</code>. Posteriormente, será necessário construir a imagem Docker:

```bash
docker build -t api .
```

Por fim, você poderá executar um container com a aplicação por meio do seguinte comando:

```bash
docker run -p 5000:5000 api
```