def error_handler(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            print('No contact')
        except ValueError:
            print('Wrong number')
        except IndexError:
            print('Give me name and phone please')
    return inner

def hello_handler():
    return 'How can I help you?'

@error_handler
def add_handler(s):
   parts = s.split(' ')
   contacts.update({parts[1]:parts[2]})
   return "You've just added a new number."

@error_handler   
def change_handler(s):
    parts = s.split(' ')
    if parts[1] in contacts.keys():
        contacts[parts[1]] = parts[2]
        return f"You've just changed {parts[1]} number."
    else:
        return "Can't find this name."
    
@error_handler   
def phone_handler(s):
    parts = s.split(' ')
    phone = contacts.get(parts[1])
    if phone:
        return f'{parts[1]} number {phone}'
            
def show_all():
    for key, value in contacts.items():
        print(key, value)
        
contacts = dict()
  
while True:
    s = input()
    s_lower = s.lower()
    if any(keyword in s_lower for keyword in ["hello","add", "change", "phone", "show all", "good bye", "close", "exit"]):
        if s_lower == 'hello':
            print(hello_handler())
        if 'add' in s_lower:
            print(add_handler(s_lower))
        if 'change' in s_lower:
            print(change_handler(s_lower))
        if 'phone' in s_lower:
            print(phone_handler(s_lower))
        if 'show all' in s_lower:
            show_all()
        if any(keyword in s_lower for keyword in ["good bye", "close", "exit"]):
            print('Good bye!')
            break
    else:
        print('Try again!')
        
        
    

        
        
        
    
        
        
    