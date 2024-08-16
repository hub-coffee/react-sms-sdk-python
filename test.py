from react_sms_sdk_python.react_sms import SMSAPI

def test():
    auth_key = "rs_befb3ee389cf3a44864b75f36680fae5"
    api_key = "rs_3108861fc1044ca7920fdbc7133323ed"
    service_key = "938125"

    sdk = SMSAPI(auth_key, api_key, service_key)
    return sdk.send("message", [{"zip_code":"+225", "number":"0758187266"}])

print(test())