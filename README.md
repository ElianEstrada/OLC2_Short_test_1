>## Elian Saúl Estrada Urbina
>### 201806838

# Code intermide generator of aritmethic expression
1. ### Input:
	```python=
	var1 > var2
	```
	### Output:
	```python=
	if var1 > var2 goto L1
	goto L2

	LV: L1
	LF: L2
	```
2. ### Input:
	```python=
	var1 < var2 and var3 > var4
	```
	### Output:
	```python=
	if var1 < var2 goto L1
	goto L2
	L1:
	if var3 > var4 goto L3
	goto L4

	LV: L3
	LF: L2,L4
	```
3. ### Input:
	```python=
	var1 > var2 and var3 < var4 or var5 > var6
	```
	### Output:
	```python=
	if var1 > var2 goto L1
	goto L2
	L1:
	if var3 < var4 goto L3
	goto L4
	L2,L4:
	if var5 > var6 goto L5
	goto L6

	LV: L3,L5
	LF: L6
	```
4. ### Input:
	```python=
	var1 > var2 and not var3 > var4
	```
	### Output:
	```python=
	if var1 > var2 goto L1
	goto L2
	L1:
	if var3 > var4 goto L3
	goto L4

	LV: L4
	LF: L2,L3
	```
5. ### Input:
	```python=
	var1 > var2 or var3 < var4 and not var5 == var6
	```
	### Output:
	```python=
	if var1 > var2 goto L1
	goto L2
	L2:
	if var3 < var4 goto L3
	goto L4
	L3:
	if var5 == var6 goto L5
	goto L6

	LV: L1,L6
	LF: L4,L5
	```
6. ### Input:
	```python=
	(n1 + n2) * n3 < n4 + n5 and (n6 + n7) < n8
	```
	### Output:
	```python=
	t1 = n1 + n2
	t2 = t1 * n3
	t3 = n4 + n5
	if t2 < t3 goto L1
	goto L2
	L1:
	t4 = n6 + n7
	if t4 < n8 goto L3
	goto L4

	LV: L3
	LF: L2,L4
	```
7. ### Input:
	```python=
	var1 + var2 > (var3 + var4 - var5) * var6
	```
	### Output:
	```python=
	t1 = var1 + var2
	t2 = var3 + var4
	t3 = t2 - var5
	t4 = t3 * var6
	if t1 > t4 goto L1
	goto L2

	LV: L1
	LF: L2
	```
8. ### Input:
	```python=
	var1 * var2 > var3 + var4 and var5 + var6 != var7 * var8
	```
	### Output:
	```python=
	t1 = var1 * var2
	t2 = var3 + var4
	if t1 > t2 goto L1
	goto L2
	L1:
	t3 = var5 + var6
	t4 = var7 * var8
	if t3 != t4 goto L3
	goto L4

	LV: L3
	LF: L2,L4
	```
9. ### Input:
	```python=
	(var1 + var2) * var3 > ((var4 - var5) / (var6 + var7 * var8)) or var9 * var10 > var11
	```
	### Output:
	```python=
	t1 = var1 + var2
	t2 = t1 * var3
	t3 = var4 - var5
	t4 = var7 * var8
	t5 = var6 + t4
	t6 = t3 / t5
	if t2 > t6 goto L1
	goto L2
	L2:
	t7 = var9 * var10
	if t7 > var11 goto L3
	goto L4

	LV: L1,L3
	LF: L4
	```
10. ### Input:
	```python=
	var1 > var2 and var3 <= var4 or not var5 > var6 and var7 < var8
	```
	### Output:
	```python=
	if var1 > var2 goto L1
	goto L2
	L1:
	if var3 <= var4 goto L3
	goto L4
	L2,L4:
	if var5 > var6 goto L5
	goto L6
	L6:
	if var7 < var8 goto L7
	goto L8

	LV: L3,L7
	LF: L5,L8
	```
11. ### Input:
	```python=
	var1 < var2 and (var3 > var4 or not (var5 < var6 or var7 == var8)) or var9 != var10
	```
	### Output:
	```python=
	if var1 < var2 goto L1
	goto L2
	L1:
	if var3 > var4 goto L3
	goto L4
	L4:
	if var5 < var6 goto L5
	goto L6
	L6:
	if var7 == var8 goto L7
	goto L8
	L2,L5,L7:
	if var9 != var10 goto L9
	goto L10

	LV: L3,L8,L9
	LF: L10
	```
12. ### Input:
	```python=
	not not var1 > var2
	```
	### Output:
	```python=
	if var1 > var2 goto L1
	goto L2

	LV: L1
	LF: L2
	```
