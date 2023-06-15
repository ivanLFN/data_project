# Проект Django API для работы с файлами

## Установка

1. Клонируйте репозиторий:

``` 
https://github.com/ivanLFN/data_project.git
```

2. Установите зависимости находясь в корне проекта:

```
pip install -r requirements.txt
```

## API

Для взаимодействия с api в заголовке необходимо указать токен. Существуют следующие эндпоинты.:

__POST /upload_file/__: Загрузка файла. В теле запроса необходимо указать файл для загрузки.

__GET /files/__: Получение списка загруженных файлов.

__GET /files/{file_id}/columns/__: Получение списка столбцов в файле с указанным идентификатором file_id.

__GET /files/{file_id}/data/__: Получение данных из файла с указанным идентификатором file_id. Вы можете также использовать фильтры и сортировку для получения конкретных данных.

__POST /register/__: Регистрация нового пользователя. В теле запроса необходимо указать данные пользователя, такие как имя пользователя (username), пароль (password) и электронная почта (email).

__POST /login/__: Авторизация пользователя. В теле запроса необходимо указать данные пользователя, такие как имя пользователя (username) и пароль (password).


## Примеры использования API

1. Пример загрузки файла:
```
curl -X POST -H "Authorization: Token <ваш_токен>" -F "file=@путь_к_файлу" http://localhost:8000/upload_file/
```

2. Пример получения списка загруженных файлов:
```
curl -X GET -H "Authorization: Token <ваш_токен>" http://localhost:8000/files/
```

3. Пример получения списка столбцов в файле:
```
curl -X GET -H "Authorization: Token <ваш_токен>" http://localhost:8000/files/1/columns/
```

4. Пример регистрации нового пользователя:
```
curl -X POST -H "Content-Type: application/json" -d '{"username":"admin", "password":"admin", "email":"admin@example.com"}' http://localhost:8000/register/
```

5. Пример авторизации пользователя:
```
curl -X POST -H "Content-Type: application/json" -d '{"username":"admin", "password":"admin"}' http://localhost:8000/login/
```