import Head
import Torso
import Arm
import Hand
import Leg
import Feet

head = Head()
right_hand = Hand()
right_arm = Arm(right_hand)
right_feet = Feet()
right_leg = Leg(right_feet)

left_hand = Hand()
left_arm = Arm(left_hand)
left_feet = Feet()
left_leg = Leg(left_feet)

torso = Torso(head, right_arm, right_leg, left_arm, left_feet)