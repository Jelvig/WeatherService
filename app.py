from flask import Flask, request
from umbrella import makeUmbrellaDecision
app = Flask(__name__)

@app.route('/')
def home():
    city = request.args.get('city')   # make sure to add '/?city=boston&country=us' 
    if makeUmbrellaDecision( city, 'us'):
        return f'Bring an umbrella in {city}'
    else:
        return f'No need for an umbrella in {city}'
