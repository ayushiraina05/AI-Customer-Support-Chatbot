from flask import Flask, render_template, request

app = Flask(__name__)

faq = {
    "hi": "Hello! How can I help you?",
    "return policy": "Our return policy is valid for 7 days.",
    "track order": "You can track your order from your account section.",
    "payment methods": "We accept UPI, Debit Card, Credit Card and Net Banking."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():

    user_input = request.form["msg"].lower()

    # 🔹 Fake Real-time API Integration
    if "order" in user_input:
        return "Your order #1234 is currently Out for Delivery 🚚"

    if "balance" in user_input:
        return "Your current account balance is ₹15,000."

    # 🔹 Predefined FAQ Matching
    for key in faq:
        if key in user_input:
            return faq[key]

    return "Sorry, I didn't understand that."

if __name__ == "__main__":
    app.run()
