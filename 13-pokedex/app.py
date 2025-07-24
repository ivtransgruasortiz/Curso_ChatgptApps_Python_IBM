from flask import Flask, render_template, abort
import requests

app = Flask(__name__)

POKEAPI_BASE = "https://pokeapi.co/api/v2"

# Obtener los 151 primeros Pokémon
def get_all_pokemons():
    url = f"{POKEAPI_BASE}/pokemon?limit=151"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results = data['results']
        pokemons = []
        for index, p in enumerate(results, start=1):
            pokemons.append({
                'id': index,
                'name': p['name'].capitalize()
            })
        return pokemons
    return []

# Obtener detalles de un Pokémon concreto por ID
def get_pokemon_by_id(pokemon_id):
    # Info general
    poke_response = requests.get(f"{POKEAPI_BASE}/pokemon/{pokemon_id}")
    species_response = requests.get(f"{POKEAPI_BASE}/pokemon-species/{pokemon_id}")

    if poke_response.status_code != 200 or species_response.status_code != 200:
        return None

    poke_data = poke_response.json()
    species_data = species_response.json()

    # Extraer habilidades
    abilities = [a['ability']['name'].capitalize() for a in poke_data['abilities']]

    # Extraer descripción en español
    descriptions = [entry['flavor_text'] for entry in species_data['flavor_text_entries']
                    if entry['language']['name'] == 'es']
    description = descriptions[0].replace('\n', ' ').replace('\f', ' ') if descriptions else "Sin descripción."

    return {
        'id': pokemon_id,
        'name': poke_data['name'].capitalize(),
        'abilities': abilities,
        'description': description,
        'image': poke_data['sprites']['other']['official-artwork']['front_default']
    }

@app.route('/')
def index():
    pokemons = get_all_pokemons()
    return render_template('index.html', pokemons=pokemons)

@app.route('/pokemon/<int:pokemon_id>')
def pokemon_detail(pokemon_id):
    pokemon = get_pokemon_by_id(pokemon_id)
    if not pokemon:
        abort(404)
    return render_template('pokemon.html', pokemon=pokemon)

if __name__ == '__main__':
    app.run(debug=True)
