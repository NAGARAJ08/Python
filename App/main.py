from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def msg():
    return "Welcome "


@app.route('/square/<int:n>')
def square(n):
    ans = n ** 2

    res = {
        "Number": n,
        "Squared Value": ans
    }
    return jsonify(res)


@app.route('/add/<a>/<b>')
def add(a, b):
    ans = int(a) + int(b)
    res = {
        "Number 1": a,
        "Number 2": b,
        "Summation of Two Numbers : ": ans
    }
    return jsonify(res)


@app.route('/sub/<a>/<b>')
def sub(a, b):
    ans = int(a) - int(b)
    res = {
        "Number 1": a,
        "Number 2": b,
        "Difference of Two Numbers : ": ans
    }
    return jsonify(res)


@app.route('/mul/<a>/<b>')
def mul(a, b):
    ans = int(a) * int(b)
    res = {
        "Number 1": a,
        "Number 2": b,
        "Product of Two Numbers : ": ans
    }
    return jsonify(res)


@app.route('/Div/<a>/<b>')
def div(a, b):
    ans = int(a) / int(b)
    res = {
        "Number 1": a,
        "Number 2": b,
        "Division of Two Numbers : ": ans
    }
    return jsonify(res)


@app.route('/even-or-odd/<int:n>')
def even_or_odd(n):
    if n % 2 == 0:
        ans = "The Number is Even"
    else:
        ans = "The Number is ODD"

    res = {

        "Number": n,
        "Verdict": ans
    }
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)