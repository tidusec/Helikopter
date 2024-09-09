# tests
import unittest
from main import Helicopter

class MyTestCase(unittest.TestCase):
    def test_init_valid_arguments(self):
        heli = Helicopter([0, 0, 0], "noord")
        self.assertEqual(heli.location, [0, 0, 0])
        self.assertEqual(heli.direction, 0)

    def test_init_invalid_begin_position(self):
        with self.assertRaises(ValueError):
            Helicopter([0, 0], "noord")
        with self.assertRaises(ValueError):
            Helicopter([0, 0, "invalid"], "noord")

    def test_init_invalid_direction(self):
        with self.assertRaises(ValueError):
            Helicopter([0, 0, 0], "invalid")

    def test_move_up(self):
        heli = Helicopter([0, 0, 0], "noord")
        heli.move_up()
        self.assertEqual(heli.location, [0, 0, 1])

    def test_move_down(self):
        heli = Helicopter([0, 0, 5], "noord")
        heli.move_down()
        self.assertEqual(heli.location, [0, 0, 4])

    def test_turn_left(self):
        heli = Helicopter([0, 0, 0], "noord")
        heli.turn_left()
        self.assertEqual(heli.direction, 3)
        self.assertEqual(heli.directions[heli.direction], "west")

    def test_turn_right(self):
        heli = Helicopter([0, 0, 0], "noord")
        heli.turn_right()
        self.assertEqual(heli.direction, 1)
        self.assertEqual(heli.directions[heli.direction], "oost")

    def test_move_forward(self):
        heli = Helicopter([0, 0, 0], "noord")
        heli.move_forward()
        self.assertEqual(heli.location, [0, 1, 0])

        heli = Helicopter([0, 0, 0], "oost")
        heli.move_forward()
        self.assertEqual(heli.location, [1, 0, 0])

        heli = Helicopter([0, 0, 0], "zuid")
        heli.move_forward()
        self.assertEqual(heli.location, [0, -1, 0])

        heli = Helicopter([0, 0, 0], "west")
        heli.move_forward()
        self.assertEqual(heli.location, [-1, 0, 0])

    def test_execute_instructions(self):
        heli = Helicopter([0, 0, 0], "noord")
        final_location, final_direction = heli.execute_instructions("UURVVVLVVRRVD")
        self.assertEqual(final_location, [3, 1, 1])
        self.assertEqual(final_direction, "zuid")

if __name__ == '__main__':
    unittest.main()