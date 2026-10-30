import os
from flask import Flask, render_template
from utils import get_random_verse


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(
  __name__,
  template_folder=os.path.join(project_root, "templates"),
  static_folder=os.path.join(project_root, "static"),
)

json_path = os.path.join(
  project_root, "configuration", "versete_imagini.json"
)


@app.route("/")
def home():
  verset_photo_random = get_random_verse(source_configuration=json_path)
  return render_template("verset_imagine.html", data=verset_photo_random)


if __name__ == "__main__":
   port = int(os.environ.get("PORT", 10000))
   app.run(host="0.0.0.0", port=port)
