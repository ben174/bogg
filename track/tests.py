import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from track.models import Bogger

class BoggerTest(TestCase):
    def setUp(self):
        self.dude = User.objects.create(username='dude')
        self.bogger_dude = Bogger.objects.create(user=self.dude, gender='M')
        self.bogger_dude.height = (6 * 12) + 2    # 6'2"
        self.bogger_dude.weight = 180
        self.bogger_dude.birthdate = datetime.datetime.now() - datetime.timedelta(days=365.25*35)
        self.bogger_dude.activity_factor = 1.2
        self.bogger_dude.daily_weight_goal = (2. / 7.)

        self.chick = User.objects.create(username='chick')
        self.bogger_chick = Bogger.objects.create(user=self.chick, gender='F')
        self.bogger_chick.height = (5 * 12) + 3    # 5'3"
        self.bogger_chick.weight = 120
        self.bogger_chick.birthdate = datetime.datetime.now() - datetime.timedelta(days=365.25*28)
        self.bogger_chick.activity_factor = 1.9
        self.bogger_chick.daily_weight_goal = (1. / 7.)

    def test_age(self):
        self.assertEqual(self.bogger_dude.age, 35)
        self.assertEqual(self.bogger_chick.age, 28)

    def test_calc_male_bmr(self):
        self.assertEqual(self.bogger_dude.gender, 'M')
        self.assertEqual(self.bogger_dude.bmr, 1889.2)

    def test_calc_female_bmr(self):
        self.assertEqual(self.bogger_chick.gender, 'F')
        self.assertEqual(self.bogger_chick.bmr, 1341.5)

    def test_calc_hbe(self):
        self.assertEqual(self.bogger_dude.hbe, 2267)
        self.assertEqual(self.bogger_chick.hbe, 2548)

    def test_calorie_goal(self):
        self.assertEqual(self.bogger_dude.calorie_goal, 1267)
        self.assertEqual(self.bogger_chick.calorie_goal, 2048)
