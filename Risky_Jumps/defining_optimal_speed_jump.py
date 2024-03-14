# defining optimal value of start speed for ball jumping
# for height of jump = 60

def defining_acceleration_v0_steps_for_S_and_FPS(fps = 40):
	S = 60
	fps_t = 1 / fps  # second
	v0 = 1  # start speed (on bottom) - 1px/frame
	v = ''  # end speed (on top)
	acceleration = -0.01   # need to find
	amount_of_iterations = 0
	S_result = 0
	while round(S_result, 1) != S and v != 0:
		# print('=' * 40)
		# print(f'Test for v0 = {v0}, acceleration = {acceleration}')
		for i in range(1, fps + 1):
			v = v0 + acceleration
			S_result += v * fps_t
			# print('S(passed) =', S_result)
			amount_of_iterations += 1

		if round(S_result, 1) >= S and v >= 0:
			print('v in top =', v)
			return [v0, acceleration, amount_of_iterations, S_result]
		else:
			acceleration -= 0.01
			v0 += 0.02
			amount_of_iterations = 0

def testing_for_different_FPS():
	for fps in range(30, 100, 10):
		result = defining_acceleration_v0_steps_for_S_and_FPS(fps)
		print('\nDefining parameters for FPS =', fps)
		print('v0 =', result[0])
		print('acceleration =', result[1])
		print('amount_of_iterations =', result[2])
		print('S(passed) =', result[3])
		print('-' * 40)


if __name__ == '__main__':
	testing_for_different_FPS()