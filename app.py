from flask import Flask,Response,jsonify, render_template ,logging,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
# from flask import *
# import os
# import socket

# app = Flask(__name__)

# # app.config["Debug"] = True
# @app.route('/')
# @app.route('/home')
# def home():
#     return render_template('index.html')

    
# if __name__ == '__main__':
#     app.run()


# PORT = int(os.environ.get("PORT", 80))
# if __name__ == '__main__':
#     app.run(threaded=True,host='0.0.0.0',port=PORT)

# if __name__ == "__main__":
#   app.run(host='0.0.0.0', port=80)
