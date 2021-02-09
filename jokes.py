from flask import Flask, render_template, app,url_for
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    image= "<img src="+ response["icon_url"] +">"

    return "<strong>Random joke from chuck norris: </strong>" + response['value'] +image

if __name__ == "__main__":
    app.run(debug=True)
