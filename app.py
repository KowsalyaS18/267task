from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def query_example():
    
    name = request.args.get('name')

    
    age = request.args.get('age')

    
    place = request.args.get('place')

    return '''
              <h1>name: {}</h1>
              <h1>age: {}</h1>
              <h1>place: {}'''. format(name, age, place) 
                 
if __name__ == '__main__':
    app.run(debug=True)
