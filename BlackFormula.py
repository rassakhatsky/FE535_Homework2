import math  # Calculation choice
import numpy as np
from scipy.stats import norm


class Option():
    def __init__(self, option, spotPrice, strikePrice, timeDays, rate, dividendYeld, volatility=4, daysYear=360):
        self.option = option
        self.spotP = float(spotPrice)
        self.strikeP = float(strikePrice)
        self.time = float(timeDays)
        self.rate = float(rate)
        self.div = float(dividendYeld)
        self.vol = float(volatility)
        self.daysYear = daysYear
        self.factors()

    def factors(self):
        self.d1 = float(math.log(self.spotP / self.strikeP) + (self.rate - self.div + ((self.vol ** 2.0) / 2.0)) * (
            self.time / self.daysYear)) / (((self.time / self.daysYear) ** (1.0 / 2.0)) * self.vol)
        self.d2 = float(self.d1 - ((self.time / self.daysYear) ** (1.0 / 2.0)) * self.vol)

    def calculatePrice(self):
        if self.option == 'call':
            price = float(
                ((norm(0, 1).cdf(self.d1)) * (
                    self.spotP * math.exp((-self.div) * (self.time / self.daysYear)))) - (
                    norm(0, 1).cdf(self.d2)) * self.strikeP * math.exp(
                    (-self.rate) * (self.time / self.daysYear)))
            # print(float(round(price, 3)))
        else:  # it's put
            price = float(
                ((1 - (norm(0, 1).cdf(self.d1))) * (
                    -self.spotP * math.exp((-self.div) * (self.time / self.daysYear)))) + (
                    1 - (norm(0, 1).cdf(self.d2))) * self.strikeP * (
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
        return float(round(self.vol * 100, 4))
