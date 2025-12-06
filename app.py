from flask import Flask, request, jsonify, render_template
import csv
import random
import chardet

app = Flask(__name__)

DATA_FILE = "data/questions.csv"

def load_questions():
    questions = []
    with open(DATA_FILE, newline='', encoding='utf-8') as f:
        sample = f.read(1024)
        f.seek(0)

        # 区切り文字を自動判定
        delimiter = '\t' if '\t' in sample else ','

        reader = csv.reader(f, delimiter=delimiter)

        for row in reader:
            if len(row) >= 6:
                questions.append({
                    "id": row[0],
                    "subject": row[1],
                    "round": int(row[2]),
                    "unit": row[3],
                    "question": row[4],
                    "answer": row[5],
                })

    return questions



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/questions")
def api_questions():
    subject = request.args.get("subject")
    start_r = int(request.args.get("start"))
    end_r = int(request.args.get("end"))
    mode = request.args.get("mode")

    data = load_questions()
    filtered = [q for q in data if q["subject"] == subject and start_r <= q["round"] <= end_r]

    if mode == "random":
        random.shuffle(filtered)

    return jsonify(filtered)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
