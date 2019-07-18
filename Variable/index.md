# Input/Output & Variables

###### Wu-Jun Pei @ CSCamp 2019

--

## Output

---

#### Output - Hello World
```python
print("Hello World")
```
- 關鍵字 `print`
- 括號內可以放一個或多個任意型態的東西，用逗號隔開

---

#### Output - Example

```python
print(12345, 3.1415, "Hello")
```
- 會用空白幫你分開每個東西，最後會印一個換行

--

## Variables (i)

---

#### Types of Variables (i)

- `int`：整數，如 `-87`、`1450`
- `float`：浮點數，如 `3.1415926`、`0.0`
- `bool`：布林變數，如 `True`、`False`
- `str`：字串，如 `'python'`、`'CSIE Camp 最高'`
- `None`

---

#### int & float
- 整數（<font class="Mark">int</font>eger）
    - 可以正負，大小沒有範圍限制！<br>
    <font class="Comment">註：很多程式語言對於整數都有範圍的限制</font>
- 浮點數（<font class="Mark">float</font>）
    - 基本上可以理解為小數
    - 會有誤差

---

#### 宣告－賦值
此時的等於的意義為「<font class="Mark">賦值</font>」，與「判斷等於」為不一樣的東西。
```python
a = 17
b = 3
c = 23.45
d = 1.67676767676767
```

---

#### 宣告－變數名稱
- 使用英文字母（`'a-zA-Z'`）、數字（`'0-9'`）、底線（`'_'`）
- 開頭不能使用數字
- 不要撞到 python 的名稱（e.g. `import`、`try`、......）
- (Ｏ) `a`、`numberOfStudents`、`my_poor_GPA`、......
- (Ｘ) `4fun`、`from`、`emoji_>.<`、......
- Yet another war......

---

#### 前四則運算

加減乘除
```python
a = 7
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```
- 這裡的除是會一般的除法
- 先乘除後加減
- 小括號有一樣的功用

---

#### 後三則運算
```python
print(a // b)
print(a % b)
print(a ** b)
```
- `//`：取商
- `%`：取餘數
- `**`：取次方，$a^b$

---

#### 修改變數值
- 重新賦值：運算後再存進變數中
- 運算子等於：將值直接做更動

```python
x = 0
x = x + 3   # x = 3
x += 4      # x = 7
x = x - 2   # x = 5
x -= 1      # x = 4

x *= 3.5    # x = 14
x /= 0.7    # x = 20

x %= 11     # x = 9
x //= 2     # x = 4
x **= 3     # x = 64
```

---

#### Practice - 一元二次方程式

題目敘述
- 有 <font class="Mark">兩相異實數解</font> 之一元二次方程式
$$ax^2 + bx + c = 0$$
- 假設 $a = 1, b = -5, c = 4$，請由小到大輸出兩個解

Hint
- 開根號就是**乘乘** $0.5$ 喔！
- 公式解
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

---

#### Sample Code - 一元二次方程式
`quadratic.py`
```
a = 1
b = -5
c = 4

x1 = # TODO
x2 = # TODO
print("x1 =", x1)
print("x2 =", x2)
```

---

#### Solution - 一元二次方程式
To be continued...

---

#### bool

- 只有 `True` 和 `False`，第一個字母是<font class="Mark">大寫</font>
- 判斷式的回傳值

---

#### str
- 字串（<font class="Mark">str</font>ing）
- 不一定只能放英文字母，基本上你打得出來的字就能放上去
- 使用單引號或雙引號包起來<br>
    e.g. `'this is a string'`、`"this is another string"`
- 宣告
```python
s1 = 'Python is so easy'
s2 = "維大力，義大利"
```

---

#### str - 加乘
- 加法：把兩個字串串在一起
- 乘法：複製自己好多次
```python
pineapple = 'pine' + 'apple'    # 'pineapple'
oops = 'o' * 10 + 'ps'          # 'oooooooooops'
```

