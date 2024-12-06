import random
import string

def generate_random_email(domains):
    username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    domain = random.choice(domains)
    return f"{username}@{domain}"

domains = ['example.com', 'test.com', 'myemail.com', 'sample.net', 'demo.org']
email_list = [generate_random_email(domains) for _ in range(7)]
print(email_list)