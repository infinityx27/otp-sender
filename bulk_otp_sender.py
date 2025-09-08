from twilio.rest import Client
import random
import sys

print("📱 Bulk OTP Sender via Twilio (Termux/PC)")

# 🔹 Step 1: Twilio Info Input
account_sid = input("Enter your Twilio Account SID: ").strip()
auth_token = input("Enter your Twilio Auth Token: ").strip()
twilio_number = input("Enter your Twilio Phone Number (e.g. +1XXXXXXXXXX): ").strip()

client = Client(account_sid, auth_token)

print("\nPaste phone numbers (one per line). When done, press Ctrl+D (Linux/Termux) or Ctrl+Z+Enter (Windows).")

# 🔹 Step 2: Read Numbers from stdin
numbers = []
try:
    for line in sys.stdin:
        line = line.strip()
        if line:
            numbers.append(line)
except EOFError:
    pass

print(f"\n✅ Total {len(numbers)} numbers loaded. Sending OTPs...\n")

# 🔹 Step 3: Send OTP
for num in numbers:
    otp = str(random.randint(100000, 999999))
    sms_body = f"[MyApp] Your verification code is {otp}. It will expire in 5 minutes."

    try:
        message = client.messages.create(
            body=sms_body,
            from_=twilio_number,
            to=num
        )
        print(f"[✔] Sent to {num} → OTP: {otp} (SID: {message.sid})")
    except Exception as e:
        print(f"[❌] Failed to send to {num}: {e}")

