import requests
import json
from datetime import datetime

def get_solved_dates(username, year=2025):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/{username}/",
        "User-Agent": "Mozilla/5.0",
    }

    query = """
    query userProfileCalendar($username: String!, $year: Int) {
      matchedUser(username: $username) {
        userCalendar(year: $year) {
          activeYears
          streak
          totalActiveDays
          dccBadges {
            timestamp
            badge {
              name
              icon
            }
          }
          submissionCalendar
        }
      }
    }
    """

    variables = {
        "username": username
    }
    if year is not None:
        variables["year"] = year

    payload = {
        "query": query,
        "variables": variables,
        "operationName": "userProfileCalendar"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print(f"Failed: HTTP {response.status_code}")
        print(response.text)
        return []

    data = response.json()

    # Navigate safely through nested data
    submission_calendar_str = (
        data.get("data", {})
            .get("matchedUser", {})
            .get("userCalendar", {})
            .get("submissionCalendar")
    )
    if not submission_calendar_str:
        print("No submissionCalendar found in response")
        return []

    # submissionCalendar is a JSON string mapping UNIX timestamps to counts
    timestamps = json.loads(submission_calendar_str)

    solved_dates = [
        datetime.utcfromtimestamp(int(ts)).strftime("%Y-%m-%d")
        for ts, count in timestamps.items()
        if int(count) > 0
    ]

    return sorted(solved_dates)


# if __name__ == "__main__":
#     username = "yogishyb"
#     # Optionally specify year: year=2025
#     solved_dates = get_solved_dates(username)
#     print(f"Total days with solved problems: {len(solved_dates)}")
#     for date in solved_dates:
#         print(date)
