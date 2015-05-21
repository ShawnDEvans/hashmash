I really love metasploit and OCL Hashcat, but they are at odds with each other when it comes to hashdump/smart_hashdump and OCL Hashcat output.  Hashcat only returns the hash and decrypted password, but as pentesters we kind of need that username.  This script will compare the msf (jtr) formatted hashdump and merge it with the Hashcat output to give you a neat list of users and their decrypted password.  

HashMash - decrypted password to username matcher

$ python hashmash.py <JTR Hash File> <OCL Hashcat Decrypted File>

User Hash File format is user:hash (or JTR NTLM)
OCL Decrypted Pasword File format is, hash:password
