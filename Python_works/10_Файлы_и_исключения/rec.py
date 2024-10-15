filename = 'rec.txt'

with open(filename, 'w') as file_object: # Открываем фаил в режиме записи
                                         # w-запись, r-чтение, a-чтение и запись 
                                         # r+ - чтение и запись в файл
    file_object.write("I love programming.") # write - метод записи строки в файл

with open(filename) as file_object:
    object = file_object.read() 
    print(object)

#---------------------------------------------------------------------#
#  w - уничтожит данные файла перед записью                           #
#---------------------------------------------------------------------#
#  Можно сохранить только строки в файл, для чисел нужно              #
# воспользоваться методом str() для приобразования                    #
#---------------------------------------------------------------------#

filename = 'rec.txt'

with open(filename, 'a') as file_object: # Открываем фаил в режиме чтения-записи
                                         # w-запись, r-чтение, a-чтение и запись 
                                         # r+ - чтение и запись в файл
                                         # write - метод записи строки в файл
    file_object.write("Текст добавляется в конец файла.") 
    file_object.write("\nТак, нужно добавлять пернос строки.") 

with open(filename) as file_object:
    object = file_object.read() 
    print(object)
