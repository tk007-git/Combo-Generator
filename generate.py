import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="the output file", default='output.txt')
parser.add_argument("-t", "--type", help="combo / email", default='combo')
args = parser.parse_args()

namesfile = 'names.json'

combos = []


def subcombo():
    name = random.choice(names).lower() + random.choice(surnames).lower()
    name_extra = ''.join(random.choice(string.digits) for _ in range(random.randint(1, 4)))
    email_domain = random.choice(email_domains) + random.choice(domain_end)
    email = name + name_extra + '@' + email_domain
    password = random.choice(passwordlist)
    combo = ('{0}:{1}'.format(email, password)).encode()
    combos.append(combo)


def submail():
    name = random.choice(names).lower() + random.choice(surnames).lower()
    name_extra = ''.join(random.choice(string.digits) for _ in range(random.randint(1, 4)))
    email_domain = random.choice(email_domains) + random.choice(domain_end)
    email = name + name_extra + '@' + email_domain
    combo = ('{0}'.format(email)).encode()
    combo = combo + '\n'.encode()
    combos.append(combo)


def main():
    from tqdm import tqdm
    for _ in tqdm(range(1000000), unit=' Combos'):
        generator()
    writefile()


def writefile():
    with open(file, 'ab') as f:
        f.writelines(combos)
    f.close()
    del combos[:]


if __name__ == "__main__":
    file = args.output
    try:
        num_lines = sum(1 for _ in open(namesfile))
        print('Got {} Names!'.format(num_lines))
        import string

        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        import os
        import random

        random.seed = (os.urandom(2048))
        email_domains = ['gmail.', 'yahoo.', 'hotmail.', 'aol.', 'outlook.', 'gmx.', 'Yandex.', 'icloud', 'tutanota',
                         'protonmail.', 'fastmail.', 'zoho.', 'mail.', 'hushmail.', 'aichi.', 'aim.', 'airforce.',
                         'airforceemail.', 'airmail.', 'airpost.']

        domain_end = ['com', 'org', 'net', 'int', 'edu', 'gov', 'ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an',
                      'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd',
                      'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bl', 'bm', 'bn', 'bn', 'bm', 'bo', 'bq', 'br', 'bs', 'bt',
                      'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl',
                      'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr',
                      'ga', 'gd', 'ge', 'gf', 'gg', 'gh', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu',
                      'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'er', 'es', 'et', 'eu', 'id', 'ie', 'il',
                      'im', 'in', 'io', 'iq', 'is', 'it', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh',
                      'ki', 'km', 'kn', 'kp', 'kr', 'li', 'ma', 'mc', 'md', 'mh', 'nl', 'no', 'np', 'nz', 'om', 'pa',
                      'pl', 'rs', 'ru', 'sa', 'sd', 'se', 'sg', 'si', 'sk', 'tc', 'td', 'tr',
                      'tw', 'ua', 'ug', 'uk', 'um', 'us', 'uz', 'uy', 'vn', 'vu', 'za', 'zm', 'zw', 'mail']

        import json

        names = json.loads(open(namesfile, encoding="utf8").read())
        surnames = json.loads(open(namesfile, encoding="utf8").read())
        passwordlist = json.loads(open('passlist.json', encoding="utf8").read())

    except FileNotFoundError:
        print('You are missing the Following Files: names.json or passlist.json')
        exit()

    print('avalible modes: standard(email:pass), email(email)')

    if args.type == 'email':
        while 1:
            generator = submail
            main()
    else:
        while 1:
            generator = subcombo
            main()
