-- Skema database Kamus EN-ID
-- Satu tabel menyimpan semua kata, bisa dicari dua arah (EN->ID dan ID->EN)

DROP TABLE IF EXISTS words;

CREATE TABLE words (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  english     TEXT NOT NULL,
  indonesian  TEXT NOT NULL,
  pos         TEXT NOT NULL,     -- part of speech: noun, verb, adjective, adverb, dll
  example_en  TEXT NOT NULL,     -- contoh kalimat bahasa Inggris
  example_id  TEXT NOT NULL      -- contoh kalimat bahasa Indonesia
);

-- Index untuk mempercepat pencarian dua arah
CREATE INDEX idx_words_english    ON words (english);
CREATE INDEX idx_words_indonesian ON words (indonesian);
