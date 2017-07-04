# BlackDNS Updater
This is a script to update dynamic DNS entries for a private ISP. In case of an error you are notified by a PushOver notification.

## Configuration file
The credentials and the tokens for DNS - Update API and the PushOver API are configured the [CONFIG][config.py] file.

```python
dns_config = {'host': '',
              'path': '',
              'token': '',
              'domain': ''}

pushover_config = {'user_key': '',
                   'api_token': ''}

```

## Install Crontab
The easiest way to update your DNS continuously is to install a cronjob. You can add th following line to your crontabs and that's it.

    */5 * * * * /path/to/repo/BlackDNS-Updater/black_dns_updater.py >/dev/null 2>&1

## License
This program is distributed under the terms of the GNU GPL v3. See the [LICENSE][license] file for more details.

[license]: https://raw.githubusercontent.com/cs-networks/Sublime-Settings/master/LICENSE
[config.py]: https://raw.githubusercontent.com/cs-networks/BlackDNS-Updater/master/config.py
