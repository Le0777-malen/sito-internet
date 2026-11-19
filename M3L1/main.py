import random
from flask import Flask

app = Flask(__name__)




@app.route("/")
def get_random_string():
    lista_fatti = ["La maggior parte delle persone che soffrono di dipendenza tecnologica sperimentano un forte stress quando si trovano al di fuori dell'area di copertura della rete o non possono utilizzare i loro dispositivi" 
                   , "Secondo uno studio condotto nel 2018, più del 50% delle persone di età compresa tra i 18 e i 34 anni si considera dipendente dal proprio smartphone" 
                   , "Lo studio della dipendenza tecnologica è una delle aree più rilevanti della ricerca scientifica moderna"
                   ,"Secondo uno studio del 2019, oltre il 60% delle persone risponde ai messaggi di lavoro sul proprio smartphone entro 15 minuti dall'uscita dal lavoro."
                   , "Un modo per combattere la dipendenza tecnologica è cercare attività che portino piacere e migliorino l'umore"
                   , "Elon Musk sostiene che i social network sono progettati per tenerci all'interno della piattaforma, in modo che trascorriamo il maggior tempo possibile a guardare contenuti"
                   ,"Elon Musk è anche favorevole alla regolamentazione dei social network e alla protezione dei dati personali degli utenti. Sostiene che i social network raccolgono un'enorme quantità di informazioni su di noi, che possono essere utilizzate per manipolare i nostri pensieri e comportamenti"
                   , "I social network hanno aspetti positivi e negativi e dobbiamo essere consapevoli di entrambi quando usiamo queste piattaforme."]
    
    return f'<p>{random.choice(lista_fatti)}</p>'

@app.route("/dadi")
def rool():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return f'<p>Il primo dado ha mostrato: {dado1}</p><p>Il secondo dado ha mostrato: {dado2}</p>'


@app.route('/random-animal')
def random_animal():
    animals = [
        '<img src="https://images.dog.ceo/breeds/hound-walker/n02089867_1030.jpg" alt="Dog Image">',
        '<img src="https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg" alt="Cat Image">'
    ]
    return random.choice(animals)
