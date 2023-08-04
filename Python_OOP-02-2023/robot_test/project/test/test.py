from project.robot import Robot
import unittest


class RobotTests(unittest.TestCase):
    def setUp(self):
        self.robot = Robot("01", "Entertainment", 3, 5.0)
        self.robot2 = Robot("02", "Education", 2, 4.0)

    def test_category_1(self):
        self.robot.category = "Military"
        result = self.robot.category
        expected_result = "Military"
        self.assertEqual(result, expected_result)

    def test_category_2(self):
        try:
            self.robot.category = "Cat"
            result = self.robot.category
        except ValueError:
            result = "ValueError"
        expected_result = "ValueError"
        self.assertEqual(result, expected_result)

    def test_price_1(self):
        self.robot.price = 10.0
        result = self.robot.price
        expected_result = 10.0
        self.assertEqual(result, expected_result)

    def test_price_2(self):
        try:
            self.robot.price = -2
            result = self.robot.price
        except ValueError:
            result = "ValueError"
        expected_result = "ValueError"
        self.assertEqual(result, expected_result)

    def test_upgrade_1(self):
        result = self.robot.upgrade("Sensor", 2.0)
        expected_result = "Robot 01 was upgraded with Sensor."
        self.assertEqual(result, expected_result)

    def test_upgrade_2(self):
        self.robot.upgrade("Sensor", 2.0)
        result = self.robot.upgrade("Sensor", 2.0)
        expected_result = "Robot 01 was not upgraded."
        self.assertEqual(result, expected_result)

    def test_update_1(self):
        result = self.robot.update(2.0, 1)
        expected_result = "Robot 01 was updated to version 2.0."
        self.assertEqual(result, expected_result)

    def test_update_2(self):
        self.robot.update(2.0, 1)
        result = self.robot.update(1.5, 1)
        expected_result = "Robot 01 was not updated."
        self.assertEqual(result, expected_result)

    def test_gt(self):
        result = self.robot.__gt__(self.robot2)
        expected_result = "Robot with ID 01 is more expensive than Robot with ID 02."
        self.assertEqual(result, expected_result)
