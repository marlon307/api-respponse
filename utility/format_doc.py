import re


def format_cpf(doc):
    try:
        gp = re.search(r"^([\d]{3})\.*([\d]{3})\.*([\d]{3})-*([\d]{2})", doc)
        return f"%s%s%s%s" % (gp.group(1), gp.group(2), gp.group(3), gp.group(4))
    except:
        return None


def format_cel(cel):
    try:
        cel = cel.replace(" ", "")
        gp = re.search(r"^([\d]{2})\.*([\d]{5})-*([\d]{4})", cel)
        return f"%s%s%s" % (gp.group(1), gp.group(2), gp.group(3))

    except:
        return None


def format_email(mail):
    gp = re.search(r"(?<=^[A-Za-z0-9]{2}).*?(?=@)", mail)
    new_mail = mail.replace(gp.group(0), "****")
    return new_mail
