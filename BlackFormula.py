import scipy.stats
from scipy.stats import norm
import numpy as np

import math  # Calculation choice

class Option():
    def __init__(self, option, spotPrice, strikePrice, timeDays, rate, dividendYeld, volatility=4, daysYear=360):
        self.option = option
        self.spotP = float(spotPrice)
        self.strikeP = float(strikePrice)
        self.time = float(timeDays)
        self.rate = float(rate)
        self.div = float(dividendYeld)
        self.vol = float(volatility)
        self.daysYear=daysYear
        self.factors()

    def factors(self):
        self.d1 = float(math.log(self.spotP / self.strikeP) + (self.rate - self.div + ((self.vol ** 2.0) / 2.0)) * (
            self.time / self.daysYear)) / (((self.time / self.daysYear) ** (1.0 / 2.0)) * self.vol)
        self.d2 = float(self.d1 - ((self.time / self.daysYear) ** (1.0 / 2.0)) * self.vol)

    def calculatePrice(self):
        if self.option == 'call':
            price = float(
                ((scipy.stats.norm(0, 1).cdf(self.d1)) * (
                    self.spotP * math.exp((-self.div) * (self.time / self.daysYear)))) - (
                    scipy.stats.norm(0, 1).cdf(self.d2)) * self.strikeP * math.exp(
                    (-self.rate) * (self.time / self.daysYear)))
            # print(float(round(price, 3)))
        else:  # it's put
            price = float(
                ((1 - (scipy.stats.norm(0, 1).cdf(self.d1))) * (
                    -self.spotP * math.exp((-self.div) * (self.time / self.daysYear)))) + (
                    1 - (scipy.stats.norm(0, 1).cdf(self.d2))) * self.strikeP * (
                    math.exp((-self.rate) * (self.time / self.daysYear))))
            # print(float(round(price, 3)))
        return float(round(price, 3))

    def vega(self):
        v = self.spotP * norm.pdf(self.d1) * np.sqrt(self.time / self.daysYear)
        return v

    def imp_vol(self, price):
        for i in range(256):
            option = Option(option=self.option, spotPrice=self.spotP, strikePrice=self.strikeP, timeDays=self.time,
                            rate=self.rate, dividendYeld=self.div, volatility=self.vol)

            self.vol -= (option.calculatePrice() - price) / self.vega()
            self.factors()
        return float(round(self.vol*100, 4))


# put = Option(option='put', spotPrice=1314.49, strikePrice=1314.49, timeDays=180, rate=0.78525 / 100.0,
#              dividendYeld=2.211 / 100.0, volatility=20.252 / 100.0)
# put.calculatePrice()
#
# call = Option(option='call', spotPrice=1314.25, strikePrice=1314.25, timeDays=30, rate=0.261 / 100.0,
#              dividendYeld=2.886 / 100.0, volatility=16.252 / 100.0)
# call.calculatePrice()
#
# vol  = Option(option='call', spotPrice=1314.25, strikePrice=1314.25, timeDays=30, rate=0.261 / 100.0,
#              dividendYeld=2.886 / 100.0, volatility=200 / 100.0)
# vol.imp_vol(23.47)
