# Finding conditional Gaussian Mixture Model using scikit-learn.mixture.GMM
# Now we will find the conditional distribution of x given y
(con_cen, con_cov, new_p_k) = gmm.cond_dist(np.array([np.nan, y]), \
    cen_lst, cov_lst, p_k)
