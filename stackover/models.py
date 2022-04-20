
#my lists
new_lists = [] 
all_questions = [] 
answers_list = []
class Users:
    #Defining the model attributes
    def __init__(self, name,email,address,password):
        self.name = name
        self.email = email
        self.address = address
        self.password= password
    
    def json_data(self):
        return self.__dict__
        
    
    
 #creating a class called Question
  
class Question:
#Defining the model attributes
    def __init__(self,question_id, user_name,title,body):
        self.question_id = question_id
        self.user_name = user_name
        self.title = title
        self.body = body
        
    
    def json_data(self):
        return self.__dict__
        
     
        
#creating a class called Answers in the models    
class Answers():
    
    def __init__(self,answer_id,user_name,question_id,body):
        self.answer_id = answer_id
        self.body = body
        self.question_id = question_id
        self.user_name = user_name
    
       
       

    def jsonData(self):
            return self.__dict__       
     

