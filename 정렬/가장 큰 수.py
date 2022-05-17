#아래 코드는 원하는 답은 나오게끔 작성됐지만 런타임 오류가 걸려 정답 처리가 되지 못했다
#코드를 작성하면서도 분명 런타임에 걸릴 것이라고 생각했지만 다른 풀이 방식이 떠오르지 않았다.
"""
def solution(numbers):
    answer = []
    str_array = []

    str_array = list(map(str,numbers))#주어진 정수값을 모두 str변경

    while len(str_array) != 0:
        max = '0'
        for j in str_array: #0번째 인덱스를 비교하여 큰 수 찾기, 새로운 값 j가 더 클 경우 j를 max로 변경
            if max[0] < j[0]:
                max = j

            elif max[0] == j[0]: #첫번째 인덱스 값이 같을 경우 순차적으로 비교해서 더 큰 값을 찾는다.
                
                if len(max) < len(j):  #listcomprehension 가능할듯
                    min_len = len(max)
                    min_v = max
                    max_v = j
                else:
                    min_len = len(j)
                    max_v = max
                    min_v = j

                
                for i in range(0,min_len):
                    if max[i] < j[i]:
                        max = j
                        break
                    
                    if min_len-1 == i:    #for문이 끝까지 갔을 때 = min_len까지의 값이 같다.
                        if min_v[-1] > max_v[min_len]:
                            max = min_v
                        else:
                            max = max_v
        str_array.remove(max)
        answer.append(max)
    
    #리스트를 문자열로 바꿔서 출력
    answer = ''.join(answer)
    return answer

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))
"""

#다양한 풀이 방식이 있었지만 그 중 가장 충격적이였던 코드이다.
#일단 이 문제를 풀기 위해서는 문자열을 비교했을 때 
#앞자리 수 부터 아스키코드로 변환하여 비교한다는 점을 기억해야 한다.

# ex) 5 < 19   >>> false
# 첫번 째에 위치한 5 와 1을 비교하여 아스키코드로 변환했을 때 53과 49가 나오기 때문에 5가 더 크다는 결과가 나온다.
# 만약 5 와 51 을 비교했다면 두번 째 값이 있는 51이 더 큰 수일 것이다. 
"""
def solution(n):
    return str(int("".join(sorted(map(str,n),key= lambda x : (x*4),reverse = True))))
"""
