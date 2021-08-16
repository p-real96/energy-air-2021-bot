import requests
import json
import time
import random

def get_answer(question):
    switcher = {
        "WIE HEISST DER OFFIZIELLE INSTAGRAM-ACCOUNT DES ENERGY AIR?": "@energyair_official",
        "MUSIKGRÖSSEN AUS WIE VIELEN LÄNDERN WAREN AM ENERGY AIR 2019 DABEI?": "Aus 7 Ländern",
        "IN WELCHER LOCATION FINDET DAS ENERGY AIR 2021 UNTER FREIEM HIMMEL STATT?": "Nationalstadion der Schweiz Wankdorf Bern",
        "IN WELCHEM SCHWEIZER KANTON ERÖFFNETE TALLY WEIJL 1987 DEN ERSTEN STORE?": "Fribourg",
        "WAS FOLGT AM DIESJÄHRIGEN ENERGY AIR ALS KRÖNENDER ABSCHLUSS?": "Aftershowparty",
        "IN WIE VIELEN LÄNDERN IST DAS KLEIDERGESCHÄFT TALLY WEIJL VERTRETEN?": "In 39 Ländern",
        "WELCHE MUSIKERIN WURDE AM ENERGY AIR 2018 VON EINER 9-JÄHRIGE BESUCHERIN AUF DER BÜHNE GECOVERT?": "Namika",
        "WIE KANNST DU DEINE GEWINNCHANCEN BEI TICKETVERLOSUNGEN FÜR ENERGY EVENTS VERDOPPELN?": "Mit einer Energy One Membership",
        "WAS WAR DAS ERSTE, WAS KÜNSTLER KNACKEBOUL NACH SEINEM AUFTRITT 2014 BACKSTAGE GEMACHT HAT?": "Mit seinem Mami ein kühles Bier getrunken",
        "WELCHE STADT GEHÖRT SEIT AUGUST AUCH ZUR ENERGY FAMILIE UND WIRD AM ENERGY AIR VERTRETEN SEIN?": "Luzern",
        "IN WELCHEN FARBEN TRITT DAS ENERGY AIR LOGO JÄHRLICH FÜR DAS SOMMERFINALE AUF?": "Blau und Weiss",
        "NACH WELCHEM KRITERIUM WÄHLT DAS ENERGY TEAM DIE ACTS FÜR DAS ENERGY AIR AUS?": "Musiker*innen, welche einen grossen Bekanntheitsgrad haben",
        "UNTER WELCHEM MOTTO FEIERN WIR AM 4. SEPTEMBER 2021 DAS ENERGY AIR?": "We are back.",
        "MIT WELCHEM ESC-HIT ROCKTE LUCA HÄNNI AM LETZTEN ENERGY AIR DIE BÜHNE?": "She Got Me",
        "WELCHER KÜNSTLER MUSSTE AM LETZTEN ENERGY AIR BACKSTAGE EINEN PART AUS DEM DIALEKTRAPSONG VON SANDRO VORRAPPEN?": "Stress",
        "MIT WELCHEM AUFBLASBAREN TIER KONNTEN ZWEI AUSERWÄHLTE AM LETZTEN ENERGY AIR ÜBER DIE GANZE MEUTE CROWDSURFEN?": "Schwan",
        "VON WELCHER MARKE WAR DAS MOTORRAD, MIT DEM LOCO ESCRITO AM LETZTEN ENERGY AIR ÜBER DIE BÜHNE FUHR?": "Harley-Davidson",
        "WELCHER ACT FEIERTE AM LETZTEN ENERGY AIR MIT EINEM NEUEN SONG EINE WELTPREMIERE?": "Aloe Blacc",
        "MIT WELCHER ZUSATZOPTION HAST DU DIE MÖGLICHKEIT, DIREKT VOR DER BÜHNE ZU STEHEN?": "XTRA Circle",
        "WELCHE ZWEI ENERGY KULTFIGUREN MISCHTEN DAS ENERGY AIR 2017 RICHTIG AUF?": "Tinu & Dänu",
        "WELCHEN KLEIDUNGSSTIL VERFOLGT TALLY WEIJL GRUNDSÄTZLICH?": "Just in time (voll im Trend)",
        "WANN IST DIE TICKETVERLOSUNG FÜRS ENERGY AIR 2021 GESTARTET?": "Am 2. August 2021",
        "WAS PASSIERT, WENN ES AM ENERGY AIR REGNET?": "Der Event findet trotzdem statt",
        "WAS IST DAS PERFEKTE OPENAIR-OUTFIT?": "Egal, hauptsache du kannst darin tanzen",
        "WIE ALT MUSS MAN SEIN, UM OHNE ERWACHSENE BEGLEITUNG AM ENERGY AIR TEILZUNEHMEN?": "14 Jahre",
        "WOMIT ERSCHIENEN DIE ENERGY MEIN MORGEN MODERATOREN MOSER UND SCHELKER AUF DER ENERGY AIR BÜHNE 2019?": "Mit Spielzeug-Pferden",
        "WIE WIRD TALLY WEIJL AUSGESPROCHEN?": "Talli Weil",
        "WIE LANGE DAUERTE DAS ENERGY AIR 2019?": "5 1/2 Stunden",
        "WER WAR DER ALLERERSTE ACT IN DER GESCHICHTE DES ENERGY AIR?": "Bastian Baker",
        "WELCHES SCHWEIZER DJ-DUO SORGTE AM ENERGY AIR 2019 ZU BEGINN FÜR REICHLICH STIMMUNG?": "Averdeck",
        "WO KANNST DU, UNTER ANDEREM, ENERGY AIR TICKETS GEWINNEN?": "Am Sender bei Radio Energy",
        "WELCHER ACT WAR NOCH NIE AN EINEM ENERGY AIR DABEI?": "Michael Patrick Kelly",
        "WER WAR DER ÜBERRASCHUNGSACT AM ENERGY AIR 2018?": "Lo & Leduc",
        "IN WELCHER BELIEBTEN SERIE WAR TALLY WEIJL ZU SEHEN?": "Gossip Girl",
        "WIE HEISST DIE INITIATIVE FÜR MEHR RESPEKT IM INTERNET, WELCHE SWISSCOM MIT ENERGY LANCIERT HAT UND AM ENERGY AIR IHREN GROSSEN HÖHEPUNKT FEIERT?": "Mute the hate",
        "WIE HEISST DIE TRAM- UND BUSHALTESTELLE, WELCHE SICH DIREKT NEBEN DEM STADION WANKDORF BEFINDET?": "Wankdorf Center",
    }
    return switcher.get(question.upper(), "Invalid question")


