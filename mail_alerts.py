"""
# Created :- Dishant [28-Aug-2022]
# Modified :- Dishant [28-Aug-2022]
# Usage :- Sendmail uitliy
"""

from os import path
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from smtplib import SMTP, SMTPException
from datetime import datetime, date, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


today = datetime.now().strftime(r'%d-%b-%Y')  # * today [DD-MMM-YYY]
content = '<H4><BR>Please Ignore This Is A Testing Mail.<BR><BR>Regards<BR>Compensation Team</H4>'
subject = f'Comp Team :- Testing Mail {today}'

# # * Internal Testing
# me = 'test@omnipayments.com'
# to = ['ankita.harad@omnipayments.com']
# cc = ['kanchan@omnipayments.com']
# bcc = ['dishant@omnipayments.com', 'tejaswini@omnipayments.com']

# * Actual Usage
me = 'no-reply@omnipayments.com'
to = ['ankita.harad@omnipayments.com', 'support@omnipayments.com']
cc = ['sushant@omnipayments.com', 'madhukar@omnipayments.com', 'dhanashree.sonawane@omnipayments.com',
      'Sachin@omnipayments.com', 'kanchan@omnipayments.com', 'sagar_bhosale@omnipayments.com',
      'cindy@omnipayments.com', 'shalaka@omnipayments.com', 'ankita@omnipayments.com',
      'jully@omnipayments.com', 'kalyani@omnipayments.com', 'vidhya@omnipayments.com',
      'abhinav@omnipayments.com']
bcc = ['dishant@omnipayments.com', 'tejaswini@omnipayments.com']


def sendmail_with_html_and_attachment(
        htmlContent: str = content,
        mailSubject: str = subject,
        attachFiles: list = None,
        secret: bool = False,
        sender: str = me,
        receiver: list = to,
        carbonCopy: list = cc,
        blindCarbonCopy: list = bcc) -> None:
    """
    Usage/Summary:
        - Send mail with these alternatives [ carbonCopy | blindCarbonCopy | attachemets | encryption ]

    Args:
        htmlContent (str, optional):
            - Mail Content. Defaults to content.
        mailSubject (str, optional):
            - Mail Subject. Defaults to subject.
        attachFiles (list, optional):
            - Attach An Array Of Files. Defaults to None.
        secret (bool, optional): 
            - Encode Msg To Cipher Text (Base64). Defaults to False.
        sender (str, optional):
            - Enter Senders Mail Id. Defaults to me.
        receiver (list, optional):
            - Enter Receiver Mail Id's. Defaults to to.
        carbonCopy (list, optional):
            - Enter CC Mail Id's. Defaults to cc.
        blindCarbonCopy (list, optional):
            - Enter BCC Mail Id's. Defaults to bcc.
    """

    # * Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['From'] = sender
    msg['To'] = ', '.join(receiver)
    msg['Cc'] = ', '.join(carbonCopy)
    # msg['Bcc'] = ', '.join(blindCarbonCopy) # * uncomment to reveal bcc to all
    msg['Subject'] = mailSubject

    # * Record the MIME types of both parts - text/plain/html
    part1 = MIMEText(htmlContent, 'html')
    msg.attach(part1)
    if secret:
        encoders.encode_base64(part1)  # * keep true for cipher msg/txt
    del part1, htmlContent, mailSubject, secret

    # * Start Attachments
    if attachFiles != None:
        try:
            for singleFile in attachFiles:
                baseFileName = path.basename(singleFile)
                # print(f"Files = {singleFile} | {baseFileName}") # * Kept For Testing / Debug
                attachment = MIMEApplication(open(singleFile, "rb").read(), _subtype="txt")
                attachment.add_header('Content-Disposition', 'attachment', filename=baseFileName)
                del baseFileName, singleFile
                msg.attach(attachment)
        except Exception as e1:
            print(f'attachFiles error : {e1}')
            del e1
        finally:
            del attachFiles

    # * Send Mail
    try:
        """
        * List of alternative ip and ports in case of failure
        1. ('192.168.3.60', 7025)
        2. ('New Ip', New Port)
        """
        s = SMTP('192.168.1.225', 8125)
        s.sendmail(sender, blindCarbonCopy, msg.as_string())
    except SMTPException as e2:
        print(f'Error smtplib.SMTPException : {e2}')
        del e2
    except Exception as e3:
        print(f'Error Exception : {e3}')
        del e3
    finally:
        s.quit()
        del s, msg


if __name__ == '__main__':
    sendmail_with_html_and_attachment(
        attachFiles=['test_one.txt', 'test_two.txt'])
