#!/usr/bin/env bash

# Quick tsts for  the score API

curl -s https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams | jq '.sports|first.leagues|first.teams[].team|.abbreviation,.id'
curl -s https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/25/schedule | jq '.events[0].shortName'
curl -s https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/25/schedule | jq '.events[0].date'
curl -s https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/25/schedule | jq '.events[0].seasonType.abbreviation'
curl -s https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/25/schedule | jq '.events[0].week.text'
curl -s https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/25/schedule | jq '.events[0].competitions[0].broadcasts[0].media.shortName'
curl -s https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/25/schedule | jq '.events[0].competitions[0].competitors[0].score.value'
curl -s https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/25/schedule | jq '.events[0].competitions[0].competitors[1].score.value'
curl -s https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/25/schedule | jq '.events[0].competitions[0].competitors[1].record[0].displayValue'
curl -s https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/25/schedule | jq '.events[0].competitions[0].competitors[1].record[1].displayValue'
