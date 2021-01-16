## 동적 계획법
### N으로표현(210116, L3)
* 틀린 이유: ret[n] = ret[n-1] + ret[1]로 계산
* 수정: ret[n] = ret[n-s] + ret[s], s = 1~n-1