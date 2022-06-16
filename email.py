import smtplib

email = "<your_smtp_Email>"
password = "<your_smtp_password>"
hostname = "smtp.gmail.com"

with smtplib.SMTP(host=hostname) as connection:
      connection.starttls()
      connection.login(user=email, password=password)
      
        connection.sendmail(from_addr=email,
                           to_addrs="xyz@gmail.com",
                           msg="Subject: Test\n\n This is test email")
