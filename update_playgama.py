import json
import urllib.request

# URL API katalog Playgama yang asli
PLAYGAMA_SOURCE_URL = "https://widgets.playgama.com/"
OUTPUT_FILENAME = "playgama.json"

def main():
    games_list = []
    try:
        req = urllib.request.Request(PLAYGAMA_SOURCE_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            if isinstance(data, list):
                games_list = data
            elif 'segments' in data and len(data['segments']) > 0:
                games_list = data['segments'][0].get('hits', [])
            elif 'hits' in data:
                games_list = data['hits']
            elif 'games' in data:
                games_list = data['games']
    except Exception as e:
        print(f"Error: {e}")

    final_output = {
        "metadata": {"status": "active"},
        "games": games_list
    }

    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
        json.dump(final_output, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
