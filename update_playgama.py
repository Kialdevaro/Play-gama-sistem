import requests
import json
import os

def fetch_all_playgama_games():
    all_hits = []
    page = 1
    limit = 100  # Ambil per batch
    
    # Header untuk mencegah blokir/error HTTP 403 dari Playgama
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json"
    }

    print("Memulai fetching database dari Playgama...")

    while True:
        # Endpoint API Playgama dengan Pagination
        url = f"https://api.playgama.com/v1/games?page={page}&limit={limit}"
        
        try:
            response = requests.get(url, headers=headers, timeout=15)
            
            if response.status_code != 200:
                print(f" Gagal pada halaman {page}, Status Code: {response.status_code}")
                break
                
            data = response.json()
            
            # Cek berbagai struktur JSON Playgama
            hits = []
            if isinstance(data, dict):
                if "segments" in data and len(data["segments"]) > 0 and "hits" in data["segments"][0]:
                    hits = data["segments"][0]["hits"]
                elif "hits" in data:
                    hits = data["hits"]
                elif "data" in data:
                    hits = data["data"]
            elif isinstance(data, list):
                hits = data

            if not hits:
                print(f" Selesai! Tidak ada data lagi di halaman {page}.")
                break

            all_hits.extend(hits)
            print(f" Berhasil mengambil halaman {page} ({len(hits)} game). Total saat ini: {len(all_hits)}")
            
            # Jika jumlah game kurang dari limit, berarti sudah halaman terakhir
            if len(hits) < limit:
                break
                
            page += 1

        except Exception as e:
            print(f" Error saat fetching halaman {page}: {e}")
            break

    return all_hits

def main():
    games = fetch_all_playgama_games()
    
    if len(games) == 0:
        print(" Error: Total game yang didapatkan 0. Proses dibatalkan agar games.json tidak rusak.")
        return

    # Buat format JSON yang kompatibel dengan script blog kamu
    final_data = {
        "segments": [
            {
                "hits": games
            }
        ]
    }

    # Simpan ke games.json
    output_file = "games.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)

    print(f" SUCCESS! Berhasil menyimpan {len(games)} game ke {output_file}")

if __name__ == "__main__":
    main()
