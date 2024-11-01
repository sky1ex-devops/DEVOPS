#git/gitlab 

GitLab Runner — это приложение с открытым исход кодом, используемое для выполнения задач [[CI CD|CI/CD]] в проектах GitLab. Оно отвечает за выполнение заданий (jobs), определенных в файле `.gitlab-ci.yml`, и за передачу результатов обратно в GitLab.

**Основные компоненты и архитектура**

🟠**GitLab**: Центральный сервер, где хранятся репозитории, настройки проектов и пайплайны CI/CD.
🟠**GitLab Runner**: Агент, который устанавливается на отдельный сервер или виртуальную машину и выполняет задачи CI/CD.
🟠**Executor**: Способ выполнения заданий Runner-ом, такие как [[Docker]], Shell, VirtualBox, [[Kubernetes]] и другие.

**Установка и настройка GitLab Runner**

Установка GitLab Runner зависит от операционной системы. Пример для Ubuntu:
```sh
GitLab Runner
curl -L --output /usr/share/keyrings/gitlab-runner-archive-keyring.gpg https://packages.gitlab.com/runner/gitlab-runner/gpgkey
echo "deb [signed-by=/usr/share/keyrings/gitlab-runner-archive-keyring.gpg] https://packages.gitlab.com/runner/gitlab-runner/ubuntu/ $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gitlab-runner.list
Runner
sudo apt-get update
sudo apt-get install gitlab-runner
```

После установки GitLab Runner нужно зарегистрировать его в GitLab для связи с проектом:

```sh
sudo gitlab-runner register
```

**Во время регистрации нужно указать:**
🟠**URL GitLab сервера**.
🟠**Токен регистрации** (доступен в настройках GitLab проекта).
🟠**Описание и метки Runner-а**.
🟠**Тип Executor-а** (например, Shell, Docker).

Пример регистрации

```sh
Please enter the gitlab-ci coordinator URL (e.g. https://gitlab.com/):
https://gitlab.com/
Please enter the gitlab-ci token for this runner:
<TOKEN>
Please enter the gitlab-ci description for this runner:
[hostname] my-runner
Please enter the gitlab-ci tags for this runner (comma separated):
docker,aws
Please enter the executor: shell, docker, docker-ssh, ssh, docker+machine, kubernetes, custom:
docker
```

Конфигурация файла .gitlab-ci.yml: Файл .gitlab-ci.yml определяет этапы (stages) и задания (jobs) пайплайна CI/CD. Пример простого файла:

```yaml
stages:
  - build
  - test
  - deploy

build_job:
  stage: build
  script:
    - echo "Building the project..."
    - ./build.sh
test_job:
  stage: test
  script:
    - echo "Running tests..."
    - ./test.sh
deploy_job:
  stage: deploy
  script:
    - echo "Deploying the project..."
    - ./deploy.sh
```

**Как работает GitLab Runner**

🟠**Запуск задания**: Когда код попадает в репозиторий (например, при пуше или создании мержа), GitLab инициирует запуск пайплайна, используя задания, определенные в `.gitlab-ci.yml`.
🟠**Получение задания**: Зарегистрированный Runner получает задание от GitLab сервера. Runner выбирается на основе меток и доступности.
🟠**Выполнение задания**: Runner выполняет шаги, указанные в скрипте `задания` (`script`). Это может включать сборку, тестирование, деплой и другие задачи.
🟠**Отправка результатов**: После выполнения задания Runner отправляет результаты обратно в GitLab сервер. Это включает в себя выходные данные, статусы выполнения и артефакты.

**Типы Executor-ов**

🟠**Shell**: Выполнение команд в оболочке (например, Bash).
🟠**Docker**: Выполнение команд в Docker-контейнере.
🟠**Docker+machine**: Автоматическое создание Docker-окружений с использованием Docker Machine.
🟠**Kubernetes**: Выполнение заданий в подах Kubernetes.

В файле .`gitlab-ci.yml` можно указать Docker Executor для выполнения заданий в контейнерах:

```yaml
build_job:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker build -t myapp:latest .
    - docker push myregistry/myapp:latest
```