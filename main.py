from flask import Flask, render_template, request, send_from_directory, jsonify
import os
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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)