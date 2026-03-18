data_samples = []

tokens = input().split()
for token in tokens:
    data_samples.append(int(token))
  
print("Original samples:", end=" ")
for samples in data_samples:
    print(samples, end=" ")
print()

copy = data_samples[:]

for i in range(len(data_samples)):
    if data_samples[i] >= 55:
        copy.remove(data_samples[i])
        
data_samples = copy
    
print("Filtered samples:", end=" ")
for samples in data_samples:
    print(samples, end=" ")
print()
