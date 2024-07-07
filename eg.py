import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_csv_data():
    data = []
    with open('heart.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            data = read_csv_data()
            filtered_data = [row for row in data if row['Name'] == name]
            return render_template('index1.html', data=filtered_data)

    return render_template('index1.html', data=[])

if __name__ == '__main__':
    app.run(debug=True)
