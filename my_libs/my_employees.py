# coding: utf-8

class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        
        self.grade = 1
    
    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1
    
    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)
        
class Developer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)
    
    def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все разработчики проходят аккредитацию
        self.seniority += 1
        
        # условие повышения сотрудника из презентации
        if self.seniority % 5 == 0:
            self.grade_up()
        
        # публикация результатов
        return self.publish_grade()
            
class Designer(Employee):
    def __init__(self, name, seniority, awards=2):
        super().__init__(name, seniority)
        self.awards = awards
    
    def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все дизайнеры проходят аккредитацию
        self.seniority += 1
        
        # условие повышения сотрудника из презентации
        if (self.seniority + self.awards * 2) % 7 == 0:
            self.grade_up()
        
        # публикация результатов
        return self.publish_grade()