import json
import urllib.request

# Menggunakan endpoint langsung ke direktori data game
PLAYGAMA_SOURCE_URL = "https://playgama.com/api/games" # atau sumber katalog aktif
OUTPUT_FILENAME = "playgama.json"

def main():
    games_list = []
    try:
        req = urllib.request.Request(PLAYGAMA_SOURCE_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            res_data = response.read().decode('utf-8')
            data = json.loads(res_data)
            if isinstance(data, list):
                games_list = data
            elif isinstance(data, dict):
                games_list = data.get('games', data.get('hits', []))
    except Exception as e:
        print(f"Error fetching data: {e}")

    final_output = {
        "metadata": {"status": "active"},
        "games": games_list
    }

    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
        json.dump(final_output, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
