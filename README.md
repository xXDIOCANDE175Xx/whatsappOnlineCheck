# Whatsapp online status detection
![Alt Text](https://meteoclari.it/wp-content/uploads/2020/11/WhatsApp-icon-PNG.png)
![Alt Text](https://icons.iconarchive.com/icons/cornmanthe3rd/plex/256/Other-python-icon.png)


This script allows, through the use of a browser and Whatsapp Web, to record when a user is online.

## Attention :warning:

This script uses Whatsapp Web, an official web application released by Whatsapp Inc.
This application often changes the code of the web pages and therefore it will be necessary to adapt the code accordingly. This version is tested until 7 May 2021.

## Installation

Use the package manager [pip](https://pypi.org/project/pip/) to install requirements. 

```bash
git clone https://github.com/xXDIOCANDE175Xx/whatsappOnlineCheck
cd whatsappOnlineCheck
pip3 install -r requirements.txt
```
Download the Chrome driver from this [link](https://chromedriver.chromium.org/downloads) and copy the file to a folder of your choice.

## Usage

Use the [ChroPath](https://chrome.google.com/webstore/detail/chropath/ljngjbnaijcbncmcnjfhigebomdlkcjo) Chrome extension to find these values ​​on the whatsapp page in case the page source code has changed. Use the absolute path.
```python
NEW_CHAT_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]'
INPUT_TXT_BOX = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/label[1]/div[1]/div[2]'
ONLINE_STATUS_LABEL = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[2]/span[1]"
```
Replace with the path to the driver file you downloaded earlier.
```python
browser = webdriver.Chrome(r'/path/to/file')
```
Replace this with name and phone number of contact target. Separate multi-target with comma.
```python
TARGETS = {'"name"': 'number_international_format'}
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
## License
MIT License

Copyright (c) 2021 xXDIOCANDE175Xx
