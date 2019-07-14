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
- 括號內可以放任意型態的東西，用逗號隔開

---

#### Output - Example

```python
print(12345, 3.1415, "Hello")
```
- 會用空白幫你分開每個東西，最後會印一個換行

---

#### Output - Additional Parameters
- 他們是函示 (function) 的一些參數
- `sep`：分開每個元素的字串，預設是空格 `' '`
- `end`：結尾字串，預設是換行符號 `'\n'`
- Example
```python
print(0, 1.1, 'www', -33333 , sep = ' | ', end='\nOwO\n')
```

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
a+b
a-b
a*b
a/b
```
- 這裡的除是會一般的除法
- 先乘除後加減
- 小括號有一樣的功用

---

#### 後三則運算
```python
a // b
a % b
a ** b
```
- `//`：取商
- `%`：取餘數
- `**`：取次方，$a^b$

---

#### Practice - 一元二次方程式

題目敘述
- 有兩相異實數解之一元二次方程式
$$ax^2 + bx + c$$
- 假設 $a = 1, b = -5, c = 4$，請由小到大輸出兩個解

Hint
- 開根號就是**乘乘** $0.5$ 喔！
- 公式解
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

---

#### Practice - 一元二次方程式

Sample Code
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
To Be Continued...

<!--
```python
a = 1
b = -5
c = 4

x1 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print("x1 =", x1)
print("x2 =", x2)
```
-->

---

#### Bool

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
s = 'pei'
```

---

#### str - 加乘
- 加法：把兩個字串串在一起
- 乘法：複製自己好多次
```python
s2 = s + s
s8 = s * 8
print(s2, s8)
```

---

#### str - len & item
- `len(s)`：得到 `s` 的長度
- `s[i]`（get item）：得到由 s 的第 i 個字元組成的字串（從零開始數）
- 若 `i` 是 <font class="Mark">-k</font>，則代表取倒數第 <font class="Mark">k</font> 個字元
```python
s = 'abcdefghijklmnopqrstuvwxyz'
#    0123456789
#              0123456789
#                        012345
print(s[3], type(s[3]), s[-1])
```

---

#### str - Slice
- `s[i : j]`：取第 i 開始到第 j 的子字串
- i、j 使用負數有一樣的效果，放空則代表從最前面開始 / 到最底
- `s[i : j : k]`：從 i 開始取道第 j，每 k 個取一次，若是負號則代表倒著取
```python
s[:5]
s[-3:]
s[4:-4]
s[::2]
s[::-1]
s[-4:4:-2]
```

---

#### str - Immutable
想要把 s 變成 abbdef...

```python
s[2] = 'b'
```

- str 是 <font class="Mark">Immutable</font>（不可改變的）
- How to change?
	1. 使用 字串加法＆Slice
		```python
		s = s[:2] + 'b' + s[3:]
		```
	2. 可以使用等等介紹的 list

---

#### None

---

#### type
可以使用 `type(variable)` 查看一個變數的型態，e.g.
- `type(33)`
- `type('wwwww')`
- `type(11 / 3)`
- `type(11 // 3)`
- `type(int)`
- `type(print)`

---

#### 型態轉換
直接用新的型態將原本的變數用小括號包起來，e.g.
- `str_a` 是一個字串 `'33'`，把他轉換成 `int` 並存在 `int_a` 之中
```python
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

#### list - 加乘 & slice
```python
l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]
print(l2[::-1])
print((2 * l1[1::-1] + l2)[::-1] + l2)
```

---

#### tuple
- 看似是用小括號包起來的 list
- 差別在 <font class="Mark">Immutable</font>（不可改變的）
- <font class="Mark">逗號</font> 才是精髓
- 也有加乘、len、get item、slice

```python
t1 = (1, 'two')
t2 = 3,'四',5		# `,` is the key
print(t1, type(t1), t2, type(t2))
t1[1] = -1		# Immutable
```

---

#### tuple - 加乘 & len & slice
- tuple 也有 len, slice，用法同 str
```python
print(len(t1))
print(t2[::-1])
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
d = {1.2345 : 77777, '我愛 how 哥' : 'how 哥 No.1'}
```

---

#### dict - Insert
直接用中括號
```python
d[4129889] = 'pizza hut hut 到家'
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



