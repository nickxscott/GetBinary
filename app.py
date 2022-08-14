from flask import Flask, render_template, request, flash
import math

app = Flask(__name__)
app.secret_key = "thisisthesecretkey"

@app.route('/')
def index():
  flash("enter base-10 integer")
  return render_template('index.html')

@app.route('/GetBinary', methods=["POST", "GET"])

def to_binary():
    
    x = int(request.form['integer'])
    
    #check if input is 0
    if int(x) == 0:
        flash("binary code: 0")
    
        return render_template('index.html')
    
    #if not 0, establish number of digits in the desired binary 
    n = (int(math.log(x, 2)) + 1)
    b = [0] * n
    #print(b)
    
    #insert 1 to first slot to represent first placeholder
    b[0] = 1

    #calculate initial remainder
    rem = x - (2**(len(b)-1))
    
    #distribute remainder among other digits in list b
    if rem != 0:
        for i in reversed(range(0,((len(b)-1)))): 
            if rem >= 2**i:
                b[-(i+1)] = 1
                rem = rem - 2**i
    
    #convert output from list to string
    output = ''
    for i in b:
        output += str(i)
        
    flash("binary equivalent: " + output)
    
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)











