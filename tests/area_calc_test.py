import unittest
from unittest.mock import patch

from area_calc import Circle, ShapeFactory, Triangle


class ShapeFactoryTest(unittest.TestCase):
    @patch("area_calc.area_calc.Circle", spec=Circle)
    @patch("area_calc.area_calc.Triangle", spec=Triangle)
    def test_shape_factory_creates_correct_shapes(self, mock_triangle, mock_circle):  # noqa: E501
        # Создаем экземпляры с помощью ShapeFactory
        circle = ShapeFactory(5)
        triangle = ShapeFactory(3, 4, 5)

        # Проверяем, что были вызваны конструкторы Circle и Triangle с правильными аргументами # noqa: E501
        mock_circle.assert_called_once_with(5)
        mock_triangle.assert_called_once_with(3, 4, 5)

        # Проверяем, что возвращенные объекты являются экземплярами Circle и Triangle соответственно # noqa: E501
        self.assertIsInstance(circle, Circle)
        self.assertIsInstance(triangle, Triangle)


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_right_angled_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())


if __name__ == "__main__":
    unittest.main()
