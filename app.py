from flask import Flask, render_template
import random
import time

app = Flask(__name__)

# list of cat images
images = [
    "https://s3.aleatori.cat/a37032b754d0962441d46e5ac13a71abc6cf2ea24d8f86eea12bbb061944dc8e.jpg",
    "https://s3.aleatori.cat/ba9f9e0bfb15223d1cabffceaae06ffeb002e1014f6bb07bd67c5080a464e36f.jpg",
    "https://s3.aleatori.cat/9751046fc3908ab44df20ba39b073f3c1c9ebc48863b85c981390982cd2fd7ca.jpg",
    "https://s3.aleatori.cat/2e3bf510be28e35ae9896adff3dac0ee8e84277cec6f9f083d066cace3314fa3.jpg",
    "https://s3.aleatori.cat/c7e615cd1e3dd2418f75b3fbefd9e996b571d849d469dcfcce8c70d5f4e75328.jpg"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

@app.route('/make_cpu_busy/<int:t>')
def make_cpu_busy(t: int):
    """Make the CPU busy for t seconds"""
    start = time.time()
    while time.time() - start < t:
        pass
    return f"CPU was busy for {t} seconds!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
