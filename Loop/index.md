# Flow Control (ii) Loops

###### Wu-Jun Pei @ CSCamp 2019

--

## 前情提要

---

--

## While

---

#### While - 日常生活
<font class="Mark">當</font> Pizza 上有鳳梨，我就會把他挑掉。
- 夏威夷 Pizza 是邪教

---

#### While - Python

```python
while [condition]:
    # do something
```
- Recall：python 是用縮排作為程式碼區塊劃分依據
- 通常以 4 個空格作為縮排
- 冒號：提示接下來要縮排
- 其實就是把 `if` 改成 `while`
- condition 放跟 if 一樣的條件式

---

#### Example
```python
done = False
while not done:
    pick_up_some_pineapples()
    if remain_pineapples is 0:
        done = True
```

---

#### Practice - Adventure
- 輸入：Boss 血量、冒險者的攻擊力
- 輸出：需要幾回合 Boss 才會死

---

#### Practice - Adventure
Sample Code
```python
boss_HP = int(input('Boss HP: '))
our_Atk = int(input('Our Atk: '))
rounds = 0

# while loop

print(rounds)
```

---

#### Solution - Adventure
To be continued......

--

## For

---

#### Scenario

<img src="imgs/100-times-a.png">

Reference: [I'm Programmer, I Have No Life](https://www.facebook.com/ProgrammersCreateLife/posts/2306646209384244)

---

<img src="imgs/100-times-b.png">

---

<img src="imgs/100-times-c.png">

---

#### For
```python
for variable in iterable_object:
    # do something
```
- variable：變數
- iterable_object：可迭代物件
- 冒號：提示接下來要縮排

---

#### For
```python
for i in range(100):
    print("Sorry, Sweet Heart")

print(list(range(100)))
```
- `range(100)`：$0, 1, ..., 98, 99$

將 `i` 從 0 到 99 迭代過去

---

#### Iterable

- [Cambridge Dictionary - iterate](https://dictionary.cambridge.org/zht/詞典/英語-漢語-繁體/iterate)<br>to repeat a process, especially as part of a computer program，重複執行一段程式碼
- iterable object：可重複執行的物件，可以想成一堆有順序的東西

---

#### Iterable - range
一些數字，常用為計數器
- `range(n)`：從 $0, 1, ..., n - 1$
- `range(m, n)`：從 $m, m + 1, ..., n - 1$
- `range(m, n, k)`：從 $m, m + k, m + 2k, ...$ 直到超過範圍<br>（$k$ 可以是負數，$n - m$ 不一定要是 $k$ 的倍數）

```python
print(list(range(6)))
print(list(range(-10, 10)))
print(list(range(1, 13, 2)))
print(list(range(19, 2, -3)))
```

---

#### Iterable - str/list/tuple/dict
- 從 str 拿出每個字元
- 從 list/tuple 拿出每個 element
- 從 dict 拿出每個 key

```python
for c in "Python":
    print(c)

for p in [2, 3, 5, 7, 11, 13, 17, 19]:
    print(p, 'is a prime')

d = {'I' : 'My', 'You' : 'Your', 'We' : 'Our'}
for key in d:
    print(key, '->', d[key])
```

---

#### Practice - Sum of Power of 5 (i)
$$ \sum_{i = 1}^N i^5 $$

- 輸入：$N$
- 輸出：五次方和
- 懸賞：背得出公式解可以獲得神秘小禮物（in 30sec）

---

#### Practice - Sum of Power of 5 (i)
Sample Code
```python
N = int(input('Input N'))

total = 0

# For Loop

print(total)
```

---

#### Practice - Sum of Power of 5 (ii)

- 輸入：$N$ 個數字
- 輸出：五次方和

---

#### Practice - Sum of Power of 5 (ii)
Sample Code
```python
# White Magic
numbers = list(int(x) for x in input(' ').split(' '))

total = 0

# For Loop

print(total)
```

---

#### Solution - Sum of Power of 5 (i) & (ii)
To be continued...

---

#### Useful Tips

- for 寫在一行之中
- 常用於各種轉型（正義）、基本轉換之中

```python
# list of int
inputSequence = input('Input some hex numbers: ').split(' ')

# list of int
intSequence = [int(x, 16) for x in inputSequence]

# convert to negative
negSequence = [-x for x in intSequence]

print(negSequence)
```

---

#### Useful Tips

- In one line
- 常常走火入魔
- （但我喜歡

```python
outputSequence = [-int(x, 16) for x in input('Input some hex numbers: ').split(' ')]
print(negSequence)
```

--

## continue & break

---

#### continue
- 直接進到下個 iteration

```python
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print((i // 3) / (i % 3))
```

---

#### break
- 終結這個迴圈

```python
ans = 7.315
for i in range(1024):
    print('Round', i)
    if i < ans and ans < i + 1:
        print('ans is between', i, 'and', i + 1)
        break
```
