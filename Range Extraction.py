def solution(args):
    args.sort()
    i = 0
    sub_list = []
    
    while i < len(args):
        sub_list_start = args[i]

        while i + 1 < len(args) and args[i + 1] - args[i] == 1:
            i += 1
        
        sub_list_end = args[i]

        if sub_list_end - sub_list_start >= 2:
            sub_list.append(f"{sub_list_start}-{sub_list_end}")
        else:
            if sub_list_start == sub_list_end:
                sub_list.append(str(sub_list_start))
            else:
                sub_list.append(str(sub_list_start))
                sub_list.append(str(sub_list_end))
        i += 1
        
    return ','.join(sub_list)

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))