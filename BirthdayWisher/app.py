from flask import Flask, request, render_template
import csv

app = Flask(__name__)


def save_to_csv(data):
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        dob = request.form['dob']
        save_to_csv([name, email, dob])
        return render_template("result.html")
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
