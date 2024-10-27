import os, requests, json
from secrets import randbelow
from base64 import b64encode as be, b64decode as bd
from Crypto.Cipher import AES
from hashlib import sha256
from Crypto.Util.Padding import pad, unpad

def encrypt_packet(packet,session_key):
    iv = os.urandom(16)
    cipher = AES.new(session_key, AES.MODE_CBC, iv)
    encrypted_packet = iv + cipher.encrypt(pad(packet.encode(), 16))
    return {'packet_data': be(encrypted_packet).decode()}

def decrypt_packet(data,session_key):
    #print("data", data)
    decoded_packet = bd(data)
    #print("decoded",decoded_packet)
    iv = decoded_packet[:16]
    #print("iv",iv, len(iv))
    encrypted_packet = decoded_packet[16:]
    #print("encrypted_packet",encrypted_packet)
    cipher = AES.new(session_key, AES.MODE_CBC, iv)
    decrypted_packet = unpad(cipher.decrypt(encrypted_packet), 16)
    packet_data = decrypted_packet
    return {"packet_data": packet_data}

URL = "http://127.0.0.1:1337" # Localhost
#URL = "http://83.136.252.233:35247" # remote host REMPLACER IP:PORT par l'hôte distant

#### test
# /api/request-session-parameters
# /api/init-session
# /api/request-challenge
# /api/dashboard : actions "flag" et "about"
# r = requests.post(f'{URL}/api/a-cool-endpoint', json={'key1': 'json', 'key2': 'data'})
r = requests.post(f'{URL}/api/request-session-parameters')

df_json = json.loads(r.content.decode())

g = int(df_json["g"],16)
p = int(df_json["p"],16)

print(json.dumps({
            "g": g,
            "p": p
        },indent=4))

b = randbelow(p)

my_pubkey = pow(g, b, p)

r = requests.post(f'{URL}/api/init-session', json={'client_public_key': my_pubkey})
r_json = json.loads(r.content.decode())

if 'error' in r_json:
    with open("session_info","r",encoding="utf-8") as f:
        session_info_json = json.load(f)
    server_public_key = session_info_json["server_public_key"]
    my_pubkey = session_info_json["my_pubkey"]
    b = session_info_json["my_secret"]
else:
    server_public_key = int(r_json['server_public_key'],16)
    with open('session_info','w',encoding="utf-8") as f:
        f.write(json.dumps({
            "server_public_key": server_public_key,
            "my_pubkey": my_pubkey,
            "my_secret": b
        }))
print(json.dumps({
            "server_public_key": server_public_key,
            "my_pubkey": my_pubkey
        },indent=4))

key = pow(server_public_key, b, p)

session_key = sha256(str(key).encode()).digest()
print("session:", session_key.hex())

r = requests.post(f'{URL}/api/request-challenge')
r_json = json.loads(r.content.decode())
print(json.dumps(r_json,indent=4))

ec = r_json["encrypted_challenge"]
print("ec",bd(ec))

dm = decrypt_packet(ec,session_key)
#print("dm", dm["packet_data"])

challenge_hash = sha256(dm["packet_data"]).hexdigest()

print("sha256", challenge_hash, len(challenge_hash))

r = requests.post(f'{URL}/api/dashboard', json={"challenge": challenge_hash,"packet_data": encrypt_packet('flag',session_key)["packet_data"]})
r_json = json.loads(r.content.decode())
print(json.dumps(r_json,indent=4))

print(decrypt_packet(r_json["packet_data"],session_key)["packet_data"].decode())