from flask import Flask, render_template

app = Flask(__name__)

# -----------------------------
# Home
# -----------------------------
@app.route("/")
def home():
    return render_template("customer/home.html")


# -----------------------------
# Services
# -----------------------------
@app.route("/services")
def services():
    return render_template("customer/services.html")


# -----------------------------
# Price List
# -----------------------------
@app.route("/pricing")
def pricing():
    return render_template("customer/pricing.html")


# -----------------------------
# Service Request (Main Page)
# -----------------------------
@app.route("/service-request")
def service_request():
    return render_template("customer/service_request.html")


# -----------------------------
# Xerox Order
# -----------------------------
@app.route("/xerox-order")
def xerox_order():
    return render_template("customer/xerox_order.html")


# -----------------------------
# Online Services
# -----------------------------
@app.route("/online-service")
def online_service():
    return render_template("customer/online_service.html")


# -----------------------------
# Mobile Repair
# -----------------------------
@app.route("/mobile-repair")
def mobile_repair():
    return render_template("customer/mobile_repair.html")


# -----------------------------
# Contact
# -----------------------------
@app.route("/contact")
def contact():
    return render_template("customer/contact.html")


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)