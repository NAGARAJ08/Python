# Json - JavaScript object notation 
import json


def explore_json():

    # Serilization:  [json.dumps] transformation of data into a series of bytes
    # Deserilization: [json.loads] conversion of JSON objects into their respective Python objects

    # json.dumps = obj to str
    # json.loads = str to python object

    # Json String
    student = '{"id":12, "name":"WBC","Subject": "Defence", "Graduated":true}'

    # Converting the json string to dictionary
    stu_dict = json.loads(student)
    print(stu_dict)
    print(type(stu_dict))

    # Convert dictionary to Json using dumps

    
    stu_json = json.dumps(stu_dict,indent=4)
    print(stu_json)
    print(type(stu_json))

    print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True,indent=4))

    # Compact
    print(json.dumps([1,4,3,2,{"c": 0, "b": 0, "a": 0}], sort_keys=True))



def employee():

    a = {"Name":"NK",
         "Age":22,
         "Salary":25000}
    b = json.dumps(a,indent=4)
    print(b)
    print(type(b))

    



def Specified_sep():
     dict = {1:'Hello',
            2:'This',
            3:'is',
            4:'Json'}
     d = json.dumps(dict,indent=4,separators=(". "," = "))
     print(d)


def dumps_func():

    dict = {(1,2,3):'Hello',
            2:'This',
            3:'is',
            4:'Json'}

    # print(json.dumps(dict,indent=4))    this gives error as our dict contains tuple as key 
    # by default skipkeys is set to False
    print(json.dumps(dict,skipkeys=True,indent=4))    
    #this above line removes those key-value pairs and prints other basic data type keys



def loads_func():

    data = """{

    "Name": "ABC",
    "Contact":"9389438493",
    "Email":"a.b.c.@gmail.com"
    
    }"""

    # print(type(data))

    D = json.loads(data)

    print(D)
    print(type(D))

    print(D["Email"])


    
# explore_json()
# employee()
# Specified_sep()
# dumps_func()
loads_func()
