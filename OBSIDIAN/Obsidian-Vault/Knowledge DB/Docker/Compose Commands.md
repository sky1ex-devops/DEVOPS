 #docker/docker-compose 
### [[Docker Compose Examples|Список шаблонов Docker Compose]]
#### Большинство команд производятся из директории с docker-compose.yml. Операции проводятся для контейнеров/образов/сервисов docker-compose файла
----------------------
***docker compose attach***        - Подключиться к запущенному контейнеру стандартным терминалом
***docker compose build***           - Собирает и пересобирает сервис
***docker compose config***         - Показывает конфигурацию compose-файла
***docker compose cp***               - Копирует файлы/каталоги между контейнером и локальной файловой системой
***docker compose create***         - Создаёт контейнеры для сервиса
***docker compose down***          - Останавливает и удаляет контейнеры и сети
***docker compose events***        - Отображает события контейнеров в реальном времени
***docker compose exec***            - Выполняет команду в запущенном контейнере
***docker compose images***       - Выводит список образов, используемых созданными контейнерами
***docker compose kill***               - Принудительно останавливает контейнеры
***docker compose logs***            - Отображает логи контейнеров
***docker compose ls***                 - Отображает список запущенных проектов
***docker compose pause***        - Приостанавливает сервисы
***docker compose port***            - Отображает публичные порты сервисов
***docker compose ps***               - Отображает контейнеры
***docker compose pull***             - Загрузить образы сервисов
***docker compose push***          - Загрузить образы сервисов в Docker registry
***docker compose restart***       - Перезапускает сервисы
***docker compose rm***              - Удаляет остановленные сервисы
***docker compose run***             - Запускает одноразовую команду в контейнере сервиса
***docker compose scale***         - Позволяет увеличить или уменьшить количество контейнеров для определенного сервиса
***docker compose start***          - Запускает остановленный сервис
***docker compose stats***          - Лайв-мониторинг статистики использования ресурсов контейнерами
***docker compose stop***           - Останавливает сервисы
***docker compose top***              - Отображает запущенные процессы
***docker compose unpause***    - Запускает приостановленные (paused) сервисы
***docker compose up***               - Собирает и запускает контейнер
	*-d (detach)* - фоновый режим
***docker compose version***       - Информация о версии docker compose
***docker compose wait***            - Блокирует выполнение команды, пока контейнер(ы)/ не будут запущены
***docker compose watch***         - Режим работы compose. при котором контейнеры автоматически обновляются на основе изменений в отслеживаемых файлах и каталогах
</block>