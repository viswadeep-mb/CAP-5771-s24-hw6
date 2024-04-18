import pickle
import numpy as np
from numpy.typing import NDArray


def em_algorithm(data: NDArray[np.floating], max_iter: int = 100) -> tuple[
    tuple[np.floating] | None,
    tuple[np.floating] | None,
    tuple[NDArray[np.floating]] | None,
    tuple[NDArray[np.floating]] | None,
]:
    """
    Arguments:
    - data: numpy array of shape 50,000 x 2
    - max_iter: maximum number of iterations for the algorithm

    Return:
    - weights: the two coefficients \rho_1 and \rho_2 of the mixture model
    - means: the means of the two Gaussians (two scalars) as a list
    - covariances: the covariance matrices of the two Gaussians
      (each is a 2x2 symmetric matrix) return the full matrix
    - log_likelihoods: `max_iter` values of the log_likelihood, including the initial value

    Notes:
    - order the distribution parameters such that the x-component of
          the means are ordered from largest to smallest.
    - hint: the log-likelihood is monotonically increasing (or constant)
          if the algorithm is implemented correctly.
    - If this code is copied from some source, make sure to reference the
        source in this doc-string.
    """
    # CODE FILLED BY STUDENT

    weights = None
    means = None
    covariances = None
    log_likelihoods = None

    return weights, means, covariances, log_likelihoods


# ----------------------------------------------------------------------
def gaussian_mixture():
    """
    Calculate the parameters of a Gaussian mixture model using the EM algorithm.
    Specialized to two distributions.
    """
    answers = {}

    # ADD STUDENT CODE

    # Return the `em_algorithm` funtion 
    answers["em_algorithm_function"] = em_algorithm

    # 1D numpy array of floats
    answers["log_likelihood"] = None

    # a line plot using matplotlib.pyplot.plot
    # Make sure to include title, axis labels, and a grid.
    # Save the plot to file "plot_log_likelihood.pdf", and add to your report.
    answers["plot_log_likelihood"] = None

    # list with the mean and standard deviation (over 10 trials) of the mean vector
    # of the first distribution
    answers["prob1_mean"] = None

    # list with the mean and standard deviation (over 10 trials) of the covariance matrix
    # of the first distribution. The covariance matrix should be in the standard order.
    # (https://www.cuemath.com/algebra/covariance-matrix/)
    answers["prob1_covariance"] = None

    # list with the mean and standard deviation (over 10 trials) of the amplitude \rho_1
    # of the first distribution.
    answers["prob1_amplitude"] = None

    # Repeat the above for the second distribution.
    # Remember \mu_x (mean value of x_1 coordinate) should be ordered from largest to smallest.
    answers["prob2_mean"] = None
    answers["prob2_covariance"] = None
    answers["prob2_amplitude"] = None

    return answers


# ----------------------------------------------------------------------
if __name__ == "__main__":
    all_answers = gaussian_mixture()
    with open("gaussian_mixture.pkl", "wb") as fd:
        pickle.dump(all_answers, fd, protocol=pickle.HIGHEST_PROTOCOL)
