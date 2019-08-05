import re

        #__Models__
requirements = []

def Req(req):
    requirements.append(req)

def Rule():
    for each in requirements:
        print(each)

def validator(password):
    alph = re.search(r'([A-Za-z])([0-9])',password)

    pass_lower = password.lower()
    
    
    if len(password) >= min or len(password) <= max:
        if pass_lower != password:
            return 'password is correct'
        else:
            return 'password is incorrect'
    else:
        return 'password is incorrect'
        
        # if alph:
            # return 'password is correct'
        # else:
            # return 'password is incorrect'
    return ''

def Start():
    print('Здравствуйте!')
    print('Введите пароль, он должен соответствовать следующим критериям :')
    Rule()


        #__setting__
min = 5
max = 10

Req('Cодержать от ' + str(min) + ' до ' + str(max) + ' символов')
Req('Иметь минимум одну большую букву')

# [&,+,@,$,#,%]


#______START_____
Start()
password = input('')
answer = validator(password)
print(answer)