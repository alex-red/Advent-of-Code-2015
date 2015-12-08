import hashlib
INPUT = "ckczppom"

def main(IN):
  # MD5 Hashing
  ctr = 0
  m = ''
  while True:
    m = hashlib.md5((IN + str(ctr)).encode('utf-8')).hexdigest()
    if m[0:6] == '000000':
      print ('Found it: ')
      print (m, ctr, IN)
      break
    ctr += 1
  return m

if __name__ == '__main__':
  main('ckczppom')