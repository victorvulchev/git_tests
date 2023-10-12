class Human():
    def __init__(self, first_name, surname) -> None:
        self.first_name = first_name
        self.surname = surname
class Student(Human):
    def __init__(self, first_name, surname, mark) -> None:
        self.mark = mark
        super().__init__(first_name, surname)
class Worker(Human):
    def __init__(self, first_name, surname, wage, hours_worked) -> None:
        self.wage = wage
        self.hours_worked = hours_worked
        super().__init__(first_name, surname)
    def money_per_hour(self):
        return self.wage / self.hours_worked

list_of_workers = []
numb_of_workers = int(input())

for i in range(numb_of_workers):
    info = input().split()
    first_name, surname, wage, hours_worked = info
    wage = float(wage)
    hours_worked = float(hours_worked)
    the_worker = Worker(first_name, surname, wage, hours_worked)
    list_of_workers.append(the_worker)

for i in list_of_workers:
    money = Worker.money_per_hour(i)
    print(f"{first_name} {surname} {money}")

