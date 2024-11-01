#sql  #nosql

### Опыт работы с SQL и NoSQL базами данных

###### SQL базы данных

**SQL (Structured Query Language)** базы данных используют реляционную модель данных и обеспечивают поддержку ACID-транзакций.

1️⃣ **PostgreSQL**
   - **Опыт**: Проектирование схем, оптимизация запросов, хранимые процедуры, индексы, триггеры.
   - **Пример**: Разработка сложных запросов, настройка репликации и резервного копирования.
   - **Инструменты**: pgAdmin, psql, pg_stat_statements.

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_users_email ON users(email);
```

2️⃣ **MySQL/MariaDB**
   - **Опыт**: Администрирование, настройка репликации и кластеризации, оптимизация производительности.
   - **Пример**: Миграция данных, оптимизация конфигурации сервера.
   - **Инструменты**: MySQL Workbench, phpMyAdmin, mysql, mysqldump.

```sql
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

3️⃣ **Microsoft SQL Server**
   - **Опыт**: Проектирование баз данных, управление сервером, T-SQL скрипты, хранимые процедуры.
   - **Пример**: Создание отчетов, настройка Always On Availability Groups.
   - **Инструменты**: SQL Server Management Studio (SSMS), Visual Studio.

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    BirthDate DATE,
    Position NVARCHAR(100)
);
CREATE PROCEDURE GetEmployeeById
    @EmployeeID INT
AS
BEGIN
    SELECT * FROM Employees WHERE EmployeeID = @EmployeeID;
END;
```

##### NoSQL базы данных

**NoSQL (Not Only SQL)** базы данных предназначены для работы с нереляционными структурами данных и часто используются для приложений, требующих высокой производительности.

1️⃣ **MongoDB**
   - **Опыт**: Проектирование схем, работа с коллекциями и документами, агрегирующие запросы, индексы.
   - **Пример**: Система учета товаров, настройка репликации и шардинга.
   - **Инструменты**: MongoDB Compass, mongo shell, Mongoose.

```js
db.products.insertOne({
    name: "Laptop",
    price: 1200,
    category: "Electronics",
    createdAt: new Date()
});
```

2️⃣ **Redis**
   - **Опыт**: Кэш и хранилище ключ-значение, настройка кластеров, работа с типами данных (строки, списки, множества).
   - **Пример**: Кэширование запросов, очереди задач.
   - **Инструменты**: redis-cli, Redis Desktop Manager, redis-py.

```python
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('username', 'johndoe')
username = r.get('username')
print(username)
```

3️⃣ **Cassandra**
   - **Опыт**: Проектирование и оптимизация схем, управление кластерами, CQL (Cassandra Query Language).
   - **Пример**: Высоконагруженные системы, настройка репликации.
   - **Инструменты**: cqlsh, DataStax DevCenter.

```sql
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    name TEXT,
    email TEXT,
    created_at TIMESTAMP
);
INSERT INTO users (user_id, name, email, created_at)
VALUES (uuid(), 'Alice', 'alice@example.com', toTimestamp(now()));
```

**Краткое резюме**

Имею значительный опыт работы с SQL и NoSQL базами данных. SQL базы данных (PostgreSQL, MySQL, SQL Server) использовал для транзакционных приложений и аналитических систем. NoSQL базы данных (MongoDB, Redis, Cassandra) использовал для высоконагруженных систем, кэширования и работы с большими данными. Этот опыт включает проектирование схем, оптимизацию запросов, настройку репликации и кластеризации.