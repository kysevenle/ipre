import re

def ipre(ip, subnet):
    #splitted = subnet.split('.')
    if validate_subnet(subnet):
        print('Valid')
    else:
        print('Not valid subnet')

    # for split in splitted:
    #     if int(split) > 255:
    #         print('not valid subnet')

def validate_subnet(subnet):
    splitted = subnet.split('.')
    for split in splitted:
        print(int(split))
        if int(split) == 255:
            return True


    #return re.compile()

testip = ipre('64.72.210.1', '255.240.240.253')



# if re.fullmatch(testip, '10.1.1.8'):
#     print('match')
# else:
#     print('No Match')
