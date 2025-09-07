import random
import time
import requests
import sys

LOG_URL = None  # চাইলে server log url বসাও, না হলে None রাখো

def generate_otp(length=6):
    """Random OTP তৈরি"""
    return "".join([str(random.randint(0, 9)) for _ in range(length)])

def format_otp_message(otp):
    """OTP message template"""
    return f"[MyApp] Your verification code is {otp}. It will expire in 5 minutes."

def send_otp(phone_number):
    otp = generate_otp()
    message = format_otp_message(otp)
    
    # Console এ দেখাও
    print(f"[✔] Sent to {phone_number} → {message}")

    # চাইলে server এ পাঠানো যাবে
    if LOG_URL:
        try:
            requests.post(LOG_URL, json={
                "phone": phone_number,
                "otp": otp,
                "message": message
            })
        except Exception as e:
            print(f"[!] Could not log OTP: {e}")

    return otp, message

def main():
    print("📱 Bulk OTP Sender Simulator (Termux)")
    print("Paste phone numbers (one per line). When done, press Ctrl+D (Linux/Termux) or Ctrl+Z+Enter (Windows).")

    # একাধিক লাইন ইনপুট নেওয়া
    numbers_input = sys.stdin.read().strip().splitlines()
    numbers = [n.strip() for n in numbers_input if n.strip()]

    for number in numbers:
        send_otp(number)
        time.sleep(1)

if __name__ == "__main__":
    main()
