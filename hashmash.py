#!/usr/bin/python

import sys


def usage():
    print 'HashMash - decrypted password to username matcher'
    print ''
    print '$ python %s <Hash File> <OCL Hashcat Decrypted File>' % sys.argv[0]
    print ''
    print 'User Hash File format is user:hash (or JTR NTLM)'
    print 'OCL Decrypted Pasword File format is, hash:password'
    print '' 
    sys.exit(1)

if len(sys.argv) != 3:
    print '[ERROR]\tWrong number of arguments'
    usage()  

try:
    hash_file = open(sys.argv[1])
    pass_file = open(sys.argv[2])
except IOError:
    print '[ERROR]\tInvalid input files, please review..'
    usage()

passDict = dict(line.split(':', 1) for line in pass_file)
hashes = hash_file.readlines()

for cracked_hash, passwd in passDict.iteritems():
    for hashItem in hashes:
        if len(hashItem) > 0:
            hashList = hashItem.split(':')
            if len(hashList) == 7 or len(hashList) == 4:
                user_name, user_hash = (hashList[0], hashList[3]) 
            else: 
                user_name, user_hash = (hashList[0], hashList[1])
            if cracked_hash.upper().strip() == user_hash.upper().strip():
                print '%s:%s' % (user_name.strip(), passwd.strip())
