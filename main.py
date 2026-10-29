import os
from flask import Flask, render_template
from utils import get_random_verse


app = Flask(__name__)


@app.route("/")
def home():
  verset_photo_random = get_random_verse(source_configuration="configuration/versete_imagini.json")
  return render_template("verset_imagine.html", data=verset_photo_random)


if __name__ == "__main__":
   port = int(os.environ.get("PORT", 10000))
   app.run(host="0.0.0.0", port=port)