---

#### str - len & item
- `len(s)`：得到 `s` 的長度
- `s[i]`（get item）：得到由 s 的第 i 個字元組成的字串（從 <font class="Mark">零</font> 開始數）
- 若 `i` 是 <font class="Mark">-k</font>，則代表取倒數第 <font class="Mark">k</font> 個字元
```python
s = 'abcdefghijklmnopqrstuvwxyz'
#    0123456789
#              0123456789
#                        012345
print(s[3], type(s[3]), s[-1])
```

---

#### str - Immutable
想要把 s 變成 abbdef...

```python
s = 'abcdefghijklmnopqrstuvwxyz'
#    0123456789
#              0123456789
#                        012345
s[2] = 'b'
```

- str 是 <font class="Mark">Immutable</font>（不可改變的）
- 不能改變其中某一個字／一段子字串，只能 <font class="Mark">重新賦值</font>

---

#### None
什麼都不是

---

#### type
可以使用 `type(variable)` 查看一個變數的型態，e.g.
```python
type(33)
type('wwwww')
type(11 / 3)
type(11 // 3)
type(int)
```

---

#### 型態轉換
直接用新的型態將原本的變數用小括號包起來，e.g.
- `str_a` 是一個字串 `'33'`，把他轉換成 `int` 並存在 `int_a` 之中
```python
str_a = '33'
int_a = int(str_a)
print(int_a, type(int_a))
```
- 再轉成浮點數
```python
float_a = float(int_a)
print(float_a, type(float_a))
```

--

## Input

---

#### Input

```python
input()
```
- 讀取使用者輸入，以 <font class="Mark">行</font> 為單位
- 會回傳一個 `str` 型態

---

#### Input
也可以在中間放一個 <font class="Mark">字串</font> 作為輸入的提示，e.g.
```python
name = input('Please input your name: ')
salary = input('Please input your salary: ')
```

---

#### Input - 基本套路
input 搭配轉型，e.g.

```python
salary = int(input('Please input your salary: '))
```

---

#### Practice - 超速のㄅㄩ
ㄅㄩ是個騎車不遵守交通法規的屁孩大學生。<br>此時此刻在基隆路上，他突然發現前方有警察架起測速機準備抓超速，此時他的時速是 $v$ km/h，而速限是 50km/h，經過他眼睛內建距離判斷系統，他距離被拍照的點 $A$ 的距離是 $d$ m。<br>試問ㄅㄩ需要以多少的加速度 $a$ 減速才會恰好在經過 $A$ 時時速 <font class="Mark"> 恰好 </font> 為 50km/h？

---

#### Sample Code - 超速のㄅㄩ
`speeding.py`
```python
input('Input v: ')
input('Input d: ')

print('Output a: ')
```
- Input：
```
87
63.3773
```
- Output：
```
-3.0856990058733684
```

---

#### Practice - 超速のㄅㄩ

<font class="Mark">懸賞</font>：<br>
正確且使用程式碼行數最短者將可獲得獎勵！

Hint
- $\quad v^2 = v_0^2 + 2as \Rightarrow a = \frac{v ^ 2 - v_0 ^ 2}{2s}$
- 注意型態（`input` 得到的型態是 <font class="Mark">str</font>，計算建議使用 <font class="Mark">float</font>）
- 注意單位（$x$ km/h -> $\frac x {3.6}$ m/s）

---

#### Solution - 超速のㄅㄩ
To be continued...

- Great，以後的物理作業可以用程式打了（Ｘ

---

#### Solution - 超速のㄅㄩ（Oneline）
To be continued...
- 你們八成看不懂 😅

--

## Variables (ii)

---

#### Types of Variables (ii)
- `list`
- `tuple`
- `dict`

---

#### list
- 一個序列
- 中括號為其精髓，包住所有元素們，以逗號隔開
- 每一個元素的 type <font class="Mark">不一定</font> 要一樣
```python
myList = ['string', 3, -0.87, ['List', 'in', 'the', 'List']]
print(myList)
```

