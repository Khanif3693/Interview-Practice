import string   #strings functions like uppercase and lower case
import random   # to generate random password 
import sqlite3   # for sqlite3 connection
import requests  # for request data from API

def generate_password(length ,complexity): #def generate_password(length: int, complexity: int) -> str:
  
  def type1(l1):
    pwd1="" # some empty password
    for _ in range(l1):
      pwd1 = pwd1 + random.choice(string.ascii_lowercase) # choose random character from
      #the lowecase l1 times(length time)
   # print(pwd1)
    return pwd1  # return all lowercase
  def type2(l2):
    pwd2 = type1(l2-1) # get all lowercase except 1 and hence length passed is -1
    
    n = random.randint(0,l2) # random position for the digit
    pwd2 = pwd2[:n] + random.choice(string.digits) + pwd2[n:] #add digit to the password generated in step 1
   # print(pwd2)
    return pwd2
  def type3(l3):
    pwd3 = type2(l3-1) # satisfy first and second condition
    n = random.randint(0,l3) # generate random location for the uppercase
    pwd3 = pwd3[:n] + random.choice(string.ascii_uppercase) + pwd3[n:]
    return pwd3
  def type4(l4):
    pwd4 = type3(l4-1) # satisfy the first three cases for the password
    n = random.randint(0,l4)
    pwd4 = pwd4[:n] + random.choice(string.punctuation) + pwd4[n:]
    return pwd4

  if(complexity == 1): # if complexity is 1
    return type1(length)

  elif(complexity == 2): # if complexity is 2
    return type2(length)

  elif(complexity == 3): # if complexity if 3
    return type3(length)

  else:
    return type4(length) # if complexity is not other than any 3 describe above 
#than it will generate strong password with the complexity 4
#print(generate_password(8,4)) # test for generate function



def check_password_level(password): # def check_password_level(password: str) -> int:
  if (any([x.islower() for x in password])): # check if password contains all lowercase

    if(any([x.isdigit() for x in password])): # check for the digit
      if(any([x.isupper() for x in password])): # check for the upper case
        if(any([x in string.punctuation for x in password])):# check for the punctuation
          return 4 # if all true than return 4
        return 3 # if punctuation false but rest true than return 3
      if(len(password) >= 8):# if punctuation and upper case is failed then check length if greater than 8 then it is 3 else 2
        return 3
      return 2
    if(len(password) >= 8): # check length if greater than 8 return 2 else 1
      return 2
    return 1

#print(check_password_level(generate_password(8,4)))

def create_user(db_path): #def create_user(db_path: str) -> None:
    length = random.randint(6,12)
    complexity = random.randint(1,4)
    current_password = generate_password(length,complexity)
    r = requests.get('https://randomuser.me/api/?inc=name,email') # request for API
    data = r.json()  # get the data into data dictinaries
    fname = data["results"][0]["name"]["first"] + data["results"][0]["name"]["last"] # save full name
    email = data["results"][0]["email"] # save emailID
    conn = sqlite3.connect('db_path') #create connection
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS userInfo (name text, password text, email text)") # create table if not exists
    c.execute("insert into user (name,password, email) values (?,?, ?)",(fname,current_password, email)) # insert
    conn.commit() 
    conn.close() # close connectinos
    
    
#create_user(r'C:\Users\khani\Desktop\Nexus_edge\example.db')
for _ in range(10):
    create_user(r'C:\Users\khani\Desktop\Nexus_edge\nexus.db')

