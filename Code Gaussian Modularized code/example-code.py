from Gaussiandistribution import Gaussian

gaussian_one = Gaussian(22, 2)
print('Mean: {}'.format(gaussian_one.mean))
print('Stdev: {}'.format(gaussian_one.stdev))
print('histogram: {}'.format(gaussian_one.plot_histogram()))
print('pdf(10): {}'.format(gaussian_one.pdf(10)))
