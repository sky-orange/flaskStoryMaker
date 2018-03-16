from flask import Flask, request, render_template, redirect
import json
app = Flask(__name__)

urlCentreText = {"0" : "Start your story"}

@app.route("/")
def start():
    return redirect("0")

@app.route("/<url>", methods=["POST", "GET"])
def story_page(url):
    global urlCentreText
    if request.method == "POST":
        if "newUrl" in request.form:
            urlCentreText[request.form["newUrl"]] = request.form["cellInput"]
        elif "save" in request.form:
            with open("savedStoryText.json", "w") as outfile:
                json.dump(urlCentreText, outfile)
        elif "load" in request.form:
            with open("savedStoryText.json") as json_data:
                urlCentreText = json.load(json_data)

    return render_template("storyTemplate.html",
                           url=url,
                           dictionary=urlCentreText)

@app.route("/<url>/storysofar")
def story_so_far(url):
    urlList = []
    for x in range(1, len(url)):
        urlList.append(url[:x + 1])
    return render_template("storySoFar.html",
                           urlList=urlList,
                           dictionary=urlCentreText)



