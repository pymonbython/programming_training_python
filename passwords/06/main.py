import requests
import logging

logging.basicConfig(level=logging.DEBUG)

def connect_ext_api(x):
    response = requests.get('https://api.pwnedpasswords.com/range/A94A8')
    logging.info(response.text)

    counter = response.text.splitlines()[0].split(':')[1]
    if int(counter) > x:
        return True
    
    else:
        return False


res = connect_ext_api(10)
logging.debug(res)
