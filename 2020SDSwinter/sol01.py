def rotationRight(face) :
	temp = face.copy()
	face[0:3] = [temp[6], temp[3], temp[0]]
	face[3:6] = [temp[7], temp[4], temp[1]]
	face[6:9] = [temp[8], temp[5], temp[2]]

def rotationLeft(face) :
	temp = face.copy()
	face[0:3] = [temp[2], temp[5], temp[8]]
	face[3:6] = [temp[1], temp[4], temp[7]]
	face[6:9] = [temp[0], temp[3], temp[6]]

def rotationOfB(M, rc, P):
	box = [[1, 2, 3, 4, 5, 6, 7, 8, 9], # A 0
		   [10, 11, 12, 13, 14, 15, 16, 17, 18], # B 1
		   [19, 20, 21, 22, 23, 24, 25, 26, 27], # C 2
		   [28, 29, 30, 31, 32, 33, 34, 35, 36], # D 3
		   [37, 38, 39, 40, 41, 42, 43, 44, 45], # E 4
		   [46, 47, 48, 49, 50, 51, 52, 53, 54]] # F 5

	# rotation
	for i in range(0, M):
		code = rc[i]
		temp = box[1].copy()
		if code >= 1 and code <= 3 :
			print('n1-3')
			code -= 1
			for c in range(0,3):
				box[1][code + (3 * c)] = box[2][code + (3 * c)]
				box[2][code + (3 * c)] = box[3][(code+2) + (3 * c)]
				box[3][code + (3 * c)] = box[0][code + (3 * c)]
				box[0][code + (3 * c)] = temp[code + (3 * c)]
		elif code >= 4 and code <= 6 :
			print('n4-6')
			code -= 4
			for c in range(0, 3):
				box[1][code + (3 * c)] = box[0][code + (3 * c)]
				box[0][code + (3 * c)] = box[3][code + (3 * c)]
				box[3][code + (3 * c)] = box[2][code + (3 * c)]
				box[2][code + (3 * c)] = temp[code + (3 * c)]
		elif code >= 7 and code <= 9:
			print('n7-9')
			code -= 7
			for c in range(0,3):
				box[1][code + c] = box[5][code + c]
				box[5][code + c] = box[3][code + c]
				box[3][code + c] = box[4][code + c]
				box[4][code + c] = temp[code + c]
		else :
			print('n10-12')
			code -= 10
			for c in range(0, 3):
				box[1][code + c] = box[4][code + c]
				box[4][code + c] = box[3][code + c]
				box[3][code + c] = box[5][code + c]
				box[5][code + c] = temp[code + c]

		# 측면 회전 시 면도 같이 회전
		if rc[i] == 3 or rc[i] == 4 or rc[i] == 7 or rc[i] == 12 :
			if rc[i] == 3 :
				rotationRight(box[5])
			elif rc[i] == 4 :
				rotationRight(box[4])
			elif rc[i] == 7 :
				rotationRight(box[0])
			else :
				rotationRight(box[2])
		elif rc[i] == 1 or rc[i] == 6 or rc[i] == 9 or rc[i] == 10 :
			if rc[i] == 1:
				rotationLeft(box[4])
			elif rc[i] == 6:
				rotationLeft(box[5])
			elif rc[i] == 9:
				rotationLeft(box[2])
			else:
				rotationLeft(box[0])
		else : print('pass')

	return ' '.join(list(map(str, box[P-1])))
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

