import itertools

from flask import Flask, render_template, Response, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import io

import requests
app = Flask(__name__)



access_key = ["t3BSzSqU8bNBu0ggt0EXzSIKSitFP2oLYJ-dInXYInQ",
              "pErhR3ajErghfoXQon5eT_FL-DL6DxSMtqfTUuBl6Fw",
              "kKBKs902JOIwxnWKjMm9N8MMFBWEcmZnkB5FxjHk500",
              "MEROpTc4LJKsTSIfQpA3Ki3IpqmTk6FSNWCgs3JJr5Q",
              "fh95VJ6hGAmIOkL6oLtPj971FtVNWmm2C29d6GRaAgM"]

list_of_facts = []

access_keys = itertools.cycle(access_key)

def get_random_fact():
    facts = []
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    response = requests.get(url)
    data = response.json()
    return data["text"]

def get_image(query):
    url = "https://api.unsplash.com/search/photos"

    params = {
    'client_id': next(access_keys), # Your access key
    'per_page' : 1, # Number of photos to fetch per request
    'page' : 1, # The page number to fetch
    'query': query }

    response = requests.get(url, params=params)
    photo = response.json() ['results' ] [0] ['urls' ] ['raw' ]
    return photo

@app.route("/")
def index():
    facts = get_random_fact()
    image = get_image(facts)
    list_of_facts.append(facts)
    return render_template('landing.html', facts_=facts, image_=image, facted=list_of_facts)

@app.route("/fetch")
def fetcher():
    facts = get_random_fact()
    image = get_image(facts)
    list_of_facts.append(facts)
    fact_of_list = list_of_facts
    return jsonify({"fact": facts,
                    "image": image,
                    "list": fact_of_list})

if __name__ == "__main__":
    app.run(debug=True)