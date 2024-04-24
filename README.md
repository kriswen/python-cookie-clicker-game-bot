# Python Cookie Clicker Game Bot

This Python script automates the playing of the [Cookie Clicker](https://orteil.dashnet.org/experiments/cookie/) game using Selenium WebDriver.

## Installation

1. Install Python if you haven't already. You can download it from [here](https://www.python.org/downloads/).
2. Install the required dependencies using pip:

    ```
    pip install selenium
    ```

3. Download the appropriate WebDriver for your browser:
   - [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

4. Make sure you have the Chrome browser installed on your system.

## Usage

1. Clone or download this repository to your local machine.
2. Place the WebDriver executable in the same directory as the Python script.
3. Run the Python script:

    ```
    python cookie_clicker_bot.py
    ```

4. The bot will automatically open the Cookie Clicker game in a new Chrome browser window and start playing.

## Features

- Automatically clicks the cookie to generate cookies.
- Purchases the most expensive available upgrade every 5 seconds, if affordable.
- Runs for 5 minutes and then displays the number of cookies generated per second.

## Notes

- The bot uses Selenium WebDriver to automate interactions with the browser.
- Make sure to keep the browser window open and not minimize it while the bot is running.
