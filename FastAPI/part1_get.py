from fastapi import FastAPI

# app object
app=FastAPI()

# 1. Home API
@app.get("/")
def home_api():
    return {
        "message":"welcome to super30 FASTAPI"
    }

# 2. student api
@app.get("/student")
def student_api():
    return {
        "name":"yamuna",
        "role":"student",
         "course":["python","datascience"]
    }

# 3. course api
@app.get("/course")
def course_api():
    return {
        "course_name":"System Design",
        "mentor":"yamuna",
        "duration":"3 months",
        "topics":["low level and high level design","softaware development"]
    }

#4. skills api
@app.get("/skills")
def skills_api():
    return {
        "skills":["python","sql","AWS","Docker","AI Automation"]
    }

# 5. addition api
@app.get("/add/{num1}/{num2}")
def addition(num1:int,num2:int):
    return {
        "result":num1+num2
}

# 6. multiplication api
@app.get("/multiply/{num1}/{num2}")
def multiply(num1:int,num2:int):
    return {
        "result":num1*num2
    }

# 7. square api
@app.get("/square/{sides}")
def square(sides:int):
    return {
        "number":sides,
        "square":sides**2
    }

# 8. Even/Odd API
@app.get("/check")
def check(num:int):
    if num%2==0:
        return {
            "number":num,
            "type":"even"
        }
    else:
        return {"number":num,"type":"odd"}

# 9. Age API
@app.get("/age/{age}")
def age_check(age:int):
    if age<=0:
        return {"message":"enter valid age"}
    elif 1<=age<=12:
        return{"age":age,"message":"your are child"}
    elif 13<=age<=17:
        return{"age":age,"message":"your are teenger"}
    elif 18<=age<=39:
        return{"age":age,"message":"your are an adult"}
    elif 40<= age<=59:
        return{"age":age,"message":"your are middle aged"}
    else:
        return{"age":age,"message":"your are a senior citizen"}
        
        
# 10. Table API
@app.get("/table/{num}")
def tables(num:int):
    tables=[]
    for i in range(1,11):
        tables.append(f"{num} x {i} = {num*i}")
    return {
        "number":num,
        "table":tables
    }

#  11. Profile API
@app.get("/profile/{name}/{age}")
def profile(name:str,age:int):
    return {
        "name":name,
        "age":age
    }

# 12 Number Analysis API
@app.get("/number/{number}")
def number_anaylsis(number:int):
    if number%2==0:
        return {
            "number":number,
            "square":number**2,
            "cube": number**3,
            "even":True
        }
    else:
        return {
            "number":number,
            "square":number**2,
            "cube": number**3,
            "even":False
        }