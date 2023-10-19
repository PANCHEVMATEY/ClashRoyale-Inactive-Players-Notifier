```markdown
# Clash Royale Clan Inactivity Notifier

You are a leader of clan in Clash Royale and you have to kick many inactive players?
Say no more this script will email you with all players with status "Member" that haven't been active in the past 4 days
Clash Royale Clan Inactivity Notifier is a Python script that monitors the activity of clan members and sends email notifications when members go inactive. This tool helps clan leaders and members keep their clan active and engaged by tracking inactivity.

## Prerequisites

Before you can use this script, you'll need to set up a few variables in the script to customize it for your specific clan and email configuration. Here's what you need:

- `sender`: Your Gmail email address from which email notifications will be sent.
- `password`: Your Gmail account's application-specific password. [Learn more](https://support.google.com/accounts/answer/185833?hl=en)
- `receiver`: The email address where you want to receive the inactivity notifications.
- `clan_tag`: Your Clash Royale clan's tag, which you want to monitor for inactivity.
- `token`: Your Clash Royale API token, which is required to access clan member data.

## Running as a Docker Container

You can run the Clash Royale Clan Inactivity Notifier as a Docker container to automate the process. This container will execute the script every Monday at 9 AM. To set up and run the Docker container, follow these steps:

1. Make sure you have Docker installed on your system.

2. Clone this repository to your local machine:

```shell
git clone https://github.com/PANCHEVMATEY/ClashRoyale-Inactive-Players-Notifier.git
```

3. Open the `variables.py` script and update the following variables with your own values:

   - `sender`: Your Gmail email address.
   - `password`: Your application-specific password.
   - `receiver`: The email address to receive notifications.
   - `clan_tag`: Your Clash Royale clan's tag.
   - `token`: Your Clash Royale API token.

4. Build the Docker image:

```shell
docker build -t clash-royale-inactivity-notifier .
```

5. Run the Docker container, scheduling it to execute every Monday at 9 AM:

```shell
docker run -d --name inactivity-notifier 
```
6. You can customize the crontab content for whatever use case you have

The script will now monitor the activity of your clan members and, when it detects an inactive member, it will send an email notification to the specified receiver every Monday at 9 AM.

## Acknowledgments

- Thanks to the Clash Royale API for providing access to clan member data.
- Code With Tomi for providing assistance with the email component.

Feel free to reach out if you have any questions or need further assistance with setting up the Clash Royale Clan Inactivity Notifier.

Happy gaming!
```

This updated README provides instructions on running the script as a Docker container and specifies the scheduling to execute it every Monday at 9 AM.