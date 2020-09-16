import unittest
import vehicle

class VehicleTests(unittest.TestCase):
    def test_vehicle(self):
      testVehicle = vehicle.Vehicle(4, 87, 4, 1)
      self.assertEqual(testVehicle.wheels, 4)
      self.assertEqual(testVehicle.fuel, 87)
      self.assertEqual(testVehicle.doors, 4)
      self.assertEqual(testVehicle.roof, 1)
    # Add code here.
    def test_vehicle2(self):
      testVehicle2 = vehicle.Vehicle(4, 91, 2, 0)
      self.assertEqual(testVehicle2.wheels, 4)
      self.assertEqual(testVehicle2.fuel, 91)
      self.assertEqual(testVehicle2.doors, 2)
      self.assertEqual(testVehicle2.roof, 0)



# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

