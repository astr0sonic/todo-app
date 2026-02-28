# Todo App

## How to start

Create the virtual environment:

```bash
./create-venv.sh
```

Fill `.env`-file:

```
PORT=
```

Start:

```bash
./start.sh
```

Структура API:

Регистрация/авторизация

```
POST /auth/sign-up - регистрация
POST /auth/sign-in - авторизация
```

Работа со списками задач (todo-list):

```
GET /lists - получение списков
GET /lists/{id} - получение конкретного списка
POST /lists - создание нового списка
PUT /lists/{id} - редактирование списка
DELETE /lists/{id} - удаление списка

GET /lists/{id}/tasks - получение задач в списке
POST /lists/{id}/tasks - создание новой задачи в списке
```

Работа с задачами (tasks):

```
GET /tasks/{id} - получение задачи
PUT /tasks/{id} - редактирование задачи
DELETE /tasks/{id} - удаление задачи
```
