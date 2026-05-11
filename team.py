# import requests
# import json

# # Paste your Teams webhook URL here
# webhook_url = "https://default371cb917b0984303b878c182ec8403.ac.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/b9639f7cb27d4d9eb5e52b331cb08736/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=EAn843l02vrZBUUcdbquKCwXAdD0pA_FtfHK_lPo20k"

# # Define the message payload
# message = {
#     "text": "🚀 Hello team! This is a test message sent via Teams webhook."
# }

# # Send the POST request
# response = requests.post(
#     webhook_url,
#     data=json.dumps(message),
#     headers={"Content-Type": "application/json"}
# )

# # Check response
# if response.status_code == 202:
#     print("Message posted successfully to Teams!")
# else:
#     print(f"Failed to send message: {response.status_code}, {response.text}")
import requests
import json

webhook_url ="https://default371cb917b0984303b878c182ec8403.ac.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/2633e42b55e44efdabdf024364b8608c/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=Hn7-H3EO4rmZoRr72h0qUOPnKWyiFtTzENfMy6YKwpo"
message = {"text": "gowth"}

print("Payload:", json.dumps(message, indent=2))

response = requests.post(
    webhook_url,
    data=json.dumps(message),
    headers={"Content-Type": "application/json"}
)

print("Status:", response.status_code)
print("Response text:", response.text)
