# this script was created by Alex Jabbour on Nov 15, 2019
import smtplib
import os
from recruiter_emails import recruiter_emails
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from mimetypes import guess_type
from email import encoders
import os

class coldmail:
    def __init__(self, recruiter_name, company_name, email_address,server):

        if (recruiter_name == None): recruiter_name = company_name + " hiring manager(s)"
        message = """Hello {}

I'm Sumanth and currently pursuing a Masters of Science in Computer Science at Viterbi School of Engineering.

I'm looking for student worker opportunities with {} in Spring 2023. I would like to check if there are any vacanies right now. I've experience in Software Development, Customer Experience Issues and have held leadership positions in the past. 

Here is something about me -

Prior to joining USC, I was working as Software Engineer at Amadeus, a travel technology company.In an agile development environment, I worked on developing products which required designing and implementing applications for travel reservations,responding to high priority customer escalations and producing bespoke changes in line with individual customer requirements.I have learned the theoretical and practical aspects of product life cycle and application development in a professional setup. 

Previously, I have also worked as a Campus Consultant for entrepreneurship club where I dealt with operations associated with events meant for the student community while achieving personal and organization goals

Would love to love hear back on any potential opportunities at {}

Please find my resume attached

Regards,
Venkat Sumanth Reddy Vadde
        """.format(recruiter_name,company_name,company_name)

        message_data = MIMEMultipart()
        message_data['From'] = "vvadde@usc.edu"
        message_data['To'] = email_address
        message_data["subject"] = "Student Worker Opportunities at {}".format(company_name)
        message_data.attach(MIMEText(message, 'plain'))
        attach_file_name = './Sumanth_Resume.pdf'
        filename=os.path.basename(attach_file_name)
        with open(attach_file_name, "rb") as attachment:
            mimetype, _ = guess_type(filename)
            mimetype = mimetype.split('/', 1)
            payload = MIMEBase(mimetype[0], mimetype[1])
            payload.set_payload(attachment.read())
            attachment.close()
            encoders.encode_base64(payload) 
            payload.add_header('Content-Disposition','attachment',filename="Sumanth_Resume.pdf")
            message_data.attach(payload)
        server.sendmail("vvadde@usc.edu", email_address, message_data.as_string())

if __name__ == "__main__":
    # run the script
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login("vvadde@usc.edu","afigbdwofrfnenib")

    # go thru each recruiter, taking the name, company and email
    for recruiter in recruiter_emails:
        print(recruiter["name"])
        coldmail(recruiter["name"], recruiter["company"], recruiter["email"],server)

    server.quit()


