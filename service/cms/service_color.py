from models.database import execut_query
from models.model_color import qColor
from utility.generat_id import generate_id
from cryptography.fernet import Fernet
from utility.u_user import send_mail_confirm_user


class sColor:
    def s_create_color(json):
        execut_query.insert(qColor.q_insert_color(), json)
        return True
