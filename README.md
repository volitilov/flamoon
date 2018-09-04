# flamoon

[![Foo](https://badges.gitter.im/flamoon/Lobby.svg)](https://gitter.im/japronto/Lobby)
[![Foo](https://img.shields.io/pypi/v/flamoon.svg)](https://pypi.python.org/pypi/flamoon)
[![Foo](https://img.shields.io/pypi/pyversions/flamoon.svg)](https://pypi.python.org/pypi/flamoon/)
[![Foo](https://travis-ci.org/volitilov/flamoon.svg?branch=master)](https://travis-ci.org/volitilov/flamoon)

---

Надстройка над Flask, для быстрой и удобной web-разработки. При инициализации
формирует уже готовый набор данных необходиммых для старта web-разработки на
Flask.
Вот дерево коталогов и файлов после комманды инициализации `flamoon init`:

```bash
.
├── app
│   ├── email.py
│   ├── ex
│   │   ├── data.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── templates
│   │   │   └── ex.html
│   │   └── views.py
│   ├── extensions.py
│   ├── __init__.py
│   ├── models
│   │   └── user.py
│   ├── static
│   │   └── img
│   │       └── favicon.ico
│   └── templates
│       └── base.html
├── config.py
├── manage.py
└── tests
    ├── app
    │   └── test_app.py
    └── client
        └── test_client.py
```


### technical requirements

По умолчанию конфигурация настроена на работу с PostgreSQL, поэтому удачного
старта можно добится только после установки и добавления своих авторизационных
данных в файл `.env`.


### install

```bash
$ pip install flamoon
```

### usage

#### create new project

```bash
$ flamoon init
```

#### run project

```bash
$ export $FLASK_APP=manage.py
$ flask db init
$ flask db migrate -m 'initial commit'
$ flask run
```

#### run tests

```bash
$ flask test all
$ flask test client
$ flask test app
```


#### run shell

```bash
$ flask shell
```


#### run coverage

```bash
$ flask test_cov
```


#### run profiling

```bash
$ flask profile
```


#### work with database

```bash
$ flask db migrate -m 'message'
$ flask db upgrade
```