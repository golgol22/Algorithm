# 진법

#### 진법 변환 함수

```
# 2진법 변환 
bin(10) # 0b1010

# 8진법 변환
oct(95) # 0O137

# 16진법 변환 0~9 + A~F
hex(350) #0x15e

# n진법 -> 10진법
int()
```



# 비트 연산

: 한개 혹은 두개의 이진수에 적용되는 연산



#### 연산자 종류 

& and : 둘다 1일 경우 1, 아니면 0 반환

| or : 둘 중 하나가 1일 경우 1, 아니면 0을 반환

^ xor : 다르면 1, 같으면 0 반환

~ not : 1은 0으로, 0은 1로 반환

<<, >>  shift : bin(0b11 << 3) 0b11000



#### 2진수의 음수

0b0011 -> 3

0b0010 -> 2

0b0001 -> 1

0b0000 -> 0

0b1111 -> -1 

0b1110 -> -2
