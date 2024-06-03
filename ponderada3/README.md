<h2>Construção de Aplicativo Híbrido com Flutter</h2>

Este projeto consiste em um aplicativo mobile desenvolvido em Flutter seguindo o padrão de arquitetura MVC (Model-View-Controller). O back-end da aplicação é desenvolvido em Python, utiliza o framework Flask, e está organizado em microsserviços.

## Estrutura do Projeto

### Back-end

O backend está organizado em três microsserviços:

1. **Serviço de Autenticação (`authentication_service`)**
2. **Serviço de Dados (`data_service`)**
3. **Serviço Principal (`main_service`)**

Estrutura padrão utilizada para cada serviço:

```shell
service/
├── app.py
├── config.py
├── models.py
├── routes.py
└── utils.py
```

### Front-end

A interface do aplicativo foi desenvolvida em Flutter e, até então, conta com uma tela de login.

Estrutura atual:

```shell
flutter_app/
├── lib/
│   ├── controllers/
│   │   └── login_controller.dart
│   ├── models/
│   │   └── user_model.dart
│   ├── views/
│   │   ├── login_view.dart
│   │   └── home_view.dart
│   └── main.dart
└── pubspec.yaml
```