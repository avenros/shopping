from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="f4uIDRBJyZN2vrKtKt6PjNPk7fOYDur",
)
app.config.from_prefixed_env()

@app.route("/")
def index():
    return render_template("views/index.html")

if __name__ == '__main__':
    app.run(debug=True)