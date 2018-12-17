import os

DEBUGMODE = True

# Domain detail
ismylife = {
    'DOMAINNAME': 'ismylife.me',
    'adminEmailAddress': 'admin.ismylife.me',
    'slaveRefresh': '1D',
    'slaveRetry': '30M',
    'slaveExpiration': '1W',
    'maximumCaching': '2H',
    'INPUTFILENAME': 'ismylife.csv',
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

def debug_file_list(vm_domain):
    if vm_domain:
        file_list = [VM_10_1_6]
    else:
        file_list = [
            DMZ_10_1_0, CORE_10_1_1, LINUX_10_1_2, BSD_10_1_3, WWW_10_1_4,
            STORAGE_10_1_5, NET_10_1_7, PC_10_1_8, MAIL_10_1_9, TDMZ_10_1_10]
    return file_list


def debug_hostdb_list(vm_domain):
    if vm_domain:
        file_list = [('db.vm_host', 'db.vm_host')]
    else:
        file_list = [('db.private_host', 'db.cc')]
    return file_list


def debug_output_host(debug, vm_domain):
    if debug:
        if vm_domain:
            return os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                'working', 'db.vm_host')
        else:
            return os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                'working', 'db.private_host')
    else:
        if vm_domain:
            return os.path.join(
                os.sep, 'etc', 'named', 'cc.cs', 'db.vm_host')
        else:
            return os.path.join(
                os.sep, 'etc', 'named', 'cc.cs', 'db.private_host')


def debug_output_dir(debug):
    if debug:
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'working')
    else:
        return os.path.join(
            os.sep, 'etc', 'named', 'cc.cs')


def debug_output_db(debug):
    if debug:
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'working')
    else:
        return os.path.join(
            os.sep, 'etc', 'named', 'db.cc.cs')


def main():
    print(SOURCE_DIR)
    print(debug_output_host(DEBUGMODE, VMDOMAIN))
    print(debug_output_dir(DEBUGMODE))
    print(debug_output_host(False, True))
    print(debug_output_dir(False))
    return True


if __name__ == '__main__':
    main()
