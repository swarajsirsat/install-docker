import smtplib

email = "swarajsirsat677@gmail.com"
password = "nptbtnsdafzlyept"
hostname = "smtp.gmail.com"

with smtplib.SMTP(host=hostname) as connection:
      connection.starttls()
      connection.login(user=email, password=password)
      
        connection.sendmail(from_addr=email,to_addrs="suvashsirsat123@gmail.com", msg="Subject: Test\n\n This is test email")
