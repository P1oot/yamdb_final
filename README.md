# yamdb_final

## Описание.

Доработка проекта https://github.com/P1oot/api_yamdb.
В данной версии проект можно развернуть на виртуальной машине при помощи контейнеризации Dkcker, что позволяет не беспокоиться о совместимости.
Реализована настройка приложений CI и CD.
Данный проект позволяет делать обзоры и давать оценку различным произведенияя, оставлять комментарии.

![Yamdb_workflow](https://github.com/P1oot/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Установка.

Клонировать репозиторий и перейти в него в командной строке:
`git clone git@github.com:P1oot/infra_sp2.git`
`cd infra_sp2`

Запустите docker-compose:
`docker-compose up -d`

Выполнить миграции:
`docker-compose exec web python manage.py migrate`

Создать суперпользователя:
`docker-compose exec web python manage.py createsuperuser`

Подключить статику:
`docker-compose exec web python manage.py collectstatic --no-input`

Остановить контейнеры можно комадой:
`docker-compose stop`

## Примеры запросов.

"Регистрация нового пользователя": "http://127.0.0.1:8000/api/v1/auth/signup/"

"Получение JWT-токена": "http://127.0.0.1:8000/api/v1/auth/token/"

"Обращение к категориям": "http://127.0.0.1:8000/api/v1/categories/"

"Обращение к жанрам": "http://127.0.0.1:8000/api/v1/genres/"

"Обращение к произведениям": "http://127.0.0.1:8000/api/v1/titles/"

"Обращение к отзывам": "http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/"

"Обращение к комментариям": "http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/"

### Авторы:

**Бердинских Даниил** https://github.com/P1oot

**Крицина Анна** https://github.com/cistellula

**Куликов Андрей** https://github.com/Kulikov1
