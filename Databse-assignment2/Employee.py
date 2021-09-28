import sqlite3

conn=sqlite3.connect('employee.db')

c = conn.cursor()
#query="""CREATE TABLE Employee ( 
     #Emp_Id INTEGER NOT NULL PRIMARY KEY, 
     #Emp_Name TEXT NOT NULL, 
     #Dept_Id INTEGER NOT NULL,    
     #Salary INTEGER NOT NULL
     #);"""
#c.execute(query)


#query="""ALTER TABLE Employee ADD COLUMN City TEXT;"""
#c.execute(query)

#query="""INSERT INTO Employee(Emp_Id,Emp_Name,Dept_Id,Salary,City)
            #VALUES
            #(1,'Rakesh',3,30000,'Kochi'),
            #(2,'Sumesh',3,30000,'Kochi'),
            #(3,'ramesh',4,40000,'Trivandrum'),
            #(4,'Rahul',4,40000,'Thrissur'),
            #(5,'Rinzi',4,40000,'Kollam');
            #"""
#c.execute(query)

#query="""CREATE TABLE Department( 
     #Dept_Id INTEGER NOT NULL PRIMARY KEY, 
     #Dept_Name TEXT NOT NULL  
     #);"""
#c.execute(query)
#query="""INSERT INTO Department(Dept_id,Dept_name)
        #VALUES
        #(1,'Human Resources'),
        #(2,'Maintenence'),
        #(3,'IT'),
        #(4,'Marketing'),
        #(5,'Public Relations');"""
#c.execute(query)



def get_employee(Emp_id):
    with conn:
         select_query = """select Emp_Id,Emp_Name,Dept_Id,Salary from Employee where Emp_Id = ?"""
         c.execute(select_query,(Emp_id,))
         records=c.fetchall()
         print("Printing Employee details:")
         for row in records:
             print("Employee Id--->",row[0])
             print("Employee Name--->",row[1])
             print("Dept Id--->",row[2])
             print("salary--->",row[3])

def get_allemployee():
    with conn:
         select_query = """select Emp_Id,Emp_Name,Dept_Id,Salary from Employee """
         c.execute(select_query)
         records=c.fetchall()
         print("Printing Employee details:")
         for row in records:
             print("Employee Id--->",row[0])
             print("Employee Name--->",row[1])
             print("Dept Id--->",row[2])
             print("salary--->",row[3])
             print("\n\n")
def name_starting():
    with conn:
        select_query="select * from Employee where Emp_Name like 'J%' "
        c.execute(select_query)
        records=c.fetchall()
        print("Printing Employee details with name starting with letter J:")
        for row in records:
             print("Employee Id--->",row[0])
             print("Employee Name--->",row[1])
             print("Dept Id--->",row[2])
             print("salary--->",row[3])
             print("city--->",row[4])
             print("\n\n")

def change_name(Emp_id):
    with conn:
        new_name=input("enter new name:")
        query="""UPDATE Employee
                SET Emp_name=?
                WHERE Emp_id=?
                """
        c.execute(query,(new_name,Emp_id))

def dept_employees(Dept_id):
    with conn:
        print("printing Details of employees in the department:")
        query="select * from Employee where Dept_id=?"
        c.execute(query,(Dept_id,))
        records=c.fetchall()
      
        for row in records:
             print("Employee Id--->",row[0])
             print("Employee Name--->",row[1])
             print("salary--->",row[3])
             print("city--->",row[4])
             print("\n\n")



something = False
while not something:
    choice=int(input("Enter Choice:\n 1-->Print all employees details\n2-->print according to employee id\n3-->Change name\n4-->Print employees name starting with J\n5-->Print Empoyees in a department\n"))

    if choice==1:
        get_allemployee()
    elif choice==2:
        e_id=int(input("enter emp id"))
        get_employee(e_id)
    elif choice==3:
        e_id=int(input("enter e_id"))
        change_name(e_id)
    elif choice==4:
        name_starting()
    elif choice==5:
        d_id=int(input("enter department id"))
        dept_employees(d_id)
    else:
        print("wrong choice")
    inout = input('type "y" to continue: ')
    if inout != 'y':
        something = True



conn.commit()
conn.close()