import requests

parameters: dict = {
    'amount': 100,
    'type': 'boolean'
}

request = requests.get('https://opentdb.com/api.php', params=parameters)
request.raise_for_status()
question_data: list = request.json()['results']
# Vai acontecer de ter HTML Entities, pir exemplo:&quot;Mongolia&quot, e para formatar precisamos de ir ao quiz_brain.py
# importei o html e acrescantar na linha 15: q_text = html.unescape(self.current_question.text)
