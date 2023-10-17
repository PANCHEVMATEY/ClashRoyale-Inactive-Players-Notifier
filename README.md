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

## How to Use

1. Clone this repository to your local machine.

```shell
https://github.com/PANCHEVMATEY/ClashRoyale-Inactive-Players-Notifier.git```

2. Open the `main.py` script.

3. Update the following variables with your own values:

   - `sender`: Your Gmail email address.
   - `password`: Your application-specific password.
   - `receiver`: The email address to receive notifications.
   - `clan_tag`: Your Clash Royale clan's tag.
   - `token`: Your Clash Royale API token.

4. Run the script using Python:

```shell
python main.py
```

The script will start monitoring the activity of your clan members. When it detects an inactive member, it will send an email notification to the specified receiver.

## Acknowledgments

- Thanks to the Clash Royale API for providing access to clan member data.
- Code With Tomi for helping with the email part

Feel free to reach out if you have any questions or need further assistance with setting up the Clash Royale Clan Inactivity Notifier.

Happy gaming!
```