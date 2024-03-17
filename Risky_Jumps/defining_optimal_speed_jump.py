# defining optimal value of start speed for ball jumping
# for height of jump = 60

def get_acceleration_v0_steps_for_S_and_FPS_up_jump(fps = 40):
	S = 60
	fps_t = 1 / fps  # second
	v0 = 10  # start speed (on bottom) - px/sec
	test_v0 = 10
	v = 0  # end speed (on top)
	acceleration = -0.05   # need to find
	amount_of_iterations = 0
	S_result = 0
	# while round(S_result, 1) != S and v0 != 0:
	for _ in range(1000):
		# print('=' * 40)
		# print(f'Test for v0 = {v0}, acceleration = {acceleration}')
		for i in range(1, fps + 1):
			v0 += acceleration
			S_result += v0 * fps_t
			# print('S(passed) =', S_result)
			# print('v0 =', v0)
			# print('iteration # =', amount_of_iterations)
			amount_of_iterations += 1
			if round(S_result, 1) >= S:
				break

		if round(S_result, 1) >= S:
			return [round(test_v0 / fps, 1), round(acceleration / fps, 3), amount_of_iterations, S_result]
		else:
			acceleration -= 0.05
			test_v0 += 1.5
			v0 = test_v0
			amount_of_iterations = 0
			S_result = 0

def get_acceleration_steps_for_S_and_FPS_down_jump(fps = 40):
	S = 60
	fps_t = 1 / fps  # second
	v0 = 0  # start speed (on top) - px/sec
	acceleration = 0.1   # need to find
	amount_of_iterations = 0
	S_result = 0
	for _ in range(1000):
		# print('=' * 40)
		# print(f'Test for v0 = {v0}, acceleration = {acceleration}')
		for i in range(1, fps + 1):
			v0 += acceleration
			S_result += v0 * fps_t
			amount_of_iterations += 1
			if round(S_result, 1) >= S:
				break

		if round(S_result, 1) >= S:
			return [round(acceleration / fps, 3), amount_of_iterations, S_result]
		else:
			acceleration += 0.1
			v0 = 0
			amount_of_iterations = 0
			S_result = 0	

def testing_for_different_FPS_up_jump(first_FPS = 30, last_FPS = 100):
	for fps in range(first_FPS, last_FPS, 10):
		result = get_acceleration_v0_steps_for_S_and_FPS_up_jump(fps)
		print('\nDefining parameters for FPS =', fps)
		print('v0 =', result[0])
		print('acceleration =', result[1])
		print('amount_of_iterations =', result[2])
		print('S(passed) =', result[3])
		print('-' * 40)

def testing_for_different_FPS_down_jump(first_FPS = 30, last_FPS = 100):
	for fps in range(first_FPS, last_FPS, 10):
		result = get_acceleration_steps_for_S_and_FPS_down_jump(fps)
		print('\nDefining parameters for FPS =', fps)
		print('acceleration =', result[0])
		print('amount_of_iterations =', result[1])
		print('S(passed) =', result[2])
		print('-' * 40)

if __name__ == '__main__':
	# testing_for_different_FPS_up_jump(30, 100)
	testing_for_different_FPS_down_jump(30, 100)