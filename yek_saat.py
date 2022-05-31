h, m = map(int, input().split(' '))
if h != 0:
    h = 12-h
    if h<10:
        h_str = '0'+str(h)
    else:
        h_str = str(h)
else:
    h_str = '00'

if m != 0:
    m = 60-m
    if m<10:
        m_str = '0'+str(m)
    else:
        m_str = str(m)
else:
    m_str = '00'

print(h_str+':'+m_str)