from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY = 'RTT'
        )
        
    else:
        app.config.from_mapping(test_config)
        
    
    
    from stackover.auth.auths import auth
    from .question.question import questions
    app.register_blueprint(auth)
    app.register_blueprint(questions)

    
    

    @app.route("/")
    def hello():
        return "hello"    
    return app
