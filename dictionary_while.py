#Each line in the input consists of a key string and a value string separated by a space. 
#Use a while loop to read key-value pairs from input until "end" is read. 
#Add each key-value pair into the dictionary orders_record.

orders_record = {}
ip = input().split()

while ip[0] != "end":
    orders_record[ip[0]] = ip[1]
    ip = input().split()
    

print("Orders record:")
print(orders_record)
