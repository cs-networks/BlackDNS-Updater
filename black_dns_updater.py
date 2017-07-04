#!/usr/bin/env python3
"""Updater Script for dynamic DNS service - BlackDNS (private ISP service)

Attributes:
    client (pushover.Client): PushOver client
    payload (dict): Contains credentials for BlackDNS API
"""

import requests
from pushover import Client
import config as cfg

# Setting up Pushover client
client = Client(cfg.pushover_config['user_key'], api_token=cfg.pushover_config['api_token'])

# Setting up parameters for Black DNS API
payload = {'token': cfg.dns_config['token'], 'record': cfg.dns_config['domain']}


def _crop(msg, max_len):
    """Cropping Text to specified length and adding '...' as sign that the string was cropped.

    Args:
        msg (str): Text to be cropped
        max_len (int): Length of new text

    Returns:
        str: Cropped Text
    """
    if max_len is not None and max_len > 0 and len(msg) > max_len:
        return "%s..." % (msg[:max_len - 3])
    else:
        return msg


try:
    r = requests.get('http://' + cfg.dns_config['host'] + cfg.dns_config['path'], params=payload)
    r.raise_for_status()

except requests.exceptions.Timeout as error:
    client.send_message(_crop(error, 512), title="BlackDNS Timeout Error")

except requests.exceptions.HTTPError as error:
    client.send_message(_crop(error, 512), title="BlackDNS HTTP Error")

except requests.exceptions.RequestException as error:
    client.send_message(_crop(error, 512), title="BlackDNS Error")

finally:
    if "OK" not in r.text:
        my_ip = requests.get('https://api.ipify.org').text
        client.send_message(_crop("Current IP: " + str(my_ip) + "\nError: " + r.text, 512), title="BlackDNS Update Error")
