import requests

# API endpoint
url = "https://gatewayapi.telegram.org/sendVerificationMessage"

# Access token (Telegram Gateway sozlamalaridan olingan)
access_token = "AAEVFgAAN7e1lv7Dy8RpZNmIvplgaFvL37Q2dd33en_Pug"  # Bu yerga olingan tokenni qo‘ying

# Headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Payload
payload = {
    "phone_number": "+998901234567",  # Telefon raqamingiz (E.164 formatida)
    "code_length": 6,                # Kod uzunligi
    "ttl": 60                        # Kod amal qilish muddati (sekund)
}

# POST so‘rovini yuborish
try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    print("Response:", response.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)
    if response:
        print("Response:", response.json())