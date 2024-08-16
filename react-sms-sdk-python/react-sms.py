# React SMS
# Copyright (c) 2022-2024 React SMS
# Licensed under the MIT License. See LICENSE file for more details.


import requests, base64, json


class SMSAPI():

    AUTH_KEY = "rs_befb3ee389cf3a44864b75f36680fae5"
    API_KEY = "rs_3108861fc1044ca7920fdbc7133323ed"
    SERVICE_KEY = "938125"
    BASE_URL = "https://react-sms.com/messages"


    def __init__(self):
        TOKEN = SMSAPI.tokenBuilder()

        self.headers = {
            'Authorization': 'Bearer {}'.format(TOKEN),
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
        }


    @staticmethod
    def tokenBuilder():
        text = "{}:{}".format(SMSAPI.AUTH_KEY, SMSAPI.API_KEY)
        return base64.b64encode(text.encode('utf-8')).decode('utf-8')


    def send(self, message, recipients):
        payload = {
            "message": message,
            "numbers": json.dumps(recipients),
            "serviceKey": SMSAPI.SERVICE_KEY
        }

        try:
            response = requests.post(SMSAPI.BASE_URL+"/send", json=payload, headers=self.headers)
            response.raise_for_status() 
            data = response.json()

        except requests.exceptions.HTTPError as http_err:
            return JsonResponse({'error': str(http_err)}, status=400)

        except Exception as err:
            return JsonResponse({'error': str(err)}, status=500)

        return data #JsonResponse(data)


    
    def balance():
        pass