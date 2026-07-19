# Kamus EN-ID (SQL Edition)

Kamus dua arah (Inggris ⇄ Indonesia) dengan data disimpan di **database SQLite asli** (`kamus.db`). Setiap kata punya *part of speech* (noun, verb, dst) dan contoh kalimat.

## Arsitektur

- **Database**: SQLite (`kamus.db`) — satu tabel `words` dengan kolom `english`, `indonesian`, `pos`, `example_en`, `example_id`.
- **Frontend**: HTML + JS vanilla, memakai [sql.js](https://github.com/sql-js/sql.js) (SQLite yang dikompilasi ke WebAssembly) untuk menjalankan **query SQL asli langsung di browser**, tanpa perlu server backend.
- Hasilnya tetap situs statis — bisa langsung di-deploy ke **GitHub Pages** tanpa perlu hosting server terpisah.

```
kamus-app-v2/
├── index.html      # UI + query SQL via sql.js
├── kamus.db        # database SQLite (hasil build)
└── db/
    ├── schema.sql   # definisi tabel
    ├── seed.sql     # data awal (10 kata)
    └── build_db.py  # script untuk membangun ulang kamus.db
```

## Menjalankan secara lokal

Karena `index.html` mengambil `kamus.db` lewat `fetch()`, buka lewat local server (bukan langsung dobel klik file), contoh:

```bash
python3 -m http.server 8000
# lalu buka http://localhost:8000
```

## Deploy ke GitHub Pages

1. Push seluruh folder ini ke repo GitHub.
2. `Settings` → `Pages` → pilih branch `main`, folder `/root`.
3. Situs akan aktif di `https://<username>.github.io/<repo>/`.

`kamus.db` akan ter-fetch otomatis oleh browser pengguna, lalu di-query pakai SQL asli melalui sql.js — jadi databasenya "hidup" tanpa perlu server.

## Menambah / mengubah kata

Edit `db/seed.sql` (atau langsung `schema.sql` kalau mau ubah struktur tabel), lalu build ulang:

```bash
cd db
python3 build_db.py
```

Script ini akan membuat ulang `kamus.db` di root folder berdasarkan isi `schema.sql` + `seed.sql`. Tidak butuh instalasi apa pun — cukup Python (modul `sqlite3` sudah bawaan).

Kalau lebih suka pakai CLI SQLite langsung (tanpa Python):

```bash
sqlite3 kamus.db < db/schema.sql
sqlite3 kamus.db < db/seed.sql
```

## Contoh struktur data

| Kolom        | Contoh isi                          |
|--------------|--------------------------------------|
| english      | book                                 |
| indonesian   | buku                                 |
| pos          | noun                                 |
| example_en   | I am reading a good book.            |
| example_id   | Saya sedang membaca buku yang bagus. |

## Teknologi

- SQLite (database)
- sql.js — SQLite via WebAssembly (query SQL di browser)
- HTML5 + CSS3 + JavaScript vanilla (tanpa framework/build tool)
- Python (`sqlite3` bawaan) — hanya dipakai untuk build database, bukan runtime
