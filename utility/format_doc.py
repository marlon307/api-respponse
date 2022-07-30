from cmath import log
import re


def format_doc(doc, rplc):
    gp = re.search(
        r"^[\d]{3}([\d]{3})([\d]{3})[\d]{2}",
        doc,
    )
    new_doc = doc.replace(f"%s%s" % (gp.group(1), gp.group(2)), rplc)
    return new_doc


def format_email(mail):
    gp = re.search(r"(?<=^[A-Za-z0-9]{2}).*?(?=@)", mail)
    new_mail = mail.replace(gp.group(0), "****")
    return new_mail
