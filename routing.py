What is Routing? 

Routing means deciding which page (or output) to show when someone visits a particular URL.

In other words:

URL → Function → Output

We tell Flask:

When the user goes to this URL, run this function, and show this result.






# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "hey Naveen"

# @app.route("/about")
# def about():
#     return "iam a data scientist"
# @app.route("/contact")
# def contact():
#     return "90239u93e893"

# if __name__=="__main__":
#     app.run(debug=True)


# BASIC ROUTING

# from flask import Flask
# app = Flask(__name__)
# @app.route("/home")
# def home():
#     return "Pochampally"

# if __name__=="__main__":
#     app.run(debug=True)



# # Routing with variables

# from flask import Flask
# app=Flask(__name__)
# @app.route('/user/<name>')
# def user(name):
#     return f"hello, {name}"

# if __name__=="__main__":
#     app.run(debug=True)



#type specific Routes
# from flask import Flask
# app=Flask(__name__)
# @app.route("/age/<int:age>")
# def show_age(age):
#     return f"My age is :{age}"
# if __name__=="__main__":
#     app.run(debug=True)




#  Multiple Routes Leading to Same Function

# we can allow more than one URL for the same function:
# from flask import Flask
# app=Flask(__name__)
# @app.route("/")
# @app.route("/home")
# def home():
#     return "Colchester"
# if __name__=="__main__":
#     app.run(debug=True)




# URL Query Parameters

# we are sending numbers to Flask using the URL,
#Flask receives those numbers and adds them.


# from flask import Flask,request
# app=Flask(__name__)
# @app.route('/add')
# def add():
#     a = request.args.get('a', type=int)
#     b = request.args.get("b", type=int)
#     return str(a + b)
# if __name__=="__main__":
#     app.run(debug=True)


# 5) POST vs GET Routes
# GET → Browser / URL
# POST → Form / API

# GET = ask for a page, POST = send data to the server.

# from flask import Flask,request
# app=Flask(__name__)
# @app.route("/login",methods =["GET","POST"])
# def login():
#     if request.method=="GET":
#         return "login page Opened"
#     if request.method=="POST":
#         return "Form submitted"
    
# if __name__=="__main__":
#     app.run(debug='True')
