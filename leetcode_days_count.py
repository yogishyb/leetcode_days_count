import json
from datetime import datetime

def get_solved_dates(username):
    # Your mock data (normally from API response)
    data = r'''{
    "data": {
        "matchedUser": {
            "userCalendar": {
                "activeYears": [2021, 2024, 2025],
                "streak": 21,
                "totalActiveDays": 65,
                "dccBadges": [],
                "submissionCalendar": "{\"1738022400\": 16, \"1738108800\": 8, \"1738195200\": 3, \"1738454400\": 27, \"1738540800\": 26, \"1738627200\": 3, \"1738713600\": 20, \"1738800000\": 35, \"1738886400\": 24, \"1738972800\": 10, \"1739059200\": 12, \"1739145600\": 3, \"1739232000\": 8, \"1739318400\": 20, \"1739404800\": 17, \"1739491200\": 5, \"1739577600\": 1, \"1739664000\": 1, \"1739750400\": 1, \"1739836800\": 1, \"1739923200\": 1, \"1740009600\": 1, \"1740096000\": 1, \"1740182400\": 1, \"1741305600\": 2, \"1741737600\": 1, \"1746144000\": 6, \"1746403200\": 4, \"1746489600\": 1, \"1746576000\": 1, \"1746662400\": 1, \"1746748800\": 1, \"1747094400\": 1, \"1747526400\": 7, \"1747612800\": 2, \"1747699200\": 5, \"1747785600\": 5, \"1747872000\": 2, \"1747958400\": 19, \"1748044800\": 14, \"1748131200\": 35, \"1748217600\": 3, \"1748304000\": 3, \"1748390400\": 10, \"1748476800\": 4, \"1748563200\": 3, \"1748736000\": 4, \"1748822400\": 3, \"1749600000\": 5, \"1749686400\": 17, \"1749772800\": 4, \"1749859200\": 1, \"1749945600\": 2, \"1750032000\": 1, \"1750118400\": 5, \"1750550400\": 2, \"1750723200\": 2, \"1730937600\": 3, \"1731024000\": 2, \"1731110400\": 4, \"1732233600\": 2, \"1734652800\": 1, \"1734739200\": 1, \"1734825600\": 10, \"1734912000\": 12}"
            }
        }
    }
}'''
    data = json.loads(data)

    calendar_str = data.get("data", {}).get("matchedUser", {}).get("userCalendar", {}).get("submissionCalendar")
    if not calendar_str:
        print("No submissionCalendar found in response")
        return []

    timestamps = json.loads(calendar_str)
    solved_dates = [
        datetime.utcfromtimestamp(int(ts)).strftime("%Y-%m-%d")
        for ts, count in timestamps.items()
        if int(count) > 0
    ]

    return sorted(solved_dates)


if __name__ == "__main__":
    username = "yogishyb"
    solved_dates = get_solved_dates(username)
    print(f"Total days with solved problems: {len(solved_dates)}")
    for date in solved_dates:
        print(date)
