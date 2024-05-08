from flask import Flask




app = Flask(__name__)
app.app_context().push()


app.config['SECRET_KEY']= '06a0ac6eea0d291331e951fc3f3d3ae5'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'


from whatsapp_chat_analyse import routes