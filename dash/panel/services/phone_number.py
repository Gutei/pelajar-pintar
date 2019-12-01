import re


def phone_validation(phone_number):
    pattern = r"\(?(?:\+62|62|0)(?:\d{2,3})?\)?[ .-]?\d{2,4}[ .-]?\d{2,4}[ .-]?\d{2,4}"
    res = re.match(pattern, phone_number)

    if hasattr(res, 'group'):
        return True

    return False


def format_number(phone_number):
    mobile_raw = list(phone_number)
    mobile_prefix = '{}{}{}'.format(mobile_raw[0], mobile_raw[1], mobile_raw[2])
    mobile_second_prefix = '{}{}'.format(mobile_raw[0], mobile_raw[1])

    mobile_digit = phone_number.split()
    mobile_init_digit = '+62'

    mobile = ''

    if mobile_prefix != '+62':
        if mobile_raw[0] == '0':
            mobile_raw[0] = '+62'
            mobile = ''.join(mobile_raw)
            return mobile
        else:
            if mobile_raw[0] == '+':
                if mobile_raw[1] == '6' and mobile_raw[2] == '2':
                    return phone_number
                else:
                    if mobile_raw[1] == '0':
                        mobile_raw[0] = '+62'
                        mobile_raw[1] = ''
                        mobile = ''.join(mobile_raw)
                        return mobile
                    else:
                        mobile_raw[0] = '+62'
                        mobile = ''.join(mobile_raw)
                        return mobile
            else:
                if mobile_raw[0] == '6' and mobile_raw[1] == '2':
                    mobile_raw[0] = '+6'
                    mobile = ''.join(mobile_raw)
                    return mobile
                else:
                    mobile = '{}{}'.format(mobile_init_digit, ''.join(mobile_digit))
                    return mobile
    else:
        return phone_number

    return mobile