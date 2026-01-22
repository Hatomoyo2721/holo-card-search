from app.database import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_en TEXT,
        original_title TEXT,
        card_game TEXT,
        version TEXT,
        original_version TEXT,
        card_number TEXT UNIQUE,
        card_index INTEGER,
        rarity TEXT,
        spec TEXT,
        oshi TEXT
    );
    """)

    conn.commit()
    conn.close()


# =========================================================
# Example card record (for reference only)
#
# id              -> auto-incremented by SQLite
#
# name_en         = "Koseki Bijou"
# original_title  = "古石ビジュー"
#
# card_game       = "hololive OFFICIAL CARD GAME"
#
# version         = "[hBP04] Curious Universe"
# original_version= "[hBP04]キュリアスユニバース"
#
# card_number     = "hBP04-066"
# card_index      = 66
#
# rarity          = "UR"
# spec            = "Foil (UR Parallel)"
#
# oshi            = "Koseki Bijou"
# =========================================================
