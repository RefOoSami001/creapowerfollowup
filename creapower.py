import requests
import re
import time
import telebot
from keep_alive import keep_alive
# Replace this with your own Telegram Bot Token
TELEGRAM_TOKEN = '6893223743:AAGreuO7BRrhRcaOj8CSUKvZG1AQk-C048E'
# Replace this with your own Telegram Chat ID (You can get it from @userinfobot on Telegram)
CHAT_ID = '854578633'
# Set up the Telegram bot using telebot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Function to send notification
def send_telegram_notification(price):
    bot.send_message(chat_id=CHAT_ID, text=price)

# Define cookies and headers
cookies = {
    'NEXT_LOCALE': 'ar',
    '_ga': 'GA1.1.1208534188.1732809038',
    '_tt_enable_cookie': '1',
    '_ttp': 'I0y3vuvP1raoRMNh1hkjrEJ24f2.tt.1',
    'optiMonkClientId': '449a3301-51ae-58f2-4aea-37be868f03d3',
    'optiMonkSession': '1732809068',
    '__kla_id': 'eyJjaWQiOiJZMkl5TWpFMU5XRXRObVUwTWkwME5tVmxMV0ZpTm1FdE5XVTRPR0ptTlRFME5ETTUiLCIkcmVmZXJyZXIiOnsidHMiOjE3MzI4MDkwNjksInZhbHVlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly96ZXJvZmF0c3VwcGxlbWVudHMuY29tL2FyL3Byb2R1Y3QvJUQ5JTgzJUQ4JUIxJUQ5JThBJUQ4JUE3JUQ4JUFBJUQ5JThBJUQ5JTg2In0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNzMyODA5NDM5LCJ2YWx1ZSI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vemVyb2ZhdHN1cHBsZW1lbnRzLmNvbS9hci9wcm9kdWN0LyVEOSU4MyVEOCVCMSVEOSU4QSVEOCVBNyVEOCVBQSVEOSU4QSVEOSU4NiJ9fQ==',
    'optiMonkClient': 'N4IgTGBsCMMgXKAxgQwcAvgGhAMwG4LQDsAzGABwAMAnFZMTgDaHwnnU0AspNAdF2g0cAOwD2AB1ZgMGIA==',
    '_ga_J786E2TQTY': 'GS1.1.1732809037.1.1.1732809479.0.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

# Function to get the price from the website
def get_price():
    response = requests.get(
        'https://zerofatsupplements.com/ar/product/%D9%83%D8%B1%D9%8A%D8%A7%D8%AA%D9%8A%D9%86/%D9%85%D8%B3%D8%AD%D8%B2%D9%82-%D9%83%D8%B1%D9%8A%D8%A7%D8%AA%D9%8A%D9%86-%D9%83%D8%B1%D9%8A%D8%A7-%D8%A8%D8%A7%D9%88%D8%B1-%D8%B4%D8%B1%D9%83%D8%A9-%D9%83%D8%B1%D9%8A%D8%A7-%D8%A8%D9%8A%D9%88%D8%B1',
        cookies=cookies,
        headers=headers,
    )

    match = re.search(r'\\"lowPrice\\":(\d+),', response.text)

    if match:
        return int(match.group(1))  # Return price as an integer
    else:
        return None

# Main loop to check price every 20 seconds
keep_alive()
while True:
    low_price = get_price()
    if low_price is not None:
        if low_price < 1090:
            message = f"Alert:⚠️👋\nThe price is now {low_price} EGP, which is below the threshold!"
            send_telegram_notification(message)
    else:
        message = ('Error\nLow Price not found!')
        send_telegram_notification(low_price)

    # Wait for 20 seconds before checking again
    time.sleep(15)