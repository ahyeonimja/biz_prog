import streamlit as st

st.title('첫번째 웹 어플 만들기')

"""
#비즈니스 모델 분석

[네이버](https://www.naver.com)
[홍익대학교](https://www.hongik.ac.kr)

이것이 일반 본문 **이것이 굵은 글씨** *이것이 기울임 글씨* ~~이것이 취소선~~

:red[빨간색 글씨] :green[초록색 글씨] :blue[파란색 글씨]

```python
import streamlit as st

print("코드 블록")
```
"""

st.caption('캡션(작고 흐린 글씨로 표현됨):st.caption()')

with st.echo():
    name='Ahyeon Bae'
    st.write("Hello, Streamlit!",name)

st.latex("\int_a^b f(x)dx")
"$$\int_a^b f(x)dx$$"