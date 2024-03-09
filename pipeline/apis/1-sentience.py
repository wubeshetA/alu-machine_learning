#!/usr/bin/env python3
""" Return list of ships"""


import requests


def sentientPlanets():
    """ Return list of names of the home planets of all sentient species.
    """

    res = requests.get('https://swapi-api.alx-tools.com/species/')

    output = []
    while res.status_code == 200:
        res = res.json()
        for species in res['results']:
            if species['designation'] == "sentient" or\
                    species['classification'] == "sentient":
                # send a request to homeworld
                if species['homeworld'] is None:
                    continue
                print(species['homeworld'])
                planet = requests.get(species['homeworld'])
                output.append(planet.json()['name'])
        try:
            res = requests.get(res['next'])
        except Exception:
            break
    return output
