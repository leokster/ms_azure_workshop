import smtplib
import numpy as np
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
import yaml
import os

#git the directory of the current file
filedir = os.path.dirname(__file__)

#get credentials for the email server
email_cred = yaml.load(open(os.path.join(filedir,'email_credentials.yml'), 'r'), Loader=yaml.BaseLoader)

#get the list of recipients
recipients = open(os.path.join(filedir,'recipients.txt'), 'r').readlines()

#modify stylesheet for email
style_sheet = '''
<style>
.text-right{
    text-align:right;
}
th{
    text-align:left;
}
th{
    padding:0.2em;
    min-width:6em;
}
</style>
'''

def get_random_recipe():
    '''
    returns the url to a random recipe
    :return:
    '''
    recipes = open(os.path.join(filedir, "recipes.txt")).readlines()
    n_rec = len(recipes)
    random_index = np.random.randint(0,n_rec,1)[0]
    return recipes[random_index]

def get_random_recipe_full():
    '''
    returns url, the ingredients, the description and the title of a random recipe
    :return:
    '''
    url = get_random_recipe()[:-2]
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    for div in soup.find_all("div"):
        if "recipe-ingredients" in div.get("class", []):
            ingredients = div.prettify()

    for sec in soup.find_all("section"):
        if 'rezept-preperation' in sec.get("class"):
            description = sec.prettify()

    title = soup.find_all("h1")[0].text

    return url, ingredients, description, title

def gen_mail_content(url, target_mail, ingredients, description, title):
    '''
    returns an MIMEMultipart msg obj for an email
    :param url: url to recipe
    :param target_mail: email recipient
    :return:
    '''
    msg = MIMEMultipart()
    #msg.set_content("This is today your random recipe: {}. Enjoy!".format(url))
    msg['Subject'] = "Heutiges Zufallsrezept: {}".format(title)
    msg['From'] = email_cred.get("user")
    msg['To'] = target_mail
    msg.attach(MIMEText("<html>"+style_sheet+"<h1>"+title+"</h1><br>"+ingredients+"\n\n\n<br><br>\n\n\n"+description+"<br><br>"+url+"</html>", 'html'))
    return msg

def send_mails(url, contacts, ingredients, description, title):
    '''
    sends the email to all recipients in the list "contacts".
    :param url: url to recipe
    :param contacts: list of recipients email addresses
    :return:
    '''

    msgs = [gen_mail_content(url, cont, ingredients, description, title) for cont in contacts]
    s = smtplib.SMTP(email_cred.get("server"))
    s.login(email_cred.get("user"), email_cred.get("pw"))
    for msg in msgs:
        s.send_message(msg)
    s.quit()

if __name__ == "__main__":
    recipients = open(os.path.join(filedir, "recipients.txt"), "r").readlines()
    url, ingredients, description, title = get_random_recipe_full()
    send_mails(url=url, contacts=recipients, ingredients= ingredients, description=description, title=title)

