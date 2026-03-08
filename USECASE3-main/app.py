from flask import Flask, render_template, request, send_file
import agents
import os
from reportlab.pdfgen import canvas

app = Flask(__name__)

latest_result = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/input")
def input_page():
    return render_template("input.html")

@app.route("/predict", methods=["POST"])
def predict():
    premium = int(request.form["premium"])
    accidents = int(request.form["accidents"])
    age = int(request.form["age"])
    miles = int(request.form["miles"])

    risk = agents.risk_profiler(accidents)
    conversion = agents.conversion_predictor()
    advice = agents.premium_advisor(premium)
    decision = agents.decision_router(risk, conversion)

    global latest_result
    latest_result = {
        "premium": premium,
        "accidents": accidents,
        "age": age,
        "miles": miles,
        "risk": risk,
        "conversion": conversion,
        "advice": advice,
        "decision": decision
    }

    return render_template(
        "result.html",
        risk=risk,
        conversion=conversion,
        advice=advice,
        decision=decision
    )

@app.route("/download")
def download():
    file = "report.pdf"
    c = canvas.Canvas(file)

    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, 780, "AI Insurance Evaluation Report")

    c.setFont("Helvetica", 12)
    y = 720
    for k, v in latest_result.items():
        c.drawString(100, y, f"{k.upper()} : {v}")
        y -= 25

    c.save()
    return send_file(file, as_attachment=True)

# IMPORTANT FOR RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
