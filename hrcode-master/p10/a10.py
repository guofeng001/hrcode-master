c = {}
with open('../p10/data.json','a') as f:

   for v,k in f:
       if isinstance(int,k):
           b = {v,k}
           c.update(b)
   print(c)
f.close()