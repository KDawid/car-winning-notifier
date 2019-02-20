import smtplib

login = "kdawid93"
password = ""
from_addr = "kdawid93@gmail.com"
to_addr_list = ["kdawid93@gmail.com", "kdawid@hotmail.com"]
cc_addr_list = ""
subject = "Python e-mail"
message = "This is my first Python e-mail"


def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header = 'From: %s' % from_addr
    header += 'To: %s' % ', '.join(to_addr_list)
    header += 'Cc: %s' % ', '.join(cc_addr_list)
    header += 'Subject: %s' % subject
    message = header + message

    print("server")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    print("start")
    server.starttls()
    print("login")
    server.login(login, password)
    print("send")
    problems = server.sendmail(from_addr, to_addr_list, message)
    print("Problems: %s" % str(problems))
    server.quit()

sendemail(from_addr, to_addr_list, cc_addr_list, subject, message, login, password)
print("Done")