#docker

- ***docker attach***     - Подключиться к запущенному контейнеру стандартным терминалом
	- *docker attach [OPTIONS] CONTAINER*  <br>
		*OPTIONS:* 
		*--detach-keys `string`* - Переопределение последовательности клавиш для отсоединения контейнера
		*--nostdin-proxy* - Не подключать стандартный ввод
		*--sig-proxy* - Проксировать все полученные сигналы для процесса (по умолчанию true)
		<br>
- ***docker build***        - Собрать образ из Dockerfile
	- docker build [OPTIONS] PATH | URL | <br>
		*OPTIONS:*
		*--add-host `list`*           Добавьте пользовательский host-to-ip маппинг (host:ip)  
		*--build-arg `list`*          Установите переменные времени сборки
		*--cache-from `strings`*      Образы, которые следует рассматривать в качестве источников кэша  
		*--cgroup-parent `string`*    Необязательная родительская группа для контейнера  
		*--compress*                Сжатие сборки с помощью gzip  
		*--cpu-period `int`*          Ограничьте период использования CPU CFS (полностью справедливого планировщика)  
		*--cpu-quota `int`*           Ограничьте квоту CPU CFS (полностью справедливый планировщик)  
		*-c, --cpu-shares `int`*          Доли процессора (относительный вес)
		*--cpuset-cpus `string`*      Процессоры, в которых разрешено выполнение (0-3, 0,1)  
		*--cpuset-mems `string`*      MEMS, в которых можно разрешить выполнение (0-3, 0,1)  
		*--disable-content-trust*   Пропустить проверку образа (по умолчанию true)
		*-f, --file `string`*             Имя Dockerfile (по-умолчанию 'PATH/Dockerfile')  
		*--force-rm*                Всегда убирайте промежуточные контейнеры
		*--iidfile `string`*          Записать ID образа в файл  
		*--isolation `string`*        Технология изоляции контейнеров  
		*--label `list`*              Установка метаданных для образа  
		*-m, --memory `bytes`*            Ограничение памяти  
		*--memory-swap `bytes`*       Изменить размер файла подкачки: '-1' для неограниченной подкачки  
		*--network `string`*          Установите сетевой режим для выполнения инструкций во время сборки (по умолчанию "default").  
		*--no-cache*                Не использовать кэш при сборке образа  
		*--pull*                    Всегда пытаться загрузить более новую версию образа  
		*-q, --quiet*                   Отключить вывод при сборке и вывести ID образа при успешном выполнении  
		*--rm*                      Удалить промежуточные контейнеры после успешной сборки (по умолчанию true)  
		*--security-opt `strings`*    Параметры безопасности  
		*--shm-size `bytes`*          Размер /dev/shm  
		*-t, --tag `list`*                Имя и, при необходимости, тег в формате 'name:tag'  
		*--target `string`*           Set the target build stage to build.  
		*--ulimit `ulimit`*           Ulimit options (default [])
		 <br>
- ***docker commit***   - Собрать новый образ, согласно изменениям в контейнере
	- docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]] <br>
	*OPTIONS*
	 *-a, --author `string`*    Автор (e.g., "John Hannibal Smith <hannibal@a-team.com>")  
	 *-c, --change `list`*      Примените инструкцию Dockerfile к созданному образу  
	 *-m, --message `string`*   Сообщение к коммиту  
	 *-p, --pause*            Приостановить контейнер во время коммита (по-умолчанию true)
	<br>
- ***docker cp***             - Копирует файлы/каталоги между контейнером и локальной файловой системой
	- docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|-
    docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH <br>
	Используйте '-' в качестве источника для чтения архива tar из стандартного ввода данных и извлечения его в целевой каталог в контейнере.
	Используйте '-' в качестве пункта назначения для потоковой передачи tar-архива исходного кода контейнера в стандартный вывод. <br>
	*OPTIONS*:  
	 *-a, --archive*       Режим архивирования (копирование всей информации о uid/gid)
	 *-L, --follow-link*   Всегда переходите по символической ссылке в SRC_PATH
	<br>

***docker create***      - Создать новый контейнер
***docker diff***            - Показывает изменения в файловой системе с момента создания контейнера
***docker events***      - Отображает события контейнеров в реальном времени

