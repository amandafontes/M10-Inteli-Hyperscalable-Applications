<h2>Atividade Prática | EC-M10-P1</h2>

O presente diretório destina-se à entrega da atividade prática referente à primeira prova do módulo 10 de Engenharia da Computação.

<h3>Descrição da Atividade</h3>

Para a questão prática da avaliação, você deve entregar uma API de nível de maturidade 2 no Modelo de Maturidade de Richardson, escrita em Python.
Você deve criar um dois recursos permitam ao usuário realizar um cadastro de um pedido. Esse pedido deve possuir o nome do usuário, o e-mail do usuário e a descrição do pedido. Ele deve ser enviado como um JSON. 

O seu sistema deve fornecer, no mínimo, as seguintes rotas:

- /novo: cadastrar um novo pedido. Recebe um JSON e retorna um ID.

- /pedidos: retorna todos os pedidos cadastrados.

- /pedidos/<id>: retorna o pedido do ID fornecido. Se esse pedido não existir, retornar que não foi possível locallizar ele, da forma mais apropriada para atender as questões do problema proposto.
  
**Requisitos:**

1. O recurso /pedidos/<id> ainda deve possibilitar editar o pedido e excluir ele, implementados em recursos distintos.

2. Nenhuma interface gráfica deve ser implementada, apenas as rotas. Elas devem ser testadas utilizando collections do Insomnia. Essas coleções devem ser exportadas no repositório.

3. A solução deve ser dockerizada.

4. Não existe a necessidade de armazenar as requisições em disco, pode ser utilizado apenas memória.

<h3>Implementação</h3>

Para a implementação da atividade, foi desenvolvida uma API em Python utilizando o framework Flask, um banco de dados SQLite e o SQLAlchemy como ORM. Foi criada uma classe <code>Pedido</code> para a modelagem do banco de dados responsável por receber os dados enviados pelo usuário. Além disso, utilizando o mecanismo de autenticação HTTP básica do Flask, foi implementada a verificação de usuário para acesso às rotas. A rota inicial <code>/</code> solicita que o usuário acesse a rota <code>/novo</code> para cadastrar um novo pedido, a rota <code>/pedidos</code> para consultar os pedidos existentes e a rota <code>/pedidos/{id}</code> para consultar as informações relacionadas a um pedido específico. Posteriormente, são implementadas, em diferentes funções, as rotas correspondentes às operações de CRUD. Na aplicação, é possível consultar, criar, atualizar e deletar os pedidos realizados. No último bloco de código, a aplicação é inicializada, de forma que o sistema crie o banco de dados e se mantenha em execução.

Além disso, foi criado um Dockerfile para que a API pudesse ser executada por meio de uma imagem Docker.

O mecanismo de autenticação de usuário, assim como todas as rotas do sistema, foram verificados e testados por meio do Insomnia. As collections correspondentes podem ser consultadas no arquivo <code>insomnia-collections.yaml</code>.

<h3>Execução</h3>

Para executar a aplicação, deverão ser seguidos os procedimentos descritos abaixo. Os comandos consideram a utilização de uma distribuição de Linux.

Primeiramente, clone o repositório e acesse o diretório correspondente à atividade prática da prova:

```shell
git clone https://github.com/amandafontes/M10-Inteli-Hyperscalable-Applications.git

cd ponderada1/src
```

Posteriormente, será necessário criar um ambiente virtual para a instalação das bibliotecas utilizadas.

```shell
python3 -m venv venv

source venv/bin/activate
```

O próximo passo é instalar os requirements:

```shell
pip install -r requirements.txt
```

Por fim, execute o comando correspondente à API:

```shell
python3 app.py
```

Desse modo, será possível conferir o script da API em execução. Você poderá testar suas rotas no Insomnia ou em ferramentas semelhantes.

Para executar a solução dockerizada, basta utilizar os comandos descritos abaixo:

Após clonar o repositório e acessar o diretório em que se encontra o código-fonte da solução, construa a imagem Docker:

```shell
docker build -t api .
```

Por fim, para executar a imagem:

```shell
docker run -p 5000:5000 api
```

<h3>Estrutura de Pastas</h3>

O diretório <code>src</code>, responsável por armazenar o código-fonte da solução, contempla os seguintes arquivos:

- **instance/pedidos.db:** banco de dados da API;
- **venv:** ambiente virtual que deverá ser criado para a instalação das bibliotecas e módulos necessários;
- **app.py:** script Python correspondente à API desenvolvida;
- **Dockerfile:** script correspondente à imagem criada para a dockerização da API;
- **insomnia-collections.yaml:** collections do Insomnia para teste das operações de CRUD da API;
- **requirements.txt:** arquivo de texto com as bibliotecas e módulos a serem instalados para o funcionamento da API.