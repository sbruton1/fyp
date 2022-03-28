#MEMORY USAGE
import ps

print ("="*40, "Memory Information", "="*40)
# get the memory details
svmem = psutil.virtual_memory()
print (f"Total: {get_size(svmem.total)}")
print (f"Available: {get_size(svmem.available)}")
print (f"Used: {get_size(svmem.used)}")
print (f"Percentage: {svmem.percent}%")
