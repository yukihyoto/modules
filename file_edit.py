if __name__ == "__main__" :
  
  f = open("geomech_log_201607011814JST.txt","r")
  newfile = open("geomech_log_201607011814JST_e1.txt","w")
  
  
  # 6000 point = 10 min, 864000 point = 1 day, 2592000 point = 3 days
  length = 2892000
  
  # 6000
  for i in range(length) :
    line = f.readline()
    if i%6000 == 0 :
      flag = 1
    else :
      flag = 0
    
    if flag == 1 :
      newfile.write(line)
      flag = 0
    else :
      pass
    
  f.close()
  newfile.close()
