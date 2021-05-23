from Cryptodome.Hash import SHA256
import time
Target=0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
data='DOGETOTHEMOON'
ans=-1
time1 = time.time()
i=0
while True :
  hash = SHA256.new()
  message=data+str(i)
  message=message.encode('utf-8')
  hash.update(message)
  enc=hash.hexdigest()
  if int(enc, 16)<Target :
    ans=i
    break
  i=i+1
time2=time.time()
print('Time: ',time2-time1,'  Number: ',ans)
