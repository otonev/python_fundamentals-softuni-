import sys
nums_count=3
max_num=-sys.maxsize
for n in range(nums_count):
    current_num=(int(input()))
    if current_num>max_num:
        max_num=current_num
print(max_num)