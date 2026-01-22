from flask import Flask, jsonify, render_template
from app.database import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("search.html")


@app.route("/cards")
def get_cards():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT name_en, card_number, card_index, version
        FROM cards
        ORDER BY version, card_index
    """)

    rows = cur.fetchall()
    conn.close()

    return jsonify([
        {
            "name": r["name_en"],
            "card_number": r["card_number"],
            "card_index": r["card_index"],
            "version": r["version"]
        }
        for r in rows
    ])


if __name__ == "__main__":
    app.run(debug=True)
