# parentNode

## 사용 방법

1. html문에서 DOS를 접근하는 방법 중에 하나로
   querySelector 등의 방법으로 받아온 후 그 다음에 사용한다.
   <br><br>
   html문에 있는 element의 위의 부분이 나온다.

EXAMPLE

```html
<table>
  <tr>
    <td id="hi">hi</td>
    <td>hello</td>
  </tr>
</table>
```

예를 들어 **const td = document.querySelector("#hi")** 로 td를 받아오면
<br>
**td.parentNode** 는 tr이 나오게 된다. 거기서 한 번 더하면 table이 나오게 된다.

# childNodes

### childNode는 parentNode와 다르게 여러개의 요소가 있을 수 있다.

### 부모는 하나고 자식은 여러 명일 수 있다고 생각하면 될 것 같다.

그래서 childNodes로 하면 **리스트** 로 결과값이 나온다.

사용방법은 parentNode와 다를 것 없이 td.childNodes로 사용하면 된다.

> firstchild = 첫번째 자식 노드

> lastchild = 마지막 자식 노드

> nextSibling = 다음 형제 노드

> previousSibling = 이전 형제 노드

> childNodes[1] 이런식으로 하면 두번째 자식 노드가 나온다!

javascript에서 html dos를 만들었을 때 사용하기 좋다.

2021.03.04
