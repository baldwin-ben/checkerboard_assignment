from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

@app.route('/')
def checkers():
    return render_template("index.html", height = 8, width = 8, color1 = "red", color2 = "blue")

@app.route('/4')
def checkers_8x4():
    return render_template("index.html", height = 4, width = 8, color1 = "red", color2 = "blue")

@app.route('/<int:height>/<int:width>') #Getting variable (height, width) from url to pass in it as parameters to your function
def checkers_x_y(height, width):
    return render_template("index.html", height = height, width = width, color1 = "red", color2 = "blue") #customize width and height in url path

@app.route('/<int:height>/<int:width>/<color1>/<color2>') #Getting variables (height, width, color1, color2) from url to pass in it as parameters to your function
def checkers_x_y_color_1_2(height, width, color1, color2):
    return render_template("index.html", height = height, width = width, color1 = color1, color2 = color2) #customize width, height, colors in url path


if __name__ == "__main__":
    app.run(debug=True)