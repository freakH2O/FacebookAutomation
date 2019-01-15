from flask import Flask, render_template, request,redirect
from flask_pymongo import PyMongo
from waitress import serve
import os
started=[]
app = Flask(__name__)


app.config['MONGO_DBNAME']='users'
app.config['MONGO_URI']='mongodb://hamza:gogoville123@ds157064.mlab.com:57064/users'
app.inta = 1
app.dic=[]
mongo=PyMongo(app)

@app.route('/',methods={'POST','GET'})
def main():
    return """
    <html>
   <body>
   <h1>Please Enter The credentials to get started</h1>
      <form action = "/start" method = "POST">
         <h2>Automation Will automatically start once you press the button ,you may close the window after 10 seconds
         </h2>
         <h2>SERVERS RESTART EVERY 24 hours that means your account will be only automated for 24 hours you will need to re-enter the credentials after 24 hours</h2>
         <p>Username <input type = "text" name = "username" /></p>
         <p>Password <input type = "text" name = "password" /></p>
         <p>Comment <input type = "text" name = "comment" /></p>
         <p><input type = "submit" value = "Submit" /></p>
      </form>
   </body>
</html>
    """
@app.route('/start',methods=['POST','GET'])
def start():
    name=request.form['username']
    password=request.form['password']
    comment=request.form['comment']
    users=mongo.db.users
    users.insert_one({'username':name,
                      'password':password,
                      'comment':comment,
                       'index':app.inta})

    return redirect('/arpa')

@app.route('/arpa',methods={'POST','GET'})
def arpa():
    users=mongo.db.users
    d=users.find_one({'index':app.inta})
    name=d['username']
    app.inta+=1
    if name not  in app.dic:
        app.dic.append(name)
    else:
        return "<h1>Automation is already running against this Username Try Again in 24 Hours</h1>"
    password=d['password']
    comment=d['comment']
    print(name)
    print(password)
    print(comment)
    app.inta += 1
    import time

    from selenium.webdriver.common.keys import Keys
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By

    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    browser = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')
    browser.get('https://touch.facebook.com')
    time.sleep(2)
    email = browser.find_element_by_xpath('//*[@id="m_login_email"]')
    email.send_keys(name)
    pw = browser.find_element_by_xpath('//*[@id="m_login_password"]')
    pw.send_keys(password, Keys.ENTER)
    time.sleep(5)
    links = []
    done = []
    i = 0
    relay = True
    while relay == True:

        try:
            time.sleep(15)
            browser.refresh()
            browser.get('https://m.facebook.com/notifications')
            notif1 = browser.find_element_by_xpath(
                '/html/body/div[1]/div/div[4]/div/div[1]/div/div/div[1]/div/a/div/div[1]')
            links = browser.find_elements_by_class_name('touchable')

            dd = links[7].get_attribute('href')
            print(dd)

            # for link in links:

            i = 0
            if dd not in done:
                done.append(dd)
                notif1.click()
                time.sleep(5)
                comment = browser.find_element_by_id('composerInput')
                comment.send_keys(comment)
                time.sleep(7)
                submit = browser.find_element_by_name('submit')
                submit.click()
                time.sleep(4)


        except Exception:
            continue
    return "<h2>Arpa.net is live</h2>"



if __name__ == '__main__':
    from waitress import serve

    serve(app, host='0.0.0.0', port=8080)
    #serve(app, listen='*:8080')
    app.run(debug=True ,port=8080)