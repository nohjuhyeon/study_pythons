# 문제 설명
## S사에서는 각 부서에 필요한 물품을 지원해 주기 위해 부서별로 물품을 구매하는데 필요한 금액을 조사했습니다. 그러나, 전체 예산이 정해져 있기 때문에 모든 부서의 물품을 구매해 줄 수는 없습니다. 그래서 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.

## 물품을 구매해 줄 때는 각 부서가 신청한 금액만큼을 모두 지원해 줘야 합니다. 예를 들어 1,000원을 신청한 부서에는 정확히 1,000원을 지원해야 하며, 1,000원보다 적은 금액을 지원해 줄 수는 없습니다.

## 부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때, 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
## d는 부서별로 신청한 금액이 들어있는 배열이며, 길이(전체 부서의 개수)는 1 이상 100 이하입니다.
## d의 각 원소는 부서별로 신청한 금액을 나타내며, 부서별 신청 금액은 1 이상 100,000 이하의 자연수입니다.
## budget은 예산을 나타내며, 1 이상 10,000,000 이하의 자연수입니다.
# 입출력 예
## d	budget	result
## [1,3,2,5,4]	9	3
## [2,2,3,3]	10	4
# 입출력 예 설명
# 입출력 예 #1
## 각 부서에서 [1원, 3원, 2원, 5원, 4원]만큼의 금액을 신청했습니다. 만약에, 1원, 2원, 4원을 신청한 부서의 물품을 구매해주면 예산 9원에서 7원이 소비되어 2원이 남습니다. 항상 정확히 신청한 금액만큼 지원해 줘야 하므로 남은 2원으로 나머지 부서를 지원해 주지 않습니다. 위 방법 외에 3개 부서를 지원해 줄 방법들은 다음과 같습니다.

## 1원, 2원, 3원을 신청한 부서의 물품을 구매해주려면 6원이 필요합니다.
## 1원, 2원, 5원을 신청한 부서의 물품을 구매해주려면 8원이 필요합니다.
## 1원, 3원, 4원을 신청한 부서의 물품을 구매해주려면 8원이 필요합니다.
## 1원, 3원, 5원을 신청한 부서의 물품을 구매해주려면 9원이 필요합니다.
## 3개 부서보다 더 많은 부서의 물품을 구매해 줄 수는 없으므로 최대 3개 부서의 물품을 구매해 줄 수 있습니다.

# 입출력 예 #2
## 모든 부서의 물품을 구매해주면 10원이 됩니다. 따라서 최대 4개 부서의 물품을 구매해 줄 수 있습니다.

# def solution(d, budget):
#     list_c = [d]
#     list_a = []
#     answer = 0
#     if sum(d) <= budget:
#         answer = len(d)
#     else:
#         for x in range(len(d)-1):
#             for i in range(len(list_c)):
#                 list_a.append(list_c[i])
#             list_c=[]
#             pass
#             for i in range(len(list_a)):         
#                 for j in range(i,len(list_a[i])):
#                     list_b = []
#                     for k in range(len(list_a[i])):
#                         list_b.append(list_a[i][k])
#                     list_b.remove(list_a[i][j])
#                     list_c.append(list_b)
#                     pass
#                 pass
#             pass
#             for i in range(len(list_c)):
#                 if sum(list_c[i]) <= budget:
#                     answer = len(list_c[i])
#                     break
#             if answer != 0:
#                 break
#             list_a=[]
#     return answer

# def solution(d, budget):
#     list_a = []
#     list_c = []
#     answer = 0
#     for i in range(len(d)):
#         list_b = []
#         list_b.append(d[i])
#         list_c.append(list_b)
#         list_a.append(list_b)
#     pass
#     repeat = 1
#     for k in range(4):
#         list_d=[]
#         for i in range(len(list_a)):
#             index = 0
#             for m in range(repeat):
#                 for j in range(i+k+1,len(d)):
#                     list_b=[]
#                     for x in range(len(list_c[index+m+i])):
#                         list_b.append(list_c[index+m+i][x])
#                         pass
#                     pass
#                     if sum(list_b) > budget:
#                         answer = k+1
#                         break
#                     else:
#                         list_b.append(d[j])
#                         pass
#                         list_d.append(list_b)
#                         pass
#                     pass
#                 pass
#             index = repeat-1-i    
#             if answer !=0:
#                 break
#         if answer != 0:
#             break
#         else:
#             repeat = len(list_a)
#         pass
#         list_c=[]
#         for i in range(len(list_d)):
#             list_c.append(list_d[i])
#         pass
#         list_a = []
#         for i in range(len(list_c)):
#             list_a.append(list_c[i])
#     return answer

# def solution(d, budget):
#     list_a = []
#     list_d = []
#     for i in range(len(d)):
#         list_b = []
#         list_b.append(d[i]) 
#         list_a.append(list_b)
#         # list_d.append(list_b)
#     pass
#     x = 1
#     for k in range(3):
#         list_d=[]
#         for y in range(len(list_a)): 
#             for i in range(x,len(d)):
#                 list_c = []
#                 for j in range(len(list_a[y])):
#                     list_c.append(list_a[y][j])
#                     pass
#                 pass
#                 list_c.append(d[i])
#                 list_d.append(list_c)
#                 pass
#             x += 1
#             pass
#         x -= 4
#         list_a = []
#         for i in range(len(list_d)):
#             list_a.append(list_d[i])
#     answer = list_a
#     return answer

# def solution(d, budget):

#     list_c = [d]
#     list_b=[]
#     pass
#     answer = 0
#     if sum(d) <= budget:
#         answer = len(d)
#     else:    
#         for j in range(len(list_c[0])-1):
#             list_b = list_c[:]
#             list_c = []
#             for k in range(len(list_b)):
#                 for i in range(len(list_b[0])):
#                     list_a =list_b[k][:i] + list_b[k][i+1:]
#                     if list_a not in list_c:
#                         list_c.append(list_a)
#                     pass
#                 pass
#             # for i in range(len(list_c)):
#             #     if sum(list_c[i])<= budget:
#             #         answer = len(list_c[i])
#             #         break
#             # if answer != 0:
#             #     break
#             pass
#             list_b=[]
#             pass
#     return answer


# def solution(d, budget):
#     list_b = []
#     list_e=[]
#     for i in range(len(d)):
#         list_a = d[:]
#         list_a.remove(d[i])
#         list_b.append(list_a)
#     for i in range(len(d)):
#         list_a = []
#         list_a.append(d[i])
#         list_e.append(list_a)
#     answer = list_e+list_b
#     list_c = []
#     count = 0
#     for i in range(len(list_b)):
#         for k in range(count,len(list_b[i])):
#             list_d = list_b[i][:]
#             list_d.remove(list_b[i][k])
#             list_c.append(list_d)
#         count += 1
#     count=1
#     answer += list_c
#     list_c=[]
#     for i in range(len(list_e)):
#         for k in range(count,len(d)):
#             list_d = list_e[i][:]
#             list_d.append(d[k])
#             list_c.append(list_d) 
#             pass
#         count += 1
#     answer += list_c
#     pass
#     return answer

def solution(d, budget):
    d.sort()
    sum_d = sum(d)
    answer = 0
    for i in range(len(d)):
        if sum_d <= budget:
            answer = len(d)-i
            break
        else:
            sum_d = sum_d - d[-i-1]
            pass
        pass
    return answer

d = [11,12,13,14]
budget = 10
answer = solution(d,budget)
print(answer)