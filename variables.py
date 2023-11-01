with open("/run/secrets/mysecrets.txt") as secrets_file:
    secrets = {}
    for line in secrets_file:
        key, value = line.strip().split("=")
        secrets[key] = value


sender = secrets.get("sender")
receiver = secrets.get("receiver")
password = secrets.get("password")
clan_tag = secrets.get("clan_tag")
token = secrets.get("token")

