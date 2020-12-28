## ig_repost_bot
A tool that reposts items from instagram feed & stories feed to specific telegram channel

### Installing
1. `sudo apt install python3-pip`
2. `git clone https://github.com/es3n1n/ig_repost_bot.git`
3. `cd ig_repost_bot`
4. `sudo python3 -m pip install -r requirements.txt`

### Configuring
1. Rename `config.json.example` to `config.json`
2. Open `config.json`
3. Fill the `instagram:login` and `instagram:password` values with your instagram's account login/password
4. Fill the `ig_repost_bot:targets_usernames` with instagram usernames
5. Create a telegram bot [here](https://t.me/botFather) and fill the token variable `telegram:bot_token`
6. Copy your telegram channel's chat id and put it into the variable `telegram:channel_id`

### Running
1. `python3 -m ig_repost_bot`

### Author:
- Telegram - [@battleyedev](https://t.me/battleyedev)
- Github - [@es3n1n](https://github.com/es3n1n)
