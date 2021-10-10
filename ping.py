import os, time, requests

url = 'URL DE VOTRE WEBHOOK'

// creation de notre boucle
while True:
    hostname = "LE SITE A PING"
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
      print (hostname, 'est en ligne!')
      data = {
    "content" : "MESSAGE DU BOT",
    "username" : "LE NOM D'UTILISATEUR"
}
      data["embeds"] = [
    {
        "description" : "Le site est en ligne",
        "title" : "PING BOT"
    }
]
      requests.post(url, json = data)
      time.sleep(900) // 900 = 15 minutes, 1 minutes = 60
    else:
      data = {
    "content" : "MESSAGE DU BOT",
    "username" : "NOM D'UTILISATEUR"
}
      data["embeds"] = [
    {
        "description" : "Le site est hors-ligne",
        "title" : "PING BOT"
    }
]
      requests.post(url, json = data)
      print (hostname, 'est down!')
      time.sleep(900) // 900 = 15 minutes, 1 minutes = 60
