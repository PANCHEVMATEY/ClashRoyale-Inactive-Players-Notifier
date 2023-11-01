from datetime import datetime
import requests
from variables import token
from variables import clan_tag
#Make a request to the Clash Royale API
#Check Clash Royale for Developers documentation for more info
r=requests.get(f"https://api.clashroyale.com/v1/clans/{clan_tag}", headers={"Accept":"application/json", "authorization":token}, params = {"limit":20})
data = r.json()
current_date = datetime.now()

#This function whill iretate thorugh the .json data returned by the API
def get_inactive_members_details(clan_data, days_threshold=4):
    #Declare today and an empty list where all inactive players will be appended
    today = datetime.now()
    inactive_players = []
    #Start to iratete trhough the data and declare variables
    for member in clan_data['memberList']:
        status = member['role']
        last_seen_str = member['lastSeen']
        last_seen = datetime.strptime(last_seen_str, "%Y%m%dT%H%M%S.%fZ")
        days_inactive = (today - last_seen).days
        #Filter the users that meet certain criteria and append them to the list
        if status == 'member' and days_inactive > days_threshold:
            inactive_players.append({
                'name': member['name'],
                'tag': member['tag'],
                'days_inactive': days_inactive
            })
    #This message will be returned by the function as plain text in order to be sent by e-mail
    message = "Inactive Players:\n"
    for player in inactive_players:
        message += f"{player['name']} is inactive for {player['days_inactive']} days\n"

    return message

message = get_inactive_members_details(data)
print(message)
