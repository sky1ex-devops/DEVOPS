#console

```bash
# Поиск файлов по имени
find /home/user/documents -name "example.txt"

# Поиск файлов по расширению
find /var/log -name "*.log"

# Поиск файлов, измененных за последние 7 дней
find /etc -mtime -7

# Поиск файлов, измененных более, чем 30 дней назад
find /usr/local -mtime +30

# Найти и удалить файл
find /tmp - name "oldfile.txt" -delete

# Поиск пустых файлов или каталогов
find /var/www -empty

# Найти файлы больше 100 Мб
find /home/user/Downloads -size +100M

# Поиск файлов, владельцем которых является конкретный пользователь
find /home -user username

# Найти файлы с полномочиями 644
find /etc -perm 644

# Найти файлы по расширению и выполнить команду архивирования
find /var/log -name "*.log" -exec gzip {} \;

# Найти пустые файлы и выполнить команду удаления файлов
find /home/user/documents -type f -empty -exec rm {} \;

# Найти файлы исключая конкретную директорию
find / -path "/proc" - prune -o -name "*.conf" -print

# Найти файлы, измененных за последние 60 минут
find /var/www -mmin -60

# Найти и ахривировать файлы с конкретным расширением
find /home/user/pictures -name "*.jpg" | xargs tar -czvf archive.tar.gz

# Найти символические ссылки
find /usr/bin -type l
```
