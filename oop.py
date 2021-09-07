class employee:
    raise_percent=1.04
    number_of_employee=0
    def __init__(self,f_name,l_name,salary):
        self.f_name=f_name
        self.l_name=l_name
        self.salary=salary
        employee.number_of_employee+=1
    
    def pay_amount(self):
        self.pay_amount=self.salary*self.raise_percent
        return self.pay_amount
        
    def full_name(self):
        print('{} {}'.format(self.f_name,self.l_name))
        
    @classmethod
    def from_string(cls,string):
        f_name,l_name,salary=string.split('-')
        return cls(f_name, l_name, salary)
    
class developer(employee):
    def __init__(self,f_name,l_name,salary,program):
        super() .__init__(f_name,l_name,salary)
        self.program=program
        
    
dev1=developer('Aravind','toretto',45000,'python')
dev2=developer('siva','kumar',50000,'python')
dev3=developer('manoj','kumar',50000,'java')
dev1.full_name()
print(dev2.salary)
print(dev1.program)
print(dev3.program)
print(dev2.l_name)



    
    
        
emp1=employee('aravind','toretto',50000)
emp2=employee('kevin', 'clifford', 90000) 
emp3=employee('dinesh','military',50000)  
emp1.raise_percent=1.05
string1=('keerthi-Aravind-50000')
string2=('dinesh-raguraj-50000')
emp_wife=employee.from_string(string1)
emp_4=employee.from_string(string2)

print(emp1.raise_percent) 
print(emp2.raise_percent)
print(emp3.raise_percent)
print(employee.number_of_employee)
print(emp_wife.full_name())
print(emp2.pay_amount())
emp2.full_name()
 


#class variable are acessed using both class and instances of class
#use wisely when you needed to use the variables
class employee:
    b_percent=1.05
    no_employee=0
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
        
        employee.no_employee+=1
        
    def yearly_bonous(self):
        print(int(self.salary * self.b_percent))
    @classmethod    
    def change_bpercent(cls,amount):
        cls.b_percent=amount
    @classmethod
    def get_value(cls,srting):
        name,salary,departement=string.split('-')
        return cls(name,salary,department)
#inheritance is process of accessing functionality from parent class or super class
class developer(employee):
    def __init__(self,name,salary,department,pro_lan):
        super().__init__(name,salary,department)
        self.pro_lan=pro_lan
        
class manager(employee):
    def __init__(self,name,salary,departement,employee=None):
        super().__init__(name,salary,departement)
        if employee is None:
            self.employee=[]
        else:
            self.employee=employee
        
    def add_employee(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)
            
    
    def remove_employee(self,emp):
        if emp  in self.employee:
            self.employee.remove(emp)
            
    def print_employee(self):
        for emp in self.employee:
            print(emp)
            
emp1=employee('aravind',35000,'developer')
emp2=employee('kevin clifford', 50000,'manager') 

dev1=developer('siva kumar', 50000, 'developer', 'python')
dev2=developer('dinesh raguraj',50000,'developer','python')
dev3=developer('aravind',50000,'developer','python')
print(dev1.salary)
print(dev2.name)

mrg1=manager('kevin clifford',100000,'manager','dev3')
print(mrg1.name)
mrg1.add_employee(dev2)
mrg1.add_empoyee(dev1)
print(mrg1.employee)
# print(employee.no_employee)       
# emp1.yearly_bonous()
# employee.change_bpercent(1.10)
# # employee.b_percent=1.10
# emp1.yearly_bonous()
# emp2.yearly_bonous()