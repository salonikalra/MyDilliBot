import requests
import json
import time    

def main():

    botId = ""
    groupFromId = ""
    groupToId = ""
    urlFrom = "https://api.telegram.org/bot"+botId+"/getUpdates"
    urlTo = "https://api.telegram.org/bot"+botId+"/sendMessage?chat_id=-"+groupToId+"&text="
    lastUpdateId = None
    
    while True:
        if lastUpdateId:
            response = requests.get(urlFrom+"?offset="+str(lastUpdateId))
        else:
            response = requests.get(urlFrom)
        # print (response)
        content = response.content.decode("utf8")
        # print (content)
        updates = json.loads(content)
        print (updates)

        if len(updates["result"]) > 0:
            num_updates = len(updates["result"])
            # print (num_updates)
            last_update = num_updates - 1
            message = updates["result"][last_update]["message"]["text"]
            # print (message)

            if "delhi" in message.lower():
                response = requests.post(urlTo+message)
                # print (response)

            updateIds = []
            for update in updates["result"]:
                updateIds.append(int(update["update_id"]))
            lastUpdateId = max(updateIds)
            lastUpdateId = lastUpdateId + 1
        time.sleep(0.5)

if __name__ == '__main__':
    main()