import unittest
from format_name import get_formatted_name 

class NamesTestCase(unittest.TestCase): # создаем класс с серией модульных тестов
    """Тесты для 'format_name'."""      

    def test_firstlast_name(self):    
        """Имя вида 'John Doe' работает правильно? """
        formatted_name = get_formatted_name('John', 'Doe', 'J') # вызываем функцию и возвращаем
                                                        # результат в formatted_name
        self.assertEqual(formatted_name, 'John J Doe') # метод assertEqual проверяет соответствия 
                                                     # желаемого результата с фактическим
                                                     # "Сравни formatted_name с 'John Doe' "
    def test_first_last_middle_name(self):
        """Работают ли такие имена, как 'Wolfgang Amadeus Mozart'?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus'
                                        )
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()

#---------------------------------------------------------------------#
# Методы assert - проверка соответствия
# 
# assertEqual(a,b) Проверяет, что a == b
# assertNotEqual(a,b) Проверяет, что a != b
# assertTrue(x) Проверяет, что x - истинно
# assertFalse(x) Проверяет, что x - ложно
# assertIn(элемент, список) Проверяет, что элемент входит в список
# assertNotIn(элемент, список) Проверяет, что элемент не входит
#  в список
#---------------------------------------------------------------------#

