from flask import Flask, request, jsonify
from script import get_solved_dates

app = Flask(__name__)

@app.route("/solved_dates", methods=["GET"])
def solved_dates():
    username = request.args.get("username", "yogishyb")
    year = request.args.get("year", None)
    if year:
        year = int(year)
    dates = get_solved_dates(username, year)
    return jsonify({
        "total": len(dates),
        "dates": dates
    })

if __name__ == "__main__":
    app.run()
