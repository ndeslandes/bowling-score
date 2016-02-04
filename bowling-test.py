import unittest, bowling

class Test(unittest.TestCase):

  def test_process_turn_oneTurn(self):
    self.assertEqual((3,''), bowling.process_turn("12"))

  def test_process_turn_oneTurn_noHit(self):
    self.assertEqual((0,''), bowling.process_turn("--"))
    
  def test_process_turn_twoTurn(self):
    self.assertEqual((3,'34'), bowling.process_turn("1234")) 

  def test_process_turn_twoTurn_withSpare_(self):
    self.assertEqual((13,'34'), bowling.process_turn("1/34"))

  def test_process_turn_twoTurn_withStrike(self):
    self.assertEqual((13,'12'), bowling.process_turn("X12"))

  def test_process_turn_twoTurn_withStrikeThenSpare(self):
    self.assertEqual((20,'1/'), bowling.process_turn("X1/"))

  def test_process_turn_threeTurn_withTwoStrikes(self):
    self.assertEqual((22,'X23'), bowling.process_turn("XX23"))
    
  def test_process_turn_fourTurn_withFourStrikes(self):
    self.assertEqual((30,'XXX'), bowling.process_turn("XXXX"))

  def test_process_game(self):
    self.assertEqual(90, bowling.process_game("--112233445566778899"))

  def test_process_game_allStrikes(self):
    self.assertEqual(300, bowling.process_game("XXXXXXXXXXXX"))

  def test_process_game_allSpares(self):
    self.assertEqual(145, bowling.process_game("-/1/2/3/4/5/6/7/8/9/-"))

if __name__ == "__main__":
    unittest.main()