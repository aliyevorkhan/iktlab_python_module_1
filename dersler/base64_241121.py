import base64

base64_message = 'UHl0aG9uIGlzIGZ1bg=='
print(base64_message)
base64_bytes = base64_message.encode('ascii')
print(base64_bytes)
message_bytes = base64.b64decode(base64_bytes)
print(message_bytes)
message = message_bytes.decode('ascii')
print(message)