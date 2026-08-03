class Person:
    def __init__(self, full_name, date_of_birth):
        self.full_name = full_name
        self.date_of_birth = date_of_birth

    def is_adult(self):
        #today = 03-08-2026
        #age = self.date_of_birth - today?????
        #if age > 18:
            #return True
        return False

    def screen_name(self):
        name = self.full_name.replace(' ', '') + self.date_of_birth[3:5] + self.date_of_birth[0:2]
        return name

class Staff(Person):
    def screen_name(self):
        name = []
        for ch in self.full_name:
            if ch.isalpha:
                name.append(ch)
        screenname = name.join() + self.date_of_birth[3:5] + self.date_of_birth[0:2] + 'Staff'
        return screenname
    
    def is_adult(self):
        return True

class Student(Person):
    def is_adult(self):
        return False


import sqlite3
conn = sqlite3.connect('school.db')

with open('people.txt') as file:
    for line in file:
        info = line.strip().split(',')
        if info[2] == 'Person':
            p = Person(info[0], info[1])
        elif info[2] == 'Staff':
            p = Staff(info[0], info[1])
        elif info[2] == 'Student':
            p = Student(info[0], info[1])
            
        print(info)
        conn.execute('INSERT INTO ? (FullName, DateOfBirth, ScreenName, isAdult) VALUES (?,?,?,?)', (info[0].split(' ')[0], info[0].split(' ')[1], p.screen_name(), p.isAdult())
conn.commit()
conn.close()
