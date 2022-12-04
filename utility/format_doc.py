import re


def format_cpf(doc: str):
    try:
        gp = re.search(r"^([\d]{3})\.*([\d]{3})\.*([\d]{3})-*([\d]{2})", doc)
        if gp is not None:
            return f"%s%s%s%s" % (gp.group(1), gp.group(2), gp.group(3), gp.group(4))
    except:
        return None


def format_cel(cel: str):
    try:
        cel = cel.replace(" ", "")
        gp = re.search(r"^([\d]{2})\.*([\d]{5})-*([\d]{4})", cel)
        if gp is not None:
            return f"%s%s%s" % (gp.group(1), gp.group(2), gp.group(3))

    except:
        return None


def format_email(mail: str):
    # regex = r"(?<=).(?=[^@]*?@)|(?:(?<=@.)|(?!^)\G(?=[^@]*$))(.)(?=.*\.)"
    # result = re.sub(regex, "*", mail, 0, re.MULTILINE)

    if mail is not None:
        return mail
    return None
