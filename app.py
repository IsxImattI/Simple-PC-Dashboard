from dashboard import cpu_usage, memory_usage
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/stats')
def stats():
    current_cpu_usage = cpu_usage()
    current_memory_usage = memory_usage()
    return jsonify(cpu_usage=current_cpu_usage, memory_usage=current_memory_usage)

if __name__ == '__main__':
    app.run(debug=True)