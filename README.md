# Todo-App

## How to start project

Create the virtual environment:

```bash
./create-venv.sh
```

Start:

```
./start.sh
```

Базовый функционал:

* регистрация/авторизация;
POST /auth/sign-up - регистрация
POST /auth/sign-in - авторизация

* работа со списками задач:

    * создание списка;
    POST /lists
    * просмотр списков;
    GET /lists
    * просмотр списка;
    GET /lists/{id}
    * редактирование списка;
    PUT /lists/{id}
    * удаление списка;
    DELETE /lists/{id}

* работа с задачи:

    * создание задачи;
    POST /lists/{id}/tasks
    * получение всех задач списка;
    GET /lists/{id}/tasks

    * просмотр задачи;
    GET /lists/{id}/tasks/{task_id}
    GET /tasks/{id}
    * редактирование задачи;
    PUT /lists/{id}/tasks/{task_id}
    PUT /tasks/{id}
    * удаление задач.
    DELETE /lists/{id}/tasks/{task_id}
    DELETE /tasks/{id}

Схема хранения данных:
https://miro.com/app/board/uXjVLEPaEcM=/?share_link_id=467286878499

Запуск БД в докер-контейнере
```
$ docker run --name db -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -d postgres
```
