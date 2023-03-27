from flask import Flask

app = Flask(__name__)

@app.route('/api1/', methods=['GET', 'POST'])
def fonapi1():
    return "Api1 cevap veriyor"

@app.route('/api2/', methods=['GET', 'POST'])
def fonapi2():
    return "Api2 cevap veriyor"

# This is a comment
# This is a comment too ! 
# This is a comment too !!
if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
