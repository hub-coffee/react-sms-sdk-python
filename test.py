from react_sms_sdk_python.react_sms import ReactSMS

def test_message_sending():
    auth_key = "rs_befb3ee389cf3a44864b75f36680fae5"
    api_key = "rs_3108861fc1044ca7920fdbc7133323ed"
    service_key = "938125"

    sdk = ReactSMS(auth_key, api_key, service_key)
    message = "just a test"
    phones = [{"zip_code":"+225", "number":"0758187266"}]

    return sdk.send(message, phones)


print("====== Test message sending =====")
print(test_message_sending())



def test_balance_checking():
    auth_key = "rs_befb3ee389cf3a44864b75f36680fae5"
    api_key = "rs_3108861fc1044ca7920fdbc7133323ed"

    sdk = ReactSMS(auth_key, api_key)
    return sdk.balance()

print("====== Test balance checking =====")
print(test_balance_checking())



def test_service_building():
    auth_key = "rs_befb3ee389cf3a44864b75f36680fae5"
    api_key = "rs_3108861fc1044ca7920fdbc7133323ed"

    sdk = ReactSMS(auth_key, api_key)

    service_name = "service test", 
    quota_sms = "0", 
    active_quota = False, 
    description = None

    return sdk.create_service(service_name, quota_sms, active_quota, description)

print("====== Test service building =====")
print(test_service_building())