import requests
import json
import time

def main():

    botId = ""
    groupFromId = ""
    groupToId = ""
    urlFrom = "https://api.telegram.org/bot"+botId+"/getUpdates"
    urlTo = "https://api.telegram.org/bot"+botId+"/sendMessage?chat_id=-"+groupToId+"&text="

    last_message = None
    while True:

        response = requests.get(urlFrom)
        # print (response)
        content = response.content.decode("utf8")
        # print (content)
        updates = json.loads(content)
        # print (updates)
        num_updates = len(updates["result"])
        # print (num_updates)
        last_update = num_updates - 1
        message = updates["result"][last_update]["message"]["text"]
        # print (message)

        if (message) != last_message:
            if "delhi" in message.lower():
                response = requests.post(urlTo+message)
                # print (response)
            last_message = message
        time.sleep(0.5)

if __name__ == '__main__':
    main()