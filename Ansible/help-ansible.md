    .
 
    ├── group_vars              # - переменные для групп хостов
    ├── inventory               # - указываем набор управляемых хостов
    │   └── inventory           
    ├── playbooks               # - Какие роли и задачи выполнять  
    │   └── testroles.yml 
    ├── roles                   # - Описываем роли
    │   ├── kay_ssh
    │   │   ├── defaults
    │   │   ├── files
    │   │   ├── handlers
    │   │   ├── tasks
    │   │   │   └── main.yml
    │   │   └── templates
    │   ├── nginx-test
    │   │   ├── defaults
    │   │   │   └── main.yml
    │   │   ├── files
    │   │   ├── handlers
    │   │   │   └── main.yml
    │   │   ├── tasks
    │   │   │   └── main.yml
    │   │   └── templates
    │   │       └── website.j2
    │   └── python
    │       ├── defaults
    │       │   └── main.yml
    │       ├── files
    │       ├── handlers
    │       │   └── main.yml
    │       ├── tasks
    │       │   └── main.yml
    │       └── templates
    │           └── website.j2
    └── roles-common
