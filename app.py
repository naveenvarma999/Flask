from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    print("✅ HOME ROUTE CALLED")
    return render_template("home.html")

@app.route('/about')
def about():
    print("✅ ABOUT ROUTE CALLED")
    return render_template("about.html")

if __name__ == "__main__":
    print("🔥 ROUTES LOADED:")
    print(app.url_map)
    app.run(debug=True)
