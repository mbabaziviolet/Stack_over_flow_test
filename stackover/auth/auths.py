from flask import request ,jsonify,Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.security import check_password_hash,generate_password_hash
from stackover.models import Users,new_lists




auth = Blueprint('auth', __name__, url_prefix='/auth')


#register endpoint
@auth.route('/register', methods= ['POST'])
def register():
  
  if request.method == "POST":
        name = request.json["name"]
        email = request.json["email"]
        address = request.json["address"]
        password = request.json["password"]
      
        
        
        
        #checking if email exists
        for new_list in new_lists:
              if new_list['email'] == email:
                      return jsonify({'error':'Email  already exists!'})
        
    
          
         #checking if name exists
      
        for new_list in new_lists:
              if new_list['name'] == name:
                     
                      return jsonify({'error':'name already in use!'})      
          
          
          
      
        #creating a hashed password
        hashed_password = generate_password_hash(password,method="sha256")
        
        #inserting values
        new_student = Users(name=name,email=email,address=address,password=password)
        new_lists.append( new_student.json_data())
        return jsonify({'name':name,'email':email,'address':address,'password':hashed_password})
  return jsonify({'error':'provide the right data'}) 





#login endpoint
@auth.route('/login', methods= ['POST'])

def signin():
      
   
        if request.method == 'POST':
          email = request.json["email"]
          password = request.json['password']
        
          
          for user in new_lists:
                  if user['email'] == email:
                     
                      password_check = check_password_hash(user['password'],password)
                      print(password_check)
                      if password_check:
                      
                     
                        return jsonify({'user_email':user['email'],'username':user['name']})
                        
                      else:
                          return jsonify({'error':'wrong password'})
                              
                    
                  else:
                       return jsonify({'error':'Email  doesnt exist!'})
                
          return jsonify({'error':'user doesnt exists'})
          














