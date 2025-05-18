from flask import Flask, render_template, request
import web_tester

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test", methods=["POST"])
def test():
    target_url = request.form["url"]

    # 🔥 Testleri çalıştırıyoruz!
    results = web_tester.run_tests(target_url)

    return render_template("results.html", results=results)

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # 📌 5001 portunu kullanıyoruz!
