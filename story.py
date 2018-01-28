from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

urlCentreText = {"start" : "start"}

cellOneInputDictionary = {}
cellTwoInputDictionary = {}
cellThreeInputDictionary = {}
cellFourInputDictionary = {}

DictOfCellInputDicts = {"1" : cellOneInputDictionary,
                        "2" : cellTwoInputDictionary,
                        "3" : cellThreeInputDictionary,
                        "4" : cellFourInputDictionary}
@app.route("/")
def start():
    return redirect("start")

@app.route("/<url>", methods=["POST", "GET"])
def story_page(url):
    url = url
    page_cell_inputs = {"centre" : url}

    if request.method == "POST":
        if "cellInput_1" in request.form:
            cellOneInputDictionary[url + "1"] = request.form["cellInput_1"]
        if "cellInput_2" in request.form:
            cellTwoInputDictionary[url]= request.form["cellInput_2"]
        if "cellInput_3" in request.form:
            cellThreeInputDictionary[url] = request.form["cellInput_3"]
        if "cellInput_4" in request.form:
            cellFourInputDictionary[url] = request.form["cellInput_4"]

    for cell in DictOfCellInputDicts:
        if url in DictOfCellInputDicts[cell]:
            page_cell_inputs[cell] = (DictOfCellInputDicts[cell][url])
        else:
            page_cell_inputs[cell] = None

    return render_template("storyTemplate.html",
                           url=url,
                           cellInput_1=page_cell_inputs["1"],
                           cellInput_2=page_cell_inputs["2"],
                           cellInput_3=page_cell_inputs["3"],
                           cellInput_4=page_cell_inputs["4"],
                           centreCellText=page_cell_inputs["centre"])



