from gadgets.motors.step_motor import Model_28BYJ_48
st_mot = Model_28BYJ_48([11,15,16,18])

for i in range(2):
 st_mot.angular_step(60,direction=2,waiting_time=2,bi_direction=True) 
