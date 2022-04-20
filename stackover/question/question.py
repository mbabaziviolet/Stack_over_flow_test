from flask import request,jsonify,Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.security import check_password_hash,generate_password_hash
from stackover.models import Answers, Question, Users,all_questions,answers_list
import string, random
    
questions = Blueprint('questions', __name__, url_prefix='/questions')

#getting all questions
def get_all_questions():
      
  return [i for i in all_questions]

@questions.route("/", methods=['GET'])
def all_questions_list():
   

    user_questions = get_all_questions()
    return jsonify(user_questions)




def get_all_questions_specific():
      
  return [x for x in all_questions]
@questions.route("/<string:question_id>/", methods=['GET'])
def all_questions_specific(question_id):
      
    users_questions = get_all_questions_specific()
    return jsonify(users_questions)

#question endpoint
@questions.route('/question', methods= ['POST'])
def question():
  
  if request.method == "POST":
        question_id =  ''.join(random.choice(string.ascii_lowercase) for x in range(4))
        user_name = request.json["user_name"]
        title = request.json["title"]
        body = request.json["body"]
        
      
        
        
        
        #checking if title exists
        for question in all_questions:
              if question['title'] == title:
                      return jsonify({'error':'Title  already exists!'})
        
    
          
         #checking if body exists
      
        for question in all_questions:
              if question['body'] == body:
                     
                      return jsonify({'error':'body already in use!'})      
          
      
        
        
        #inserting values
        new_question = Question(question_id=question_id,user_name=user_name,title=title,body=body)
        all_questions.append( new_question.json_data())
           
        #using method jsonify to return the json data
        return jsonify({'question_id':question_id,'user_name':user_name,'title':title,'body':body})
  return jsonify({'error':'provide the right data'}) 

#answers endpoint
@questions.route('/<string:question_id>/answers', methods= ['POST'])
def answers(question_id):
  
  if request.method == "POST":
        answer_id = ''.join(random.choice(string.ascii_lowercase) for x in range(4))
        question_id = request.json['question_id']
        user_name = request.json["user_name"]
        body = request.json["body"]
        
      
        
        
        
   
        for answer_list in answers_list:
              if answer_list['body'] == body:
                      return jsonify({'error':'Body already exists!'})
        
          
        
        #inserting values
        new_answers = Answers(answer_id=answer_id,question_id=question_id,user_name=user_name,body=body)
        answers_list.append(new_answers.jsonData())
           
        
        return jsonify({'answer_id':answer_id,'question_id':question_id,'user_name':user_name,'body':body})
  return jsonify({'error':'invalid data'}) 



