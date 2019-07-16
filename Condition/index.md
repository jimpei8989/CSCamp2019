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
if condition:
    # do something
```
- 冒號：提示接下來要縮排
- 縮排：四格空格，接下來有一樣縮排的程式碼都是同一個區塊

---

#### Example

如果我期末考低於 80 分，我就會被當

```python
if finalScore < 80:
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

#### 常見錯誤 (i)

```python
a, b = 1, 2
if a = b:
    print(a, b)
```
`SyntaxError`，不能只有一個 `=`，要變成 `==`

---

#### 常見錯誤 (ii)

```python
a, b = 1, 2 - 1
if a == b:
     print('haha')
    print(a, b)
```
`IndentationError`，要確定縮排的大小都一樣（建議是 4 格空格）

---

#### 邏輯運算 - not、and、or

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

#### 邏輯運算 - not、and、or

Ｑ: `not`、`and`、`or` 的優先度為何？<br>
Ａ: `not` > `and` > `or`
- 優先度的意義就像是先乘除後加減一樣，運算子也有優先順序
- 善用小括號避免不必要紛爭

NOTE:



---

#### Practice - EZcaptcha
自製 CAPTCHA
- 若使用者輸入的跟 `secret` 一樣，則認證為合法使用者，輸出 `'Valid User'`
- 若不一樣，則輸出 `'Invalid User'`

---

#### Practice - EZcaptcha
Sample Code（`howhow.py`）
```python
secret = 'abcdefghijklmnopqrstuvwxyz'
captcha = input('Please input the characters in the bracket \{{}\}\n>'.format(secret))

# TODO
```

---

#### Solution - EZcaptcha
To be continued......

--

## Elif/Else

---

#### Elif/Else - 日常生活

<font class="Mark">如果</font>天空打雷，我就要躲進騎樓；<font class="Mark">不然</font>如果出太陽，我就去買春山茶水；<font class="Mark">不然</font>我就繼續睡午覺。
- 如果：`if`
- 不然如果：`elif`（<font class="Mark">el</font>se <font class="Mark">if</font>）
- 不然：`else`

---

#### Elif/Else - Python

```python
if condition1:
    # do something
elif condition2:
    # do something
elif condition3:
    # do something

# ...

else:
    # do something
```

- 第一個只能是 `if`
- 中間可以有任意 `elif`
- 最後可以有 `else`，也可以不要
- 善用 else 系列讓人生變得美好

---

#### Elif/Else - Example

```python
score = int(input('Please input your math score: '))

if score >= 90:
    print('Great job')
elif score >= 60:
    print('Not bad, keep going on')
else:
    print('See you next year')
```

---

#### Practice - 一元二次方程式 (Advanced)
$$ax^2 + b x + c = 0$$

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

--

## Nested

---

#### Nested
- 不是 Nestea
- 一沙一世界，一縮排一天堂

---

#### Nested
```python
if condition_1:
    if condition_1_1:
        # do something
    elif condition1_2:
        # do something
elif condition_2:
    # do something
else:
    if condition_3_1:
        # do something
    else:
        if condition_3_2_1:
            # do something
```
要多深就可以多深

---

#### Nested
<img src="imgs/nested.jpg" style="width: 720px">

Reference: [Google Image](https://images.app.goo.gl/R5EUFg3tmStT9j5h8)

---

#### Nested - Example
```python
price = 8200
balance = int(input('Please input your balance: '))
desire = int(input('Please input your desire: '))
if balance > price:
    if desire > 0.5:
        print('Gonna buy it')
    else:
        print('No way')
else:
    if desire > 1 and len(rich_friends) >= 1:
        print('Borrow me money')
    else:
        print('I have no money')
```
好想買 switch ㄛ

