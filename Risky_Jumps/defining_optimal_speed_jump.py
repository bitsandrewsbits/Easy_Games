# defining optimal value of start speed for ball jumping
# for height of jump = 60

def get_acceleration_v0_steps_for_S_and_FPS_up_jump(fps = 40):
	h = 60
	k_fps = h / fps
	v0 = 2.2 * k_fps       # start speed (on bottom) - px/sec
	test_v0 = 2.2 * k_fps
	v = 0  # end speed (on top)
	acceleration = -(v0 / fps)   # as a = -(v0 / FPS) [px * (t_1frame)^2]
	amount_of_iterations = 0
	S_result = 0
	# while round(S_result, 1) != S and v0 != 0:
	for _ in range(1000):
		# print('=' * 40)
		# print(f'Test for v0 = {v0}, acceleration = {acceleration}')
		for i in range(1, fps + 1):
			v0 += acceleration * 1
			S_result += v0 * 1
			# print('S(passed) =', S_result)
			# print('v0 =', v0)
			# print('iteration # =', amount_of_iterations)
			amount_of_iterations += 1
			if round(S_result, 1) >= h and round(v0) <= 0:
				break

		if round(v0) <= 0 and round(S_result, 1) >= h:
			return [round(test_v0, 1), round(acceleration, 3), amount_of_iterations, S_result]
		else:
			test_v0 += 0.005
			v0 = test_v0
			acceleration = (v0 / fps)
			amount_of_iterations = 0
			S_result = 0

def get_new_acceleration_for_new_FPS_down_jump(fps = 40):
	h = 60
	if fps >= h:
		k_fps = fps / h
	else:
		k_fps = h / fps
	# fps_t = 1 / fps  # part of second for 1 frame 
	v0 = 0  # start speed (on top) - px/sec
	acceleration = (10 / fps) * k_fps    # as g = 10 / FPS
	return [acceleration, 0, 0]
	# amount_of_iterations = 0
	# S_result = 0
	# for _ in range(1000):
	# 	# print('=' * 40)
	# 	# print(f'Test for v0 = {v0}, acceleration = {acceleration}')
	# 	for i in range(1, fps + 1):
	# 		v0 += acceleration
	# 		S_result += v0 * fps_t
	# 		amount_of_iterations += 1
	# 		if round(S_result, 1) >= S:
	# 			break

	# 	if round(S_result, 1) >= S:
	# 		return [round(acceleration / fps, 3), amount_of_iterations, S_result]
	# 	else:
	# 		# acceleration += 0.005
	# 		v0 = 0
	# 		amount_of_iterations = 0
	# 		S_result = 0	

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
	testing_for_different_FPS_up_jump(30, 300)
	# testing_for_different_FPS_down_jump(30, 300)