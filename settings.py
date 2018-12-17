DEBUGMODE = True

# Domain detail
ismylife = {
    'DOMAINNAME': 'ismylife.me',
    'adminEmailAddress': 'admin.ismylife.me',
    'slaveRefresh': '1D',
    'slaveRetry': '30M',
    'slaveExpiration': '1W',
    'maximumCaching': '2H',
    'INPUTFILENAME': ['ismylife.csv'],
    'ONLYFORWARD': True,
    }
# Will create ismylife.db for forwarding file name
# file format is {domain name first word}.db
# Will create ismylife.rev for reversing file name
# file format is {domain name first word}.rev
# DOMAINNAME, INPUTFILENAME, ONLYFORWARD is required
# adminEmailAddress default is admin.{domain name}
# slaveRefresh default is 1D(86400)
# slaveRetry default is 30M(1800)
# slaveExpiration default is 1W(604800)
# maximumCaching default is 2H(7200)

# Please and all domain to the LIST
domainList = [ismylife]


def main():
    print(DEBUGMODE)
    print(domainList)
    return True


if __name__ == '__main__':
    main()