- ***docker exec***          - Выполняет команду в запущенном контейнере
	- docker exec [OPTIONS] CONTAINER COMMAND [ARG...] <br>
	*OPTIONS:*
	*-d, --detach* &emsp;  Автономный режим: запуск команды в фоновом режиме
	*--detach-keys `string`* &emsp;  Переопределение последовательности клавиш для отсоединения контейнера
	*-e, --env `list`*      &emsp;         Установите переменные среды
    *--env-file `list`*     &emsp;     Просмотр в файле переменных окружения
	*-i, --interactive*         &emsp;    Держите стандартный ввод открытым, даже если он не подключен
    *--privileged*         &emsp;    Предоставьте расширенные привилегии команде
	*-t, --tty*              &emsp;      Allocate a pseudo-TTY
	*-u, --user `string`*   &emsp;        Имя пользователя или UID (формат: <name|uid>[:<group|gid>])
	*-w, --workdir `string`*       &emsp;  Рабочий каталог внутри контейнера
	<br>

- ***docker export***       - Собрать информацию о контейнере в архив
	- docker export [OPTIONS] CONTAINER <br>
	*OPTIONS:*
	*-o, --output `string`*  -  Запись в файл вместо стандартного вывода
	<br>
	
***docker history***       - Показать историю изменений образа

- ***docker images***      - Показать список образов
	- docker images [OPTIONS] [REPOSITORY[:TAG]] <br>
	*OPTIONS:*
	*-a, --all*             Показывать все изображения (по умолчанию промежуточные изображения скрыты)  
	*--digests*         Показывать дайджесты  
	*-f, --filter `filter`*   Отфильтровать выходные данные на основе предоставленных условий  
	*--format `string`*   Pretty-print images using a Go template  
	*--no-trunc*        Не усекать выходные данные  
	*-q, --quiet*           Показать только ID образов
	<br>

***docker import***        - Создать образ из архива, созданного с помощью *export*
***docker info***             - Системная информация о контейнерах

- ***docker inspect***       - Показать полную низкоуровневую информацию об объектах Docker
	- docker inspect [OPTIONS] NAME|ID [NAME|ID...] <br>
	*OPTIONS:*
	*-f, --format `string`*   Format the output using the given Go template  
	*-s, --size*            Отображать общий размер файла, если выбран тип контейнера  
	 *--type `string`*     Возвращает JSON для указанного типа
	 <br>
	 
***docker kill***               - Принудительное удаление контейнера
***docker load***            - Загрузить образ(ы) из архива
***docker login***           - Авторизация в Docker registry
***docker logout***        - Деавторизация в Docker registry
***docker logs***            - Вывести логи контейнера
***docker pause***         - Приостановить все процессы в контейнере
***docker port***             - Вывести маппинг портов или специфику маппинга контейнера

- ***docker ps***                - Вывести список контейнеров
	- docker ps [OPTIONS] <br>
	*OPTIONS:*
	*-a, --all*             Показывать все контейнеры (по умолчанию отображаются только запущенные)
	*-f, --filter `filter`*   Фильтруйте выходные данные на основе предоставленных условий  
	*--format `string`*   Pretty-print containers using a Go template  
	*-n, --last `int`*        Показаны последние созданные контейнеры (включая все состояния) (по умолчанию -1)  
	*-l, --latest*          Показать последний созданный контейнер (включая все состояния)  
	*--no-trunc*        Не усекать выходные данные  
	*-q, --quiet*           Отображать только ID контейнеров  
	*-s, --size*            Отображение общего размера файла
	<br>
	
***docker pull***              - Загрузить образ (pull) из Docker registry
***docker push***           - Загрузить образ (push) в Docker registry
***docker rename***       - Переименоать контейнер
***docker restart***         - Перезапустить контейнер

- ***docker rm***                - Удалить остановленный контейнер(ы)
	- docker rm [OPTIONS] CONTAINER [CONTAINER...] <br>
	*OPTIONS:*
	*-f, --force*     Принудительное удаление запущенного контейнера (использует SIGKILL)  
	*-l, --link*      Удалить указанную ссылку  
	*-v, --volumes*   Удалить анонимные тома, связанные с контейнером
	<br>

***docker rmi***               - Удалить образ(ы)
***docker run***               - Запустить команду в новом контейнере
***docker save***             - Сохранить образ(ы) в архив
***docker search***         - Поиск образов в репозитории (Docker Hub)
***docker start***             - Запустить остановленный контейнер
***docker stats***            - Лайв-мониторинг статистики использования ресурсов контейнерами
***docker stop***             - Остановить запущенный контейнер
***docker tag***               - Создать тег для образа
***docker top***               - Отображает запущенные процессы
***docker unpause***      - Запусть приостановленные процессы в контейнере
***docker update***         - Обновить конфигурационные настройки для контейнера
***docker version***        - Информация о версии docker
***docker wait***              - Блокирует выполнение команды до остановки контейнера(ов)