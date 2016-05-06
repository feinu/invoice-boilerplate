import yaml
import os
import errno

def ensureDirectoryExists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


company = input('Choose a company: ')
description = input('Enter a description: ')

details = []

while True:
    detail = input('Enter additional details (blank to continue): ')
    if len(detail) > 0:
        details.append(detail)
    else:
        break

price = input('Enter the price: ')

item = {'description': description, 'price': price}

if details:
    item['details'] = details

identifier = input('Enter an identifier (so you can reuse this entry): ')
newfilepath = company + '/entries/' + identifier + '.yml';

ensureDirectoryExists(newfilepath)
newfile = file(newfilepath, 'w')
yaml.dump(item, newfile)
newfile.close()
