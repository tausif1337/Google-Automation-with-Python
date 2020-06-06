#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        employee_file = csv.DictReader(open(csv_file_location), dialect='empDia$
        employee_list=[]
        for data in employee_file:
                employee_list.append(data)
        return employee_list

employee_list = read_employees('/home/student-02-630e8f6b8e98/data/employees.cs$
#print(employee_list) - To be removed after first step

def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data['Department'])
        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = department_list.count(depart$
        return department_data

dictionary = process_data(employee_list)
print(dictionary)

def write_report(dictionary, report_file):
        with open(report_file, 'w+') as f:
          for department_name in set(department_list):
                department_data[department_name] = department_list.count(depart$
        return department_data

dictionary = process_data(employee_list)
print(dictionary)

def write_report(dictionary, report_file):
        with open(report_file, 'w+') as f:
                for k in sorted(dictionary):
                        f.write(str(k)+':'+str(dictionary[k])+'\n')
                f.close()
write_report(dictionary,'/home/student-02-630e8f6b8e98/test_report.txt')

