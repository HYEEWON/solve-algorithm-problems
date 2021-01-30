from collections import deque
string = list(input())

st = deque()

for s in string:
    if s == '(' or s == '[':
        st.appendleft(s)
    elif len(st) <= 0:
        break

    if s == ']':
        if st[0] == '[':    
            st.popleft()
            st.appendleft(3)
        else:
            tmp = 0
            while len(st):
                if st[0] == '(' or st[0] == '[':
                    break
                tmp += st.popleft()
            if len(st) <= 0 or st[0] != '[':
                break
            st.popleft()    
            st.appendleft(tmp*3)
    elif s == ')':
        if st[0] == '(':    
            st.popleft()
            st.appendleft(2)
        else:
            tmp = 0
            while len(st):
                if st[0] == '(' or st[0] == '[':
                    break
                tmp += st.popleft()
            if len(st) <= 0 or st[0] != '(':
                break
            st.popleft()
            st.appendleft(tmp*2)
try:
    print(sum(st))
except:
    print(0)