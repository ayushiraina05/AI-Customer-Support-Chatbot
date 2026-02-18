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
    response = "Sorry, I didn't understand that."

    for key in faq:
        if key in user_input:
            response = faq[key]

    return response

if __name__ == "__main__":
    app.run()
