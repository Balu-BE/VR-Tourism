from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=824dfd4d-99de-440d-9991-629c01b3832d.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30119;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=tkp83648;PWD=DnkqMxS8odNtHnMp",'','')
print(conn)

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/mettur')
def mettur():
    return render_template('mettur.html')

@app.route('/bhavanisagar')
def bhavanisagr():
    return render_template('bhavanisagar.html')

@app.route('/kodiveri')
def kodiveri():
    return render_template('kodiveri.html')

@app.route('/jkkm')
def jkkm():
    return render_template('jkkm.html')

@app.route('/index')
def index():
    return render_template('index.html')


# Registration page routing

@app.route('/register1',methods=["POST"])
def register1():
    x = [x for x in request.form.values()]
    print(x)
    EMAIL=x[0]
    PASSWORD=x[1]
    MOBILE=x[2]
    sql = "SELECT * FROM REGISTER WHERE EMAIL =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,EMAIL)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    print(account)
    if account:
        return render_template('login.html', pred="You are already a member, please login using your details")
    else:
        insert_sql = "INSERT INTO REGISTER VALUES (?, ?, ?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, EMAIL)
        ibm_db.bind_param(prep_stmt, 2, PASSWORD)
        ibm_db.bind_param(prep_stmt, 3, MOBILE)
        ibm_db.execute(prep_stmt)
        return render_template('login.html', pred="Registration Successful, please login using your details")
       
          
    
@app.route('/login1',methods=["POST"])
def login1():
    EMAIL = request.form['EMAIL']
    PASSWORD = request.form['PASSWORD']
    sql = "SELECT * FROM REGISTER WHERE EMAIL =? AND PASSWORD=?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,EMAIL)
    ibm_db.bind_param(stmt,2,PASSWORD)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    print (account)
    print(EMAIL,PASSWORD)
    if account:
            return render_template('index.html')
    else:
        return render_template('login.html', pred="Login unsuccessful.Incorrect username/password !") 
      
        
if __name__ == "__main__":
    app.run(debug =True, port =8080)