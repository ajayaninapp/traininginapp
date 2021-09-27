import sqlite3

conn=sqlite3.connect('hospital.db')

c = conn.cursor()
#c.execute("""CREATE TABLE Doctor ( 
     #Doctor_Id INTEGER NOT NULL PRIMARY KEY, 
     #Doctor_Name TEXT NOT NULL, 
     #Hospital_Id INTEGER NOT NULL, 
     #Joining_Date TEXT NOT NULL, 
     #Speciality TEXT NOT NULL, 
     #Salary INTEGER NOT NULL,
     #Experience INTEGER
#);""")
#c.execute("""INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience) 
#VALUES 
#('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL), 
#('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL), 
#('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL), 
#('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL), 
#('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL), 
#('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL), 
#('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL), 
#('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL);""")
#c.execute("""CREATE TABLE Hospital (
    #Hospital_Id INTEGER NOT NULL PRIMARY KEY, 
    #Hospital_Name TEXT NOT NULL, 
    #Bed_Count INTEGER NOT NULL
#);""")
#c.execute("""INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count) 
#VALUES 
#('1', 'Mayo Clinic', 200), 
#('2', 'Cleveland Clinic', 400), 
#('3', 'Johns Hopkins', 1000), 
#('4', 'UCLA Medical Center', 1500);""")


#conn.commit()

def get_specialist_doctors_list(speciality, salary):

    with conn:

        c = conn.cursor()
        sql_select_query = """select * from Doctor where Speciality = ? and Salary > ?"""
        c.execute(sql_select_query, (speciality, salary))
        records = c.fetchall()
        print("Printing doctors whose specialty is", speciality, "and salary greater than", salary, "\n")
        for row in records:
            print("Doctor Id: ", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")

def get_hospital_name(hospital_id):
    with conn:
        c = conn.cursor()
        select_query = """select * from Hospital where Hospital_Id = ?"""
        c.execute(select_query, (hospital_id,))
        record = c.fetchone()
        return record[1]

def get_doctors(hospital_id):   
    with conn:

        hospital_name = get_hospital_name(hospital_id)
        c = conn.cursor()
        sql_select_query = """select * from Doctor where Hospital_Id = ?"""
        c.execute(sql_select_query, (hospital_id,))
        records = c.fetchall()  

        print("Printing Doctors of ", hospital_name, "Hospital")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Hospital Name:", hospital_name)
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")       
        
    
        
      
        
choice=int(input("What do you choose\n1----> Get specialist doctor list\n2-->Get Doctors in a hospital\n"))
if choice==1:
    speciality=(input("enter speciality-->"))
    salary=int(input("\nenter salary-->"))
    get_specialist_doctors_list(speciality, salary)
elif choice==2:
    h_id=int(input("enter hospital id"))
    get_doctors(h_id)
else:
    print("wrong choice")


        



conn.close()
