from flask import Flask, render_template, request, send_from_directory, jsonify
from AudioStoryGenerator import AudioStoryGenerator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        topic = request.form['topic']
        generator = AudioStoryGenerator()
        output_file = generator.generate(topic)
        return jsonify({"status": "success", "file": output_file})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)