---

#### list - Append
- `list.append(sth)`：將 `sth` 插入至最後面
```python
myList.append('💩' * 3)
print(myList)
```

---

#### list - len & get/set items
- `len(myList)`：取得 myList 的長度
- `print(myList[i])`：取得 myList 第 i 個元素
- `myList[i] = sth`：將 myList 第 i 個元素設成 sth

```python
print(len(myList))
print(myList[-1])
myList[2] = 'sth'
print(myList)
```

---

#### tuple
- 看似是用小括號包起來的 list
- 差別在 <font class="Mark">Immutable</font>（不可改變的）
- <font class="Mark">逗號</font> 才是精髓
- 也有加乘、len、get item（和 list 一樣）

```python
t1 = (1, 'two')
t2 = 3,'四',5        # `,` is the key
print(t1, type(t1), t2, type(t2))
t1[1] = -1      # Immutable
```

---

#### tuple - Useful Tips
- 若有多個變數要設可以一次用 tuple 設好！
- swap：交換兩個變數的內容

```python
x, y = 1, 3
print(x, y, (x, y))

x, y = y, x
print(x, y, (x, y))
```

---

#### dict

- 字典（<font class="Mark">dict</font>ionary）
- key -> value
- 可以用大括號宣告
```python
my = {'Face' : 'Ugly', 'Salary' : 1e10, 'Over18' : True, 'girlfriend': None}
```

---

#### dict - Insert & Modify
直接用中括號
```python
my[19] = [1, 9]
my['Face'] = 'Pretty Handsome'
```

---

#### dict - keys & items

- `d.keys()`：得到 d 的所有 key
- `d.items()`：得到一個 (key, value) 的類似 list 的結構
- 都可以用 list 包起來變成真的 list
```python
print(d.keys())
print(d.items())
```

---

#### 注意
```python
l, t, d = [], (), {}
print(l[3])
print(t[2])
print(d['wwwww'])
```

`IndexError`：要注意你的 index 有沒有超過 list/tuple 的 len
`KeyError`：要注意 key 有沒有在 dict 裡

---

#### Practice - 愛吃拉麵的ＯＯ同學
ＯＯ同學是個愛吃拉麵的資工系學生，然而在炎熱的夏日出門吃拉麵是件令人煩惱的事情，必須要考慮到可達性、價位、食慾、季節......<br>
然而可達性是最重要的一環，請問你能幫忙算出地圖上一些點對的方向（<font class="Mark">相對向量</font>），以方便他進行選擇嗎？

---

#### Practice - 愛吃拉麵的ＯＯ同學
假設：
- 台大為原點 `(0, 0)`
- 家為 `(-12.6, 21.3)`
- 心拉麵為 `(2.6, 4.9)`
- 麵屋一燈 `(-8.1, 10.3)`
- 五之神製麵所 `(6.7, 6.7)`
- 山嵐為 `(-0.4, -0.3)`

聲明：
- 我不是ＯＯ同學（？
- 為了保護ＯＯ同學，家的座標是他同學的家

---

#### Sample Code - 愛吃拉麵的ＯＯ同學
`ramenMap.py`
```python
ramenMap = {'NTU': (0, 0), 'Home': (-12.6, 21.3), 'Soba Shin': (2.6, 4.9), 'Itto': (-8.1, 10.3), 'GoNoKami': (6.7, 6.7), '山嵐': (-0.4, -0.3)}

f = input('From: ')
t = input('To: ')

# TODO
```
Hint
- `ramenMap` 是一個 <font class="Mark">dict</font>
- 每個地點使用 <font class="Mark">str</font> 代表，座標使用 <font class="Mark">2-tuple</font> 代表
- tuple 的減法（？

---

#### Solution - 愛吃拉麵的ＯＯ同學

To be continued...
