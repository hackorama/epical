from typing import Tuple

import config
import pytz
import requests
from dateutil.parser import parse


class ScoreData:
    # ESPN NFL API endpoint
    SCORE_API_URL = " https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/{team}/schedule"
    # Team name abbreviation id map used by ESPN NFL API
    SCORE_TEAMS = {
        "ARI": "22",
        "ATL": "1",
        "BAL": "33",
        "BUF": "2",
        "CAR": "29",
        "CHI": "3",
        "CIN": "4",
        "CLE": "5",
        "DAL": "6",
        "DEN": "7",
        "DET": "8",
        "GB": "9",
        "HOU": "34",
        "IND": "11",
        "JAX": "30",
        "KC": "12",
        "LV": "13",
        "LAC": "24",
        "LAR": "14",
        "MIA": "15",
        "MIN": "16",
        "NE": "17",
        "NO": "18",
        "NYG": "19",
        "NYJ": "20",
        "PHI": "21",
        "PIT": "23",
        "SF": "25",
        "SEA": "26",
        "TB": "27",
        "TEN": "10",
        "WSH": "28",
    }

    @staticmethod
    def get_score_logo() -> Tuple[str, int, int]:
        return "resources/team.png", 150, 150

    @staticmethod
    def get_scores(team=config.SCORE_TEAM_ID):  # pylint: disable=too-many-locals
        team_id = int(ScoreData.SCORE_TEAMS.get(team))
        result = []
        if not team_id:
            print("ERROR: Could not find team for {team}")
            return result
        r = requests.get(
            ScoreData.SCORE_API_URL.format(team=team), timeout=config.API_TIMEOUT_SECS
        )
        for event in r.json().get("events", []):
            team_a = event["competitions"][0]["competitors"][0]["team"]["id"]
            team_a_abbr = event["competitions"][0]["competitors"][0]["team"][
                "abbreviation"
            ]
            team_b_abbr = event["competitions"][0]["competitors"][1]["team"][
                "abbreviation"
            ]
            won = ""
            if (
                "winner" in event["competitions"][0]["competitors"][0]
                or "winner" in event["competitions"][0]["competitors"][1]
            ):
                team_a_won = event["competitions"][0]["competitors"][0]["winner"]
                team_b_won = event["competitions"][0]["competitors"][1]["winner"]
                won = team_a_won if int(team_a) == team_id else team_b_won
            team_a_home_away = event["competitions"][0]["competitors"][0]["homeAway"]
            team_b_home_away = event["competitions"][0]["competitors"][1]["homeAway"]
            score_a = None
            score_b = None
            if "score" in event["competitions"][0]["competitors"][0]:
                score_a = event["competitions"][0]["competitors"][0]["score"][
                    "displayValue"
                ]
                score_b = event["competitions"][0]["competitors"][1]["score"][
                    "displayValue"
                ]
            game_time = ""
            if "date" in event["competitions"][0]:
                game_date = event["competitions"][0]["date"]
                game_date = parse(game_date)
                game_date = game_date.astimezone(pytz.timezone("America/Los_Angeles"))
                game_time = game_date.strftime("%a %d %b %I:%M %p").upper()

            home_away = team_a_home_away if int(team_a) == team_id else team_b_home_away
            sf_score, other_score = (
                (score_a, score_b) if int(team_a) == team_id else (score_b, score_a)
            )
            other_team_name = team_b_abbr if int(team_a) == team_id else team_a_abbr

            score = ""
            if home_away == "away":
                name = f"@ {other_team_name}"
                if score_a is not None and score_b is not None:
                    score = f"{sf_score} - {other_score}"
            else:
                name = f"{other_team_name}"
                if score_a is not None and score_b is not None:
                    score = f"{other_score} - {sf_score}"

            game = {"name": name, "score": score, "won": won, "game_time": game_time}
            result.append(game)
        return result
