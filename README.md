>## Elian Saúl Estrada Urbina
>### 201806838

# Code intermide generator of aritmethic expression
1. ### Input:
	```python=
	var1 + var2
	```
	### Output:
	```python=
	t1 = var1 + var2
	```
2. ### Input:
	```python=
	var1 + var2 - var3
	```
	### Output:
	```python=
	t1 = var1 + var2
	t2 = t1 - var3
	```
3. ### Input:
	```python=
	var1 * var2 + var3
	```
	### Output:
	```python=
	t1 = var1 * var2
	t2 = t1 + var3
	```
4. ### Input:
	```python=
	var1 + var2 * var3
	```
	### Output:
	```python=
	t1 = var2 * var3
	t2 = var1 + t1
	```
5. ### Input:
	```python=
	(var1 + var2) * var3
	```
	### Output:
	```python=
	t1 = var1 + var2
	t2 = t1 * var3
	```
6. ### Input:
	```python=
	((var1 - var2) / (var3 + var4 * var5)) * var6
	```
	### Output:
	```python=
	t1 = var1 - var2
	t2 = var4 * var5
	t3 = var3 + t2
	t4 = t1 / t3
	t5 = t4 * var6
	```
7. ### Input:
	```python=
	var1 - var2 * (var3 - var4 * var5 - (var6 + var7)) / var8
	```
	### Output:
	```python=
	t1 = var4 * var5
	t2 = var3 - t1
	t3 = var6 + var7
	t4 = t2 - t3
	t5 = var2 * t4
	t6 = t5 / var8
	t7 = var1 - t6
	```
8. ### Input:
	```python=
	var1 / var2 * var3 + (var4 + var5 * var6) + var7/(var8 * var9) - var10
	```
	### Output:
	```python=
	t1 = var1 / var2
	t2 = t1 * var3
	t3 = var5 * var6
	t4 = var4 + t3
	t5 = t2 + t4
	t6 = var8 * var9
	t7 = var7 / t6
	t8 = t5 + t7
	t9 = t8 - var10
	```
9. ### Input:
	```python=
	var1 * (var2 / (var3 + var4 / (var5 - var6 * var7) * var8) * var9) / var10
	```
	### Output:
	```python=
	t1 = var6 * var7
	t2 = var5 - t1
	t3 = var4 / t2
	t4 = t3 * var8
	t5 = var3 + t4
	t6 = var2 / t5
	t7 = t6 * var9
	t8 = var1 * t7
	t9 = t8 / var10
	```
10. ### Input:
	```python=
	(var1 - (var2 * var3 - var4 * var5 * var6) * (var7 / var8)) / (var9 * var10)
	```
	### Output:
	```python=
	t1 = var2 * var3
	t2 = var4 * var5
	t3 = t2 * var6
	t4 = t1 - t3
	t5 = var7 / var8
	t6 = t4 * t5
	t7 = var1 - t6
	t8 = var9 * var10
	t9 = t7 / t8
	```
11. ### Input:
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
12. ### Input:
	```python=
	var1 < var2 and var3 > var4
	```
	### Output:
	```python=
	if var1 < var2 goto L3
	goto L4
	L3:
	if var3 > var4 goto L5
	goto L6

	LV: L5
	LF: L4,L6
	```
