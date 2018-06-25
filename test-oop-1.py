class Employee:
    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.' + last + '@kmitl.ac.th'

        Employee.num_of_emp += 1

    @property
    def email(self):
        return '{}.{}@kmitl.ac.th'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split('')

    @fullname.deleter
    def fullname(self):
        print 'Delete Name!'
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)       # super().__init__(first, last, pay) not support in python 2
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)       # super().__init__(first, last, pay) not support in python 2
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print '-->', emp.fullname()



# dev_1 = Developer('Pacharapol', 'Deesawat', 50000, 'Python')
# dev_2 = Developer('Benny', 'Benjarat', 60000, 'Java')

emp_1 = Employee('Core', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
# print emp_1.__repr__()
# print emp_1.__str__()

print emp_1 + emp_2

emp_1.fullname = 'Corey Schafer'

print emp_1.email

del emp_1.fullname
# print int.__add__(1, 2)
# print str.__add__('b', 'a')


# mgr_1 = Manager('Sue', 'Smith', 90000)


# print isinstance(mgr_1, Manager)

# print mgr_1.email
#
# # mgr_1.add_emp(dev_2)
# # mgr_1.remove_emp(dev_1)
#
# mgr_1.add_emp()
#
# print mgr_1.print_emps()

# print dev_1.email
# print dev_2.email

# print dev_1.prog_lang
# print dev_2.prog_lang
# print dev_1.pay
# dev_1.apply_raise()
# print dev_1.pay

# emp1 = Employee('Pacharapol', 'Deesawat', 6000)
# emp2 = Employee('Benny', 'Benjarat', 12000)
#
# Employee.set_raise_amt(1.10)
#
# print emp1.fullname()
# print Employee.fullname(emp1)
# print Employee.raise_amount
# print emp1.pay
# emp1.apply_raise()
# print emp1.pay
#
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steven-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'
#
# new_emp_1 = Employee.from_string(emp_str_1)
# new_emp_2 = Employee.from_string(emp_str_2)
# new_emp_3 = Employee.from_string(emp_str_3)
#
# print Employee.num_of_emp
#
# import datetime
#
# my_date = datetime.date(2016, 7, 12)   #  << Sunday
# print Employee.is_workday(my_date)


# print emp2.fullname()
# print Employee.fullname(emp2)
# print emp2.email
