#!/usr/bin/env python3

"""
Test Synchronizer to make sure it works properly in all combinations:
* Synchronous robot using with syntax
* Synchronous robot using try finally syntax
* Asynchronous robot using with syntax
* Asynchronous robot using try finally syntax
* Lastly disconnecting and reconnecting with the same robot
"""

import time

from anki_vector.events import Events  # pylint: disable=wrong-import-position
import anki_vector  # pylint: disable=wrong-import-position


def main():
    args = anki_vector.util.parse_command_args()

    print("------ begin testing sync ------")

    def test_subscriber(event_type, event):
        """test that subscriptions work"""
        print(f"Subscriber called for: {event_type} = {event}")

    print("------ Synchronous Robot using with ------")
    with anki_vector.Robot(args.serial) as robot:
        robot.events.subscribe(test_subscriber, Events.robot_state)
        robot.anim.play_animation("anim_blackjack_victorwin_01")

    print("------ Synchronous Robot using with ------")
    with anki_vector.Robot(args.serial) as robot:
        robot.events.subscribe_by_name(test_subscriber, event_name='test1')
        robot.anim.play_animation("anim_blackjack_victorwin_01")
        robot.events.unsubscribe_by_name(test_subscriber, event_name='test1')
        robot.events.unsubscribe_by_name(test_subscriber, event_name='test1')
        robot.motors.set_wheel_motors(100.0, -100.0)

    time.sleep(2)

    print("------ Synchronous Robot using try finally ------")
    robot = anki_vector.Robot(args.serial)
    robot.events.subscribe_by_name(test_subscriber, event_name='test1')
    try:
        robot.connect()
        robot.anim.play_animation("anim_blackjack_victorwin_01")
        robot.motors.set_wheel_motors(-100.0, 100.0)
    finally:
        robot.disconnect()

    time.sleep(2)

    print("------ Asynchronous Robot using with ------")
    with anki_vector.AsyncRobot(args.serial) as robot:
        robot.events.subscribe(test_subscriber, Events.robot_state)
        robot.anim.play_animation("anim_blackjack_victorwin_01").result()
        robot.motors.set_wheel_motors(-100.0, 100.0).result()

    time.sleep(2)

    print("------ Asynchronous Robot using try finally ------")
    robot = anki_vector.AsyncRobot(args.serial)
    robot.events.subscribe(test_subscriber, Events.robot_state)
    try:
        robot.connect()
        robot.anim.play_animation("anim_blackjack_victorwin_01").result()
        robot.motors.set_wheel_motors(100.0, -100.0).result()
    finally:
        robot.disconnect()

    time.sleep(2)

    print("------ Repeated Robot using try finally ------")
    # Reuse the same robot from a previous connection
    try:
        robot.connect()
        robot.anim.play_animation("anim_blackjack_victorwin_01").result()
        robot.motors.set_wheel_motors(0.0, 0.0).result()
    finally:
        robot.disconnect()

    print("------ finish testing sync ------")


if __name__ == "__main__":
    main()
