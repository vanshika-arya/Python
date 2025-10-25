N = int(input())
for i in range(N):
    work_num, SH, SM, EH, EM = map(int, input().split())
    
    start_minutes = (SH * 60) + SM
    end_minutes = (EH * 60) + EM
    duration_total_minutes = end_minutes - start_minutes
    duration_H = duration_total_minutes // 60
    duration_M = duration_total_minutes % 60
    print(duration_H, duration_M)