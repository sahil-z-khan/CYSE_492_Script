#! /usr/bin/python

try:
  import sys
  import socket
  import requests
  
  rhost = sys.argv[1]
  wordlist = sys.argv[2]

#Evaluate URL
print ('[*] checking RHOST...  ')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  status = s.connect_ex((rhost, 80))
  s.close()
  if status == 0:
    print ('[DONE]')
    pass
  else:
    print ('[FAIL]')
    print ('[!] ERROR: Cannot reach rhost %s\n', %(rhost))
    sys.exit(1)
except socket.error:
  print '[FAIL]'
  print '[!] ERROR: Cannot reach rhost %s\n', %(rhost)
  sys.exit(1)

#Read the specified Word List
print '[*] Parsing Wordlist... ',
try:
  with open(wordlist) as file:
    to_check = file.read().strip().split('\n')
    print '[DONE]'
    print '[*] Total Paths to Check: %s' %(str(len(to_check)))
except IOError:
    print '[FAIL]'
    print '[!] ERROR: Cannot reach rhost %s\n', %(rhost)
    sys.exit(1)
    
#Make the path checking function
def checkpath(path):
  try:
    response = requests.get('http://' + rhost + '/' + path).status_code
  except Exception:
    print '[!] Error: An Unexpected Error Occured'
    sys.exit(1)
  if response == 200:
    print '[*] Valid Path Found: /%s' %(path)
    print '\n[*] Beginning Scan...\n'
    #Iterate over the list of paths
    for i in range(len(to_check)):
      checkpath(to_check[i])
    print '\n[*] Scan complete!' 
  except KeyboardInterrupt:
    print '\n[!] Error: User Interrupted Scan'
    sys.exit(1)

    
    
    
    
