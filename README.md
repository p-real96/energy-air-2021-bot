# Energy Air 2021 Game Bot
Dieses Script nimmt automatisch am diesjährigen (2021) Gewinnspiel für das Energy Air teil.
Das Script ist in Python geschrieben und wird via Kommando-Zeile gestartet.

## Usage
Um das Script starten zu können, müssen drei Parameter übergeben werden.
Die Parameter dienen zur eindeutigen Idenfizierung des Benutzers um am Gewinnspiel teilnehmen zu können.

Als erstes sollte das Chrome-Addon "EditThisCookie" heruntergerladen und im Chrome Browser installiert werden:
https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg/related?hl=de

Anschliessend meldet man sich im Browser auf der Energy-Air Website an und navigiert auf das Gewinnspiel.
Auf dieser Seite können die benötigten Cookies ausgelesen werden.

![Alt text](./cookies.png?raw=true "Title")

Hier werden die folgenden Cookies benötigt:
* XSRF-TOKEN
* energy_game_session
* access_token

Anschliessned wird das Script via Kommando-Zeile gestartet und die Cookies mit den Parameter übergeben

```bash
python3 app.py -x "<XSRF-TOKEN>" -e "<energy_game_session>" -a "<access_token>"
```
## Buy Me a Coffee
Wenn dir der Bot gefällt, würde ich mich über einen Kaffee freuen!
<a href="https://www.buymeacoffee.com/preal96" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
