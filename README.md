# react-sms-sdk-python


SDK Python pour React SMS


## Installation du package


Pour l'installation rendez-vous sur https://pypi.org/project/reactsms-sdk-python/ ou 

    pip install reactsms-sdk-python==0.2


## Utilisation du package


    from react_sms_sdk_python.react_sms import ReactSMS


    class SMSAPI():

        AUTH_KEY = "rs_befb3ee389cf3a44864b75f36680fae5"

        API_KEY = "rs_3108861fc1044ca7920fdbc7133323ed"

        SERVICE_KEY = "938125"

        def __init__(self):
            self.sdk = ReactSMS(SMSAPI.AUTH_KEY, SMSAPI.API_KEY, SMSAPI.SERVICE_KEY)
        
        def send_message(self, message:str, phones:list):
            return self.sdk.send(message, phones)
        
        def balance(self):
            return self.sdk.balance()

        def create_service(self, service_name:str, quota_sms:int, active_quota:bool, description:str):
            return self.sdk.create_service(service_name, quota_sms, active_quota, description)