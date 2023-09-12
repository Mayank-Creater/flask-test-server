from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
}

url = 'https://www.nseindia.com/option-chain'
url_main = 'https://www.nseindia.com/'
url_bnf = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'
url_nf = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
url_gift = 'https://sgxnifty.org'

def getcookie():
    sess = requests.Session()
    res = sess.get(url, headers=headers)
    cookies = dict(res.cookies)

    return cookies

@app.route('/')
def welcome():
    return 'Welcome to the Home Page.'

@app.route('/api')
def data():
    cookies = getcookie()
    bnf_res = requests.get(url_bnf, headers=headers, cookies=cookies)
    bnf_data = bnf_res.json()['filtered']

    bnf_ce_totOI = bnf_data['CE']['totOI']
    bnf_pe_totOI = bnf_data['PE']['totOI']
    bnf_ce_coi = []
    bnf_pe_coi = []
    bnf_ce_vol = []
    bnf_pe_vol = []
    bnf_strike = []

    for i in bnf_data['data']:
        bnf_strike.append(i['strikePrice'])
        if 'CE' in i:
            bnf_ce_coi.append(i['CE']['changeinOpenInterest'])
            bnf_ce_vol.append(i['CE']['totalTradedVolume'])
        if 'PE' in i:
            bnf_pe_coi.append(i['PE']['changeinOpenInterest'])
            bnf_pe_vol.append(i['PE']['totalTradedVolume'])

    bnf_ce_coi = sum(bnf_ce_coi)
    bnf_pe_coi = sum(bnf_pe_coi)

    bnf_sorted_ce_vol = sorted(bnf_ce_vol)
    bnf_sorted_pe_vol = sorted(bnf_pe_vol)

    bnf_max_ce_vol = bnf_sorted_ce_vol[-1]
    bnf_max_ce_vol2 = bnf_sorted_ce_vol[-2]
    bnf_max_ce_vol3 = bnf_sorted_ce_vol[-3]

    bnf_max_pe_vol = bnf_sorted_pe_vol[-1]
    bnf_max_pe_vol2 = bnf_sorted_pe_vol[-2]
    bnf_max_pe_vol3 = bnf_sorted_pe_vol[-3]

    bnf_max_ce_vol_index = bnf_ce_vol.index(bnf_max_ce_vol)
    bnf_max_ce_vol2_index = bnf_ce_vol.index(bnf_max_ce_vol2)
    bnf_max_ce_vol3_index = bnf_ce_vol.index(bnf_max_ce_vol3)

    bnf_max_ce_vol_strike_price = bnf_strike[bnf_max_ce_vol_index]
    bnf_max_ce_vol2_strike_price = bnf_strike[bnf_max_ce_vol2_index]
    bnf_max_ce_vol3_strike_price = bnf_strike[bnf_max_ce_vol3_index]

    bnf_max_pe_vol_index = bnf_pe_vol.index(bnf_max_pe_vol)
    bnf_max_pe_vol2_index = bnf_pe_vol.index(bnf_max_pe_vol2)
    bnf_max_pe_vol3_index = bnf_pe_vol.index(bnf_max_pe_vol3)

    bnf_max_pe_vol_strike_price = bnf_strike[bnf_max_pe_vol_index]
    bnf_max_pe_vol2_strike_price = bnf_strike[bnf_max_pe_vol2_index]
    bnf_max_pe_vol3_strike_price = bnf_strike[bnf_max_pe_vol3_index]



    nf_res = requests.get(url_nf, headers=headers, cookies=cookies)
    nf_data = nf_res.json()['filtered']

    nf_ce_totOI = nf_data['CE']['totOI']
    nf_pe_totOI = nf_data['PE']['totOI']
    nf_ce_coi = []
    nf_pe_coi = []
    nf_ce_vol = []
    nf_pe_vol = []
    nf_strike = []

    for j in nf_data['data']:
        nf_strike.append(j['strikePrice'])
        if 'CE' in j:
            nf_ce_coi.append(j['CE']['changeinOpenInterest'])
            nf_ce_vol.append(j['CE']['totalTradedVolume'])
        if 'PE' in j:
            nf_pe_coi.append(j['PE']['changeinOpenInterest'])
            nf_pe_vol.append(j['PE']['totalTradedVolume'])

    nf_ce_coi = sum(nf_ce_coi)
    nf_pe_coi = sum(nf_pe_coi)

    nf_sorted_ce_vol = sorted(nf_ce_vol)
    nf_sorted_pe_vol = sorted(nf_pe_vol)

    nf_max_ce_vol = nf_sorted_ce_vol[-1]
    nf_max_ce_vol2 = nf_sorted_ce_vol[-2]
    nf_max_ce_vol3 = nf_sorted_ce_vol[-3]

    nf_max_pe_vol = nf_sorted_pe_vol[-1]
    nf_max_pe_vol2 = nf_sorted_pe_vol[-2]
    nf_max_pe_vol3 = nf_sorted_pe_vol[-3]

    nf_max_ce_vol_index = nf_ce_vol.index(nf_max_ce_vol)
    nf_max_ce_vol2_index = nf_ce_vol.index(nf_max_ce_vol2)
    nf_max_ce_vol3_index = nf_ce_vol.index(nf_max_ce_vol3)

    nf_max_ce_vol_strike_price = nf_strike[nf_max_ce_vol_index]
    nf_max_ce_vol2_strike_price = nf_strike[nf_max_ce_vol2_index]
    nf_max_ce_vol3_strike_price = nf_strike[nf_max_ce_vol3_index]

    nf_max_pe_vol_index = nf_pe_vol.index(nf_max_pe_vol)
    nf_max_pe_vol2_index = nf_pe_vol.index(nf_max_pe_vol2)
    nf_max_pe_vol3_index = nf_pe_vol.index(nf_max_pe_vol3)

    nf_max_pe_vol_strike_price = nf_strike[nf_max_pe_vol_index]
    nf_max_pe_vol2_strike_price = nf_strike[nf_max_pe_vol2_index]
    nf_max_pe_vol3_strike_price = nf_strike[nf_max_pe_vol3_index]

    gift_res = requests.get(url_gift)
    soup = BeautifulSoup(gift_res.text, 'html.parser')
    gift_change = soup.find_all('td', {'class': 'main-change'})[1].text
    gift_change_value = gift_change.strip()

    main_res = requests.get(url=url_main, headers=headers, cookies=cookies)
    main_soup = BeautifulSoup(main_res.text, 'html.parser')
    nf_price = main_soup.find_all('p', {'class': 'tb_val'})[0].text
    nf_change = main_soup.find_all('p', {'class': 'tb_per'})[0].text
    bnf_price = main_soup.find_all('p', {'class': 'tb_val'})[3].text
    bnf_change = main_soup.find_all('p', {'class': 'tb_per'})[3].text

    bnf_change = bnf_change.strip().replace('\r\n', '')
    bnf_price = bnf_price.strip().replace('\n', '')
    nf_change = nf_change.strip().replace('\r\n', '')
    nf_price = nf_price.strip().replace('\n', '')

    result = {
        "BNF":{
            "ce_totOI": bnf_ce_totOI,
            "ce_coi": bnf_ce_coi,
            "ce_max_vols": [
                [bnf_max_ce_vol, bnf_max_ce_vol_strike_price],
                [bnf_max_ce_vol2, bnf_max_ce_vol2_strike_price],
                [bnf_max_ce_vol3, bnf_max_ce_vol3_strike_price]
            ],
            "ce_vol":bnf_ce_vol,
            "pe_totOI": bnf_pe_totOI,
            "pe_coi": bnf_pe_coi,
            "pe_max_vols": [
                [bnf_max_pe_vol, bnf_max_pe_vol_strike_price],
                [bnf_max_pe_vol2, bnf_max_pe_vol2_strike_price],
                [bnf_max_pe_vol3, bnf_max_pe_vol3_strike_price]
            ],
            "pe_vol":bnf_pe_vol,
            "strike_price":bnf_strike,
            "price": bnf_price,
            "change": bnf_change
        },
        "NF":{
            "ce_totOI": nf_ce_totOI,
            "ce_coi": nf_ce_coi,
            "ce_max_vols": [
                [nf_max_ce_vol, nf_max_ce_vol_strike_price],
                [nf_max_ce_vol2, nf_max_ce_vol2_strike_price],
                [nf_max_ce_vol3, nf_max_ce_vol3_strike_price]
            ],
            "ce_vol": nf_ce_vol,
            "pe_totOI": nf_pe_totOI,
            "pe_coi": nf_pe_coi,
            "pe_max_vols": [
                [nf_max_pe_vol, nf_max_pe_vol_strike_price],
                [nf_max_pe_vol2, nf_max_pe_vol2_strike_price],
                [nf_max_pe_vol3, nf_max_pe_vol3_strike_price]
            ],
            "pe_vol": nf_pe_vol,
            "strike_price": nf_strike,
            "price": nf_price,
            "change": nf_change
        },
        "GIFT NIFTY": gift_change_value,
    }

    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

if __name__ == '__main__':
    app.run(debug=True)
