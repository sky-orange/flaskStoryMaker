from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

urlCentreText = {"0" : "Start your story"}

@app.route("/")
def start():
    return redirect("0")

@app.route("/<url>", methods=["POST", "GET"])
def story_page(url):
    if request.method == "POST":
        urlCentreText[request.form["newUrl"]] = request.form["cellInput"]

    return render_template("storyTemplate.html",
                           url=url,
                           dictionary=urlCentreText)



