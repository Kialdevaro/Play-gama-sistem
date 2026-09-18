import json
import os

# Contoh daftar game otomatis (Anda bisa sesuaikan sumber pengambilannya dari API atau scrape)
# Pastikan data selalu terisi dan tidak kosong agar tidak merusak blog
new_games_data = [
    {
        "title": "Piece of Game: Merge & Bake",
        "category": "Puzzle",
        "iframeUrl": "https://playgama.com/embed/piece-of-cake-merge-and-bake"
    },
    {
        "title": "Hazmob FPS: Online Shooter",
        "category": "Action",
        "iframeUrl": "https://playgama.com/embed/hazmob-fps-online-shooter"
    }
]

# Validasi keamanan: Jika data 0/kosong, hentikan proses agar games.json tidak jadi 0 (kosong)
if not new_games_data or len(new_games_data) == 0:
    print("Error: Data game kosong! Proses update dibatalkan.")
    exit(1)

# Simpan ke file games.json
file_path = "games.json"
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(new_games_data, f, ensure_ascii=False, indent=4)

print("Berhasil memperbarui games.json dengan", len(new_games_data), "game.")
