import matplotlib.pyplot as plt
import numpy as np

# Plot guassian distributions
def plot_normal_distributions(filename):
    max_x = 10
    def normal_pdf(x, mu, sigma):
        return 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2))

    x = np.linspace(-max_x, max_x, 100)
    plt.figure(figsize=(8,4))
    plt.title('Normal Distributions')
    plt.plot(x, normal_pdf(x, 0, 1) , linewidth=2, color='r', linestyle='solid')
    plt.plot(x, normal_pdf(x, 0, 2.5), linewidth=2, color='b', linestyle='dashed')
    plt.plot(x, normal_pdf(x, -5, 2), linewidth=2, color='g', linestyle='dotted')
    plt.xlabel(r'$x$')
    plt.savefig(filename, transparent=True, dpi=1000)

plot_normal_distributions(filename='notes01_distributions.png')