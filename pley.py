from flask import Flask, render_template, request
import reviewz
import os

app = Flask(__name__)

@app.route("/")
def hello():
    user_request1 = request.values.get('biz')
    user_request2 = request.values.get('biz1')
    get_business=None
    if user_request1 and user_request2:
        get_business = reviewz.lookup(user_request1,user_request2)
    return render_template('hello.html', orange=get_business)


if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)