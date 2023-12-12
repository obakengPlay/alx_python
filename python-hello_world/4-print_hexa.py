for i in range(99): 
    print ("{:d} = 0x{:x}".format(i, i) 
          if i > 15 else "{:d} = 0x{:02x}".format(i, i))