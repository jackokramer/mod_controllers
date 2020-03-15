from config import app
from controller_functions import index, register_new_user
app.add_url_rule("/", view_func=index)
app.add_url_rule("/adddojo", view_func=add_dojo, methods=["POST"])
app.add_url_rule("/add_ninja", view_func=add_ninja, methods=["POST"])

@app.route("/")


@app.route("/adddojo", methods=['POST'])


@app.route("/add_ninja", methods=['POST'])



