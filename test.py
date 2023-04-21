from flask import Flask  
from flask import render_template
      
app = Flask(__name__) #creating the Flask class object   
     
@app.route('/') #decorator drfines the   
def home():  
    return render_template('base.php');  
      
if __name__ =='__main__':  
    app.run(debug = True)  