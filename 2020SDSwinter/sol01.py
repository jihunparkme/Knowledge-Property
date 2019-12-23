def rotationRight() :
def rotationLeft() :

def rotationOfB(M, rc, P):
	box = ['A', 'B', 'C', 'D', 'E', 'F']
	A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	B = [10, 11, 12, 13, 14, 15, 16, 17, 18]
	C = [19, 20, 21, 22, 23, 24, 25, 26, 27]
	D = [28, 29, 30, 31, 32, 33, 34, 35, 36]
	E = [37, 38, 39, 40, 41, 42, 43, 44, 45]
	F = [46, 47, 48, 49, 50, 51, 52, 53, 54]

	# rotation
	for i in range(0, M):
		code = rc[i]
		temp = B
		if code >= 1 and code <= 3 :
			code -= code
			for c in range(0,3):
				B[code + (3 * c)] = C[code + (3 * c)]
				C[code + (3 * c)] = D[code + (3 * c)]
				D[code + (3 * c)] = A[code + (3 * c)]
				A[code + (3 * c)] = temp[code + (3 * c)]
		elif code >= 4 and code <= 6 :
			code -= code
			for c in range(0, 3):
				B[code + (3 * c)] = A[code + (3 * c)]
				A[code + (3 * c)] = D[code + (3 * c)]
				D[code + (3 * c)] = C[code + (3 * c)]
				C[code + (3 * c)] = temp[code + (3 * c)]
		elif code >= 7 and code <= 9:
			code -= code
			for c in range(0,3):
				B[code + c] = F[code + c]
				F[code + c] = D[code + c]
				D[code + c] = E[code + c]
				E[code + c] = temp[code + c]
		else :
			code -= code
			for c in range(0, 3):
				B[code + c] = E[code + c]
				E[code + c] = D[code + c]
				D[code + c] = F[code + c]
				F[code + c] = temp[code + c]

	# 측면 회전 시 면도 같이 회전
	if rc[i] == 3 or rc[i] == 4 or rc[i] == 7 or rc[i] == 12 :
		if rc[i] == 3 :
			obj = F
			F = rotationRight(obj)
		elif rc[i] == 4 :
			obj = E
			E = rotationRight(obj)
		elif rc[i] == 7 :
			obj = A
			A = rotationRight(obj)
		else :
			obj = C
			C = rotationRight(obj)
	else :
		rotationLeft()

	return ' '.join(list(map(str, B)))
	# rst = ' '.join(list(map(str, B)))

if __name__ == "__main__":
	T = int(input())	# test case
	for t in range(0, T):
		commmand = list(map(int, input().split()))
		M = commmand[0]		# number of rotation code
		rc = commmand[1:M+1]	# rotation command code
		P = commmand[-1]	# output face
		rst = rotationOfB(M, rc, P)
		print('#'+str(t+1),rst)

box = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
	[10, 11, 12, 13, 14, 15, 16, 17, 18],
	[19, 20, 21, 22, 23, 24, 25, 26, 27],
	[28, 29, 30, 31, 32, 33, 34, 35, 36],
 	[37, 38, 39, 40, 41, 42, 43, 44, 45],
	[46, 47, 48, 49, 50, 51, 52, 53, 54]]