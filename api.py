from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/scrape')
def scrape():
    url = 'http://agricoop.gov.in/en/Major#gsc.tab=0'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    results = soup.find("tbody")
    
    # Create a list of dictionaries to store the scraped data
    data = []
    for row in results.find_all("tr"):
        cols = row.find_all("td")
        data.append({
            "SR. NO": cols[0].get_text(),
            "TITLE": cols[1].get_text(),
            "PUBLISH DATE": cols[2].get_text(),
            "DETAILS ": cols[3].get_text()
        })
    
    # Return the scraped data as JSON
    return jsonify(data)
#since i had to make a change
if __name__ == '__main__':
    app.run(debug=True)