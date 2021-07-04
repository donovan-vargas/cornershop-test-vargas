""""
slack utils
To send messages
"""

from django.conf import settings
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def send_message_slack(message, channel=None):
    """
    send_message_slack, send messages
    :param message: message to channel
    :param channel: channel will send message
    :return:
    """
    slack_token = getattr(settings, "SLACK_OAUTH_ACCESS_TOKEN")
    if not channel:
        channel = getattr(settings, "SLACK_CHANNEL")
    client = WebClient(token=slack_token)
    try:
        print(client.chat_postMessage(channel=channel, text=message))
        return True
    except SlackApiError as slack_error:
        assert slack_error.response["error"]
        return False
