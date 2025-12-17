import re
from datetime import datetime
import random
import json

def mail_gen():
    names = ["thiha"]
    random_name = random.choice(names)
    
    random_numbers = "".join(str(random.randint(0, 9)) for _ in range(4))
    
    generated_email = f"{random_name}{random_numbers}@gmail.com" 
    
    encoded_email = generated_email.replace("@gmail.com", "%40gmail.com")
    
    return encoded_email
