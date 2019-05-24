# avito-intern-test-task
Tesk task for Full-stack DBA intern position

## Основное задание
Написать сервер на Python3, завернутый в докер-контейнер, у которого будет следующее API:

GET /api/v1/get_rabbit
GET /api/v1/get_mongo
Response должен содержать в body работающий shell скрипт для установки standalone RabbitMQ или MongoDB на DebianStretch.

## Усложнение 1
Добавить метод для тестирования установки standalone MongoDB (придумать шаги тестирования самостоятельно)

GET /api/v1/test_mongo?host=arg1&port=arg2
Response должен вернуть true, если тесты прошли успешно и false в противном случае.

## Усложнение 2
Добавить в метод get_mongo возможность установки реплика-сета (primary, secondary, arbiter).

GET /api/v1/get_mongo?replication=true
После установки с помощью сгенерированного shell скрипта должны успешно пройти тесты из усложнения 1.

