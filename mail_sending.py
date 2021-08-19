import smtplib
import email_pass_api_key as ep


MY_EMAIL = ep.EMAIL
MY_PASSWORD = ep.PASSWORD

with smtplib.SMTP('smtp.gmail.com') as smtp:
    smtp.starttls()
    smtp.login(
        user=MY_EMAIL,
        password=MY_PASSWORD
    )
    smtp.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=ep.MY_EMAIL,
        msg="Subject: Hello\n\nThis is how to send email using Python's SMTP module."
    )
    