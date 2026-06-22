class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary
        pass

    @property
    def name(self):
        return self._name
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter 
    def salary(self, salary):
        if salary < 0:
            raise ValueError("El Salario no puede ser negativo")
        self._salary = salary
        
    def promote(self, porcent):
        self._salary = (self._salary * porcent) + self._salary

employee = Employee("Ana", 1000)
employee.promote(0.1)  

#employee2 = Employee("Emilio", -1000 )

print(employee.name)
print(employee.salary) 

#print(employee2.name)
#print(employee2.salary) 


