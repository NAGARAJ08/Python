from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')

def msg():
    return "Welcome "

@app.route('/square/<int:n>')
def sum(n):
    ans = n**2
    
    res = {
        "Number":n,
        "Squared Value":ans
    }
    return jsonify(res)



@app.route('/even-or-odd/<int:n>')
def even_or_odd(n):
    
    if n%2==0:
        ans =  "The Number is Even"
    else:
        ans =  "The Number is ODD"
    
    res = {
        
        "Number":n,
        "Verdict":ans
    }
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)