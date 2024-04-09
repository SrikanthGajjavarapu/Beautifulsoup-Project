import requests
from bs4 import BeautifulSoup

url = 'https://www.nseindia.com/market-data/live-equity-market'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)
print(response)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')

# Check if the table is found
if table:
    # Extract table rows
    rows = table.find_all('tr')

    # Loop through rows, starting from the second row (index 1) to skip the header row
    for row in rows[1:]:
        columns = row.find_all('td')
        if len(columns) >= 12:  # Ensure the row has enough columns
            symbol = columns[0].text.strip()
            ltp = columns[1].text.strip()
            chng = columns[2].text.strip()
            percent_chng = columns[3].text.strip()
            open_price = columns[4].text.strip()
            high = columns[5].text.strip()
            low = columns[6].text.strip()
            prev_close = columns[7].text.strip()
            volume_shares = columns[8].text.strip()
            value_lakhs = columns[9].text.strip()
            week_52_high = columns[10].text.strip()
            week_52_low = columns[11].text.strip()

            # Print the extracted data for each stock
            print(f"Symbol: {symbol}")
            print(f"LTP: {ltp}")
            print(f"CHNG: {chng}")
            print(f"%CHNG: {percent_chng}")
            print(f"OPEN: {open_price}")
            print(f"HIGH: {high}")
            print(f"LOW: {low}")
            print(f"PREV. CLOSE: {prev_close}")
            print(f"VOLUME (shares): {volume_shares}")
            print(f"VALUE (₹ Lakhs): {value_lakhs}")
            print(f"52W HIGH: {week_52_high}")
            print(f"52W LOW: {week_52_low}")
            print("\n")

else:
    print("Table not found on the webpage.")
