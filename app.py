from flask import Flask, render_template, request
import  utility,math

  
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = request.form['age']
        rm = request.form['rm']
        brm = request.form['brm']
        population = request.form['population']
        connection = utility.get_db_connection()
        #open cursor
        try:
            cur = connection.cursor()
        except Exception as e:
            print(e)
        #execute the cursor
        stat = "SELECT TOP 1 PREDICT(USAHousingPriceModel USE USAHousingPriceModel_t1 WITH (,,"+str(age)+","+str(rm)+","+str(brm)+","+str(population)+")) FROM  SQLUser.usa_housing_train"   
        try:
            cur.execute(stat)
            pred = cur.fetchall()
            pred = pred[0][0]
            pred = "${:,.0f}".format(float(pred))
            return render_template('index.html', age=age,rm=rm,brm=brm,population=population,pred=pred)
        except Exception as e:
            print(e)          
              
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)