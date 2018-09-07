def estimate_predictive_distributions(stringX, stringY, L_max, verbose = False):
    #stringX, stringY 
    # Counter for events (X_{t-L}^{t-1}, Y_{t-L}^{t-1})
    word_lookup_marg = Counter()
    # Counter for events (X_{t-L}^{t-1}, Y_{t-L}^{t-1}, Y_{t})
    word_lookup_fut  = Counter()
    Xs = copy.copy(stringX); Ys = copy.copy(stringY)   
    if verbose:
        print 'Estimating predictive distributions using multi-line.'   
    #loops through the episodes    
    for line_ind in range(len(Xs)): 
        #extracts the temporary input and output strings for the current episode
        stringX = Xs[line_ind]; stringY = Ys[line_ind]    
        #checks length input/outputs is the same   
        Tx = len(stringX)
        Ty = len(stringY)
        assert Tx == Ty, 'The two time series must have the same length.'
        T = Tx
        #loops through the current episode episode starting from 0 till length-L_max+1
        for t_ind in range(T-L_max):
            #extracts a subsequence of length L_max+1 taking steps of 1
            cur_stringX = stringX[t_ind:(t_ind + L_max + 1)]
            cur_stringY = stringY[t_ind:(t_ind + L_max + 1)]
            #add the subsequence of length L_max+1/L_max to count
            word_lookup_marg[(cur_stringX, cur_stringY[:-1])] += 1
            #add the subsequence of length L_max+1/L_max+1 to count
            word_lookup_fut[(cur_stringX, cur_stringY)] += 1
            #extracts all the subsequences of length 0:L_max-1
            for remove_inds in range(1, L_max+1):
                trunc_stringX = cur_stringX[:-remove_inds]
                trunc_stringY = cur_stringY[:-remove_inds]
                word_lookup_marg[(trunc_stringX, trunc_stringY[:-1])] += 1
                word_lookup_fut[(trunc_stringX, trunc_stringY)] += 1   
    return word_lookup_marg, word_lookup_fut




