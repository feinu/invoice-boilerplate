import yaml

configfile = file('config.yml', 'r')
config = yaml.load(configfile)
configfile.close()

companyfile = file('companies/muster.yml', 'r')
company = yaml.load(companyfile)
companyfile.close()

clientfile = file('clients/muster.yml', 'r')
client = yaml.load(clientfile)
clientfile.close()

details = dict(config.items() + company.items() + client.items())
detailsfile = file('details.yml', 'w')
detailsfile.writelines('---\n')
yaml.dump(details, detailsfile)
detailsfile.writelines('---\n')
detailsfile.close()
