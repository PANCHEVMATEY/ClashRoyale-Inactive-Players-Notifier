from datetime import datetime
import requests as requests
from variables import token
from variables import clan_tag

r=requests.get(f"https://api.clashroyale.com/v1/clans/{clan_tag}", headers={"Accept":"application/json", "authorization":token}, params = {"limit":20})
data = r.json()
current_date = datetime.now()


def get_inactive_members_details(clan_data, days_threshold=4):
    today = datetime.now()
    inactive_players = []

    for member in clan_data['memberList']:
        status = member['role']
        last_seen_str = member['lastSeen']
        last_seen = datetime.strptime(last_seen_str, "%Y%m%dT%H%M%S.%fZ")
        days_inactive = (today - last_seen).days

        if status == 'member' and days_inactive > days_threshold:
            inactive_players.append({
                'name': member['name'],
                'tag': member['tag'],
                'days_inactive': days_inactive
            })

    message = "Inactive Players:\n"
    for player in inactive_players:
        message += f"{player['name']} is inactive for {player['days_inactive']} days\n"

    return message

message = get_inactive_members_details(data)
print(message)

