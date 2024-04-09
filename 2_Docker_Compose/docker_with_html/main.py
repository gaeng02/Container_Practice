from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def show_lists():
    try : 
        response = requests.get(f"http://database:5001/get_data")
        data = response.json() if response.status_code == 200 else []
        print(data)
        return render_template('index.html', data = data)
    except : 
        return render_template('index.html', data=data)

    return render_template('index.html', data=data)


if (__name__ == '__main__') :
    app.run(host="0.0.0.0", port=5000)
