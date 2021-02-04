# test_user_api
## Описание
API для создания редактирования и удаления профилей пользователя. 

Новый профиль может создать любой уже существующий пользователь. Но удалить
или изменить созданный профиль может только его хозяин. Также все операции
по созданию, изменению и удалению профилей доступны через панель 
администратора http://127.0.0.1:8000/admin/

## Установка
* склонируйте репозиторий
* перейдите в папку с проектом
* создайте файл .env с одной строкой: S_KEY = <ваш SECRET_KEY>
* создайте виртуальное окружение
* установите необходимые библиотеки
* запустите миграции
* создайте суперпользователя
* запустите проект

```
git clone https://github.com/Fr33vvay/test_user_api.git
cd test_user_api/
python -m venv venv
pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

### Токен аутентификации
Используется JWT-token. Для того, чтобы пользователь мог отправлять запросы,
ему необходимо послать POST-запрос на получение токена по адресу
http://127.0.0.1:8000/api/v1/token/ В теле запроса надо передать свой
username и password. В ответ будет получен токен вида
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGcigfdgIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxMjU1MDYxNCwianRpIjoiNTU4MGIyYzUyZDg3NDA5MGExNmNhNmRjMGY2YjJiOGYiLCJ1c2VyX2lkIjoxMX0.-jDswawANZNgunZUHOjU84OrOGr9grTNn31MI27Bsec",
    "access": "eyJ0eXAiOiJKV1QiLCJhbfdOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjEyODk2MjE0LCJqdGkiOiJlMTMyNDBmM2I0YzQ0MjMzODhmYWE1NDU4ZTg3MGIxNCIsInVzZXJfaWQiOjExfQ.ZNfXYdWRfkIza8CuiuRrk52-nGsU9C3jsrRpzOJNMdQ"
}
```
В дальнейшем в каждый запрос необходимо добавлять параметр 
Authorization: Bearer <значение access без кавычек>. Значение refresh
используется для обновления токена. Срок жизни токена - 5 дней.
[Подробнее.](https://pyjwt.readthedocs.io/en/stable/)

### Дополнительная информация
При пуше в ветку main на github проводится автоматическая проверка тестов
и соответствия PEP8.
