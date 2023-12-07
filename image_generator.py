import requests

access_key = ""

# Request to Unsplash API
def  get_random_image(query):
    orientation = "landscape"
    url = f"https://api.unsplash.com/photos/random/?query={query}&orientation={orientation}&client_id={access_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data and 'urls' in data:
            return data['urls']['regular']
    else:
        return f"Error: {response.status_code}"