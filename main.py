from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/lic')
def license():
  return render_template('lic.html')

app.run(host='0.0.0.0', port=8080)
