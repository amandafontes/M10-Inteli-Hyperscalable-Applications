<h2>Prova 02 | Implementação de Sistema de Logs</h2>

<p>A atividade prática correspondente à segunda prova do módulo caracteriza-se pela implementação de um sistema de logs em uma API previamente fornecida, a qual deve ser ajustada para atender aos requisitos da atividade. Devem ser desenvolvidos os seguintes elementos:</p>

<li>Realizar a adequação do projeto desenvolvido em Flask para FastAPI.
<li>Adicionar o log em todas as rotas do sistema. O log deve ficar armazenado em um arquivo. Logar apenas informações de nível WARNING em diante.
<li>Implementar o sistema em um container docker
<li>Adicionar um container com um Gateway utilizando NGINX para o sistema
<li>Criar um arquivo docker-compose que permita executar toda a aplicação
<li>Implementar os testes da API com Insomnia

<h3>Implementação</h3>

Para a implementação da atividade, foi, primeiramente, criado um ambiente virtual Python para a instalação das dependências necessárias. As dependências do projeto encontram-se listadas no arquivo <code>requirements.txt</code>.

Os comandos utilizados estão adaptados para o contexto de uso do Ubuntu, em especial o terminal Zsh.

```zsh
python3 -m venv venv
source venv/bin/activate
pip install 'fastapi[all]' uvicorn
pip freeze > requirements.txt
```

Posteriormente a esse processo, o código correspondente à API foi replicado no arquivo <code>main.py</code> e adaptado para o FastAPI, ganhando caráter de API assíncrona. O próximo passo foi adicionar, ao diretório raiz do projeto, o arquivo <code>logs.py</code>, responsável por configurar o sistema de logs da aplicação. Nesse arquivo, foi possível configurar o nível das mensagens de logging, bem como o formato da mensagem gerada. No script principal, foi importado o módulo <code>logging</code>.

Posteriormente, o logger foi ajustado para que pudesse ser configurado por um arquivo externo. Desse modo, foi adicionado o arquivo <code>logging_config.py</code>, também no diretório raiz da atividade. Retomando o arquivo <code>main.py</code>, ele foi ajustado para que passasse a contemplar o logger raiz. Por fim, foi possível adicionar logs nas rotas utilizando <code>LOGGER.info()</code>.

Uma vez adicionados os logs às rotas da API, foi criado um arquivo <code>Dockerfile</code> para containetizar o sistema. Por fim, um <code>docker-compose.yml</code> que permite executar a aplicação em sua totalidade.

```
docker-compose build
docker-compose up
```

<h3>Estrutura de Diretórios</h3>

- prova2
  - src
    - logs
    - docker-compose.yml
    - Dockerfile
    - logging_config.py
    - logs.py
    - main.py
    - requirements.txt
  - README.md


<h3>Desafios e Próximos Passos</h3>

Ao implementar os elementos da atividade, não foi possível adicionar um container com um Gateway utilizando NGINX, nem testar as rotas da API com o Insomnia. Embora a aplicação tenha sido containerizada, tive também dificuldades com a execução do sistema em sua completude. Acredito que estes seriam os próximos passos para progredir com a atividade em um momento futuro.