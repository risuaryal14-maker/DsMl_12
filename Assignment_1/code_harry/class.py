#basic class programing
print('frist-->')
class employee:
    
    salary=180000           #class attribute=instance attribute
    language='python'
rickson=employee()
rickson.name='rickson aryal,'
print(rickson.name,rickson.language, rickson.salary)

risu=employee()
risu.name='risu aryal,'
print(risu.name,risu.language, risu.salary)

#hence the salary and language is directly align to the class
#but the name is in diferent catogery so it called as an object


#instance attribute and class attribute
print('second------->')
class employee:
    salary=180000           
    language='python'
rickson=employee()
rickson.language='javaScript,'
print(rickson.language, rickson.salary)
#if you have defult class attribute and instance attribute simultaneously,
#the code will run instance attribute automatically

#self parameter
print('third------>')
class employee:
    name='rickson'
    salary=180000           
    language='python'
    def getInfo(self):
        print(f' your salary is:{self.salary} and you have completed learning {self.language}')
    def greet(self):
        print(f'good morning,{self.name}')
rickson=employee()
#rickson.language='javaScript,'
#print(rickson.language, rickson.salary)
rickson.greet()
rickson.getInfo()

#static method
print('fourth----->')
class employee():
    salary=12000
    language='javaScript'
    @staticmethod
    def greet():
        print('good morining')
risu=employee()
risu.greet()
print(risu.salary, risu.language)

#dunder method
print('fifth--------->')
class employee():
    salary=120000
    language='javascript'
    def __init__(self,name,language,salary):
        self.name=name
        self.language=language
        self.salary=salary
        print('hey')
risu=employee('rickson',130000,'javascript')
print(risu.name,risu.salary, risu.language)
