from flask import Flask
import random
app = Flask(__name__)


@app.route("/")
def hello():
    # return "Hello World!"
    lists = ""
    for i in range(1, 667):
        i = random.randrange(1, 667)
        lists += f"<li>{i}</li>"
    return f"<ol>{lists}</ol>"

# ссылка на гитхаб с этим кодом: 


if __name__ == "__main__":
    app.run()