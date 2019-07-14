# Flow Control (i) if/elif/else

###### Wu-Jun Pei @ CSCamp 2019

--

## 前情提要

---

#### I/O
- `print`
- `input`

---

#### Variables

- `int`
- `float`
- `str`
- `list`
- `tuple`
- `dict`

---

#### Boring
我的一元二次只能解有解，好想要順便叫電腦判斷有沒有解ㄛ

--

## If

---

#### If - 日常生活

- 如果 howhow 出新片，我就馬上去看
- 如果今天星巴克買一送一，我還不馬上衝出去喝一波

---

#### If - Python

```python
if [condition]:
    # do something
```
- Recall：python 是用縮排作為程式碼區塊劃分依據
- 通常以 4 個空格作為縮排
- 冒號：提示接下來要縮排

---

#### Example

如果我期末考低於 80 分，我就會被當

```python
if final_score < 80:
    print('I will get a F')
```

---

#### 常見判斷式
- `==`：判斷等於（Recall 一個等號的 `=` 是 <font class="Mark">賦值</font>）
- `!=`：不等於
- `<`、`<=`、`>`、`>=`：所唸極為所求

```python
1 / 3 == 0.333333333333333333333333
[1] < [1, 2, 3]
```

---

#### 常見判斷式
- `is`：可以用來判斷型態
- `in`：判斷 element 有沒有在一個 `list`/`tuple`/`dict` 裡面

```python
type(3.0) is int
3 in ['one', 2.0, 3]
```

---

#### 連接各個判斷式 - not、and、or

- `not`
- `and`
- `or`

```python
if myGender == 'Male' and myXingZuo == 'Leo':
    print('He must be a handsome boy')
it = 0.1

if it is not int:
    print('Then it must be a float')
```

---

#### Question

`not`、`and`、`or` 的優先度為何？
- 優先度的意義就像是先乘除後加減一樣，運算子也有優先順序
- Hint：嘗試看看
```python
0 and 0 or 1
1 or 0 and 0
```
- 善用小括號避免不必要紛爭

---

#### Answer

- To be continued...

---

#### Practice

---

#### Solution

--

## Else

---

#### Else - 日常生活

<font class="Mark">如果</font>天空打雷，我就要躲進騎樓；<font class="Mark">不然</font>如果出太陽，我就去買春山茶水；<font class="Mark">不然</font>我就繼續睡午覺。
- 如果：`if`
- 不然如果：`elif`（<font class="Mark">el</font>se <font class="Mark">if</font>）
- 不然：`else`

---

#### Else - Python

```python
if [condition1]:
    # do something
elif [condition2]:
    # do something
elif [condition3]:
    # do something
...
else:
    # do something
```

- 第一個只能是 `if`
- 中間可以有很多個 `elif`
- 最後可以有 `else`，也可以不要
- 善用 else 系列讓人生變得美好

---

#### Practice - 一元二次方程式 (Advanced)
$$ f(x) = ax^2 + b x + c$$
- 若該方程式無實數解，請輸出 "無實數解"
- 若該方程式重根，請輸出 "重根，x = "
- 若該方程式有相異解，請輸出 "有相異解，x = "

---

#### Practice - 一元二次方程式 (Advanced)
Sample Code
```python
ipt = input("請輸入 a, b, c，並以空白分開：").split(' ')
a, b, c = float(ipt[0]), float(ipt[1]), float(ipt[2])

if #TODO :
    print('無實數解')
elif #TODO :
    x = #TODO
    print('重根，x =', x)
else:
    x1 = #TODO
    x2 = #TODO
    print('有相異解，x =', (x1, x2))
```

---

#### Solution - 一元二次方程式 (Advanced)

To be continued...

---

#### Advanced - 條件表達式

```python
variable = true_value if condition else false_value
```

- 簡單美學









