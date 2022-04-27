from pages.home_page import Home_page
from pages.login_page import Login_page
from pages.secure_page import Secure_page
from pages.forgot_password_page import Forgot_password_page
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.login_page = Login_page()
    context.home_page = Home_page()
    context.secure_page = Secure_page()
    context.forgot_password_page = Forgot_password_page()



def after_all(context):
    context.browser.close()


    # contextul este o cutiuta care contine cate un obiect de tipul fiecarei clase de pagini
    #before all=BDD
    #after all = BDD
    # de fiecare data cand adaugam o pagina noua in proiect, o vom adauga in context