from Gaussiandistribution import Gaussian
from  Binomialdistribution import Binomial

gaussian_one = Gaussian()
print('G Mean: {}'.format(gaussian_one.mean))
print('G Stdev: {}'.format(gaussian_one.stdev))
print('G histogram: {}'.format(gaussian_one.plot_histogram()))
print('G pdf(10): {}'.format(gaussian_one.pdf(10)))

binomial_one= Binomial()
binomial_one.calculate_mean
calculate_stdev
print('B Mean: {}'.format(binomial_one.mean))
print('B Stdev: {}'.format(binomial_one.stdev))