while True:

    url = "https://game.energy.ch/api/questions"
    payload={}
    headers = {
    'Host': 'game.energy.ch',
    'Connection': 'close',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://game.energy.ch/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'XSRF-TOKEN=OqoaJFBweWilnYdaAETDC0NOTUVeIZ8Pws4RadC8; energy_game_session=8IbZrPceEemKfCNJ1ZQGA81pZ0AYesd2VXtTanT1; _ga=GA1.2.990381397.1629101106; _gid=GA1.2.1552452295.1629101106; _gat=1; access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlM2UVRPR1h5RmYzWjV0RnlBQUdRbTdzZ1FDejlnMzl5Zm5OOXp4YlRkclEifQ.eyJqdGkiOiJCNndFN0xYWUs4QjhCTFlXQnp5MmsiLCJzdWIiOiJhdXRoMHxmNWE4MzE5Nzk5Y2E5Yjg4NGQ3Y2JjYjZiN2U3NDgyMTMxZWM1YjBhM2UwMDhmZjRmMTY2M2VhN2YxYWU5MWU5IiwiaWF0IjoxNjI5MTAxNDAzLCJleHAiOjE2MjkxODc4MDMsInNjb3BlIjoib3BlbmlkIGVtYWlsIiwiaXNzIjoiaHR0cHM6Ly9sb2dpbi5jb25uZWN0LnJpbmdpZXIuY2gvIiwiYXVkIjoiSldUOUdCak1jYUo3ZG44RkN6WjdTVkVTcGdZajk4bnEiLCJodHRwczovL2Nvbm5lY3QucmluZ2llci5jaC91cm46cmluZ2llcjpicmFuZC1uYW1lIjoiZW5lcmd5IiwidXJuOm9uZWxvZzpicmFuZC1uYW1lIjoiZW5lcmd5IiwiYXV0aF90aW1lIjoxNjI5MTAxNDAzfQ.QjsDwoRHLq2pGJ1ngmpkBAFn-gwH-6nCIqCAom-XXRRTlurlkYISqZDLknGpEoP1EJ3L42PHUhPjgRGfB-66hCB9tcbFrfx6d6Vr5uW378YeBHP-BC_6c3NjEspnaqomgCpM-WfLK6ETIEfr3S-MWbQ_g__YU8uXBAmOFHMC0bSgewgN0RTLvP53BAOLoLbsvv-kAAB2bGMGtXyXzvof-I-kiBPdtfOeO4bvXYY2kwJM6_pHDVvhpcP8Iq-CnwqYlwS29NezaqsABd4n7R8mH7vZT1IVc6H0gfRscVwpqXUnLyksdfMJkjaXM8anNu8Bfuvef2p10Xq4lLDDaXfEsQ; energy_game_session=8IbZrPceEemKfCNJ1ZQGA81pZ0AYesd2VXtTanT1'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = json.loads(response.text)

    print(response_json)
    answer_ids = []

    for question in response_json:
        
        print("question: {} | answer: {}".format(question['text'], get_answer(question['text'])))

        answer_text = get_answer(question['text'])
        index = 0

        for answer in question['answers']:
            
            if answer['text'] == answer_text:
                #print("found id: {}".format(index))
                answer_ids.append(index)
            index += 1

    data = {}
    data['answers'] = answer_ids
    json_data = json.dumps(data)
    print(json_data)

    time.sleep(random.randint(5, 10))

    url = "https://game.energy.ch/api/questions/check"

    #payload="{\"answers\":[0,0,1,0,2,0,2,1,1,1]}"
    payload = json_data
    headers = {
    'Host': 'game.energy.ch',
    'Connection': 'close',
    'Content-Length': '33',
    'Accept': 'application/json, text/plain, */*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://game.energy.ch',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://game.energy.ch/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'XSRF-TOKEN=OqoaJFBweWilnYdaAETDC0NOTUVeIZ8Pws4RadC8; energy_game_session=8IbZrPceEemKfCNJ1ZQGA81pZ0AYesd2VXtTanT1; _ga=GA1.2.990381397.1629101106; _gid=GA1.2.1552452295.1629101106; access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlM2UVRPR1h5RmYzWjV0RnlBQUdRbTdzZ1FDejlnMzl5Zm5OOXp4YlRkclEifQ.eyJqdGkiOiJCNndFN0xYWUs4QjhCTFlXQnp5MmsiLCJzdWIiOiJhdXRoMHxmNWE4MzE5Nzk5Y2E5Yjg4NGQ3Y2JjYjZiN2U3NDgyMTMxZWM1YjBhM2UwMDhmZjRmMTY2M2VhN2YxYWU5MWU5IiwiaWF0IjoxNjI5MTAxNDAzLCJleHAiOjE2MjkxODc4MDMsInNjb3BlIjoib3BlbmlkIGVtYWlsIiwiaXNzIjoiaHR0cHM6Ly9sb2dpbi5jb25uZWN0LnJpbmdpZXIuY2gvIiwiYXVkIjoiSldUOUdCak1jYUo3ZG44RkN6WjdTVkVTcGdZajk4bnEiLCJodHRwczovL2Nvbm5lY3QucmluZ2llci5jaC91cm46cmluZ2llcjpicmFuZC1uYW1lIjoiZW5lcmd5IiwidXJuOm9uZWxvZzpicmFuZC1uYW1lIjoiZW5lcmd5IiwiYXV0aF90aW1lIjoxNjI5MTAxNDAzfQ.QjsDwoRHLq2pGJ1ngmpkBAFn-gwH-6nCIqCAom-XXRRTlurlkYISqZDLknGpEoP1EJ3L42PHUhPjgRGfB-66hCB9tcbFrfx6d6Vr5uW378YeBHP-BC_6c3NjEspnaqomgCpM-WfLK6ETIEfr3S-MWbQ_g__YU8uXBAmOFHMC0bSgewgN0RTLvP53BAOLoLbsvv-kAAB2bGMGtXyXzvof-I-kiBPdtfOeO4bvXYY2kwJM6_pHDVvhpcP8Iq-CnwqYlwS29NezaqsABd4n7R8mH7vZT1IVc6H0gfRscVwpqXUnLyksdfMJkjaXM8anNu8Bfuvef2p10Xq4lLDDaXfEsQ; _gat=1; energy_game_session=8IbZrPceEemKfCNJ1ZQGA81pZ0AYesd2VXtTanT1'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    time.sleep(random.randint(3, 6))

    url = "https://game.energy.ch/api/win"

    payload="{\"name\":\"eair\",\"isTicketGame\":true}"
    headers = {
    'Host': 'game.energy.ch',
    'Connection': 'close',
    'Content-Length': '35',
    'Accept': 'application/json, text/plain, */*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://game.energy.ch',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://game.energy.ch/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'XSRF-TOKEN=OqoaJFBweWilnYdaAETDC0NOTUVeIZ8Pws4RadC8; energy_game_session=8IbZrPceEemKfCNJ1ZQGA81pZ0AYesd2VXtTanT1; _ga=GA1.2.990381397.1629101106; _gid=GA1.2.1552452295.1629101106; access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlM2UVRPR1h5RmYzWjV0RnlBQUdRbTdzZ1FDejlnMzl5Zm5OOXp4YlRkclEifQ.eyJqdGkiOiJCNndFN0xYWUs4QjhCTFlXQnp5MmsiLCJzdWIiOiJhdXRoMHxmNWE4MzE5Nzk5Y2E5Yjg4NGQ3Y2JjYjZiN2U3NDgyMTMxZWM1YjBhM2UwMDhmZjRmMTY2M2VhN2YxYWU5MWU5IiwiaWF0IjoxNjI5MTAxNDAzLCJleHAiOjE2MjkxODc4MDMsInNjb3BlIjoib3BlbmlkIGVtYWlsIiwiaXNzIjoiaHR0cHM6Ly9sb2dpbi5jb25uZWN0LnJpbmdpZXIuY2gvIiwiYXVkIjoiSldUOUdCak1jYUo3ZG44RkN6WjdTVkVTcGdZajk4bnEiLCJodHRwczovL2Nvbm5lY3QucmluZ2llci5jaC91cm46cmluZ2llcjpicmFuZC1uYW1lIjoiZW5lcmd5IiwidXJuOm9uZWxvZzpicmFuZC1uYW1lIjoiZW5lcmd5IiwiYXV0aF90aW1lIjoxNjI5MTAxNDAzfQ.QjsDwoRHLq2pGJ1ngmpkBAFn-gwH-6nCIqCAom-XXRRTlurlkYISqZDLknGpEoP1EJ3L42PHUhPjgRGfB-66hCB9tcbFrfx6d6Vr5uW378YeBHP-BC_6c3NjEspnaqomgCpM-WfLK6ETIEfr3S-MWbQ_g__YU8uXBAmOFHMC0bSgewgN0RTLvP53BAOLoLbsvv-kAAB2bGMGtXyXzvof-I-kiBPdtfOeO4bvXYY2kwJM6_pHDVvhpcP8Iq-CnwqYlwS29NezaqsABd4n7R8mH7vZT1IVc6H0gfRscVwpqXUnLyksdfMJkjaXM8anNu8Bfuvef2p10Xq4lLDDaXfEsQ; _gat=1; energy_game_session=8IbZrPceEemKfCNJ1ZQGA81pZ0AYesd2VXtTanT1'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    response = json.loads(response.text)
    if response['win'] == "true":
        break;

    time.sleep(random.randint(3, 5))
