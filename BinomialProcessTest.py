import numpy as np

def nCr(n, r):
    out = np.math.factorial(n)/(np.math.factorial(r)*np.math.factorial(n-r))
    return out

def main():
    # Generate population
    p = 0.583
    s = 2229000 # Population size
    ss = 200 # Sample size
    sampleTime = 50000
    population = np.random.rand(s)
    booleanArray = population < p
    population[booleanArray] = 1
    population[booleanArray == False] = 0

    # obtain actual mean
    actualMean = population.mean()
    print "Actual Mean = ", actualMean

    # Sample 200 events from the population for 10000 times
    sampleMean = []
    for i in xrange(sampleTime):
        samplePopulation = np.zeros(ss)
        for j in xrange(ss):
            samplePopulation[j] = population[np.random.randint(0,s - 1)]
        sampleMean.append(samplePopulation.mean())
    sampleMean = np.array(sampleMean)
    sampleMean[sampleMean > 0.6] = 0
    sampleMean[sampleMean < 0.55] = 0
    booleanArray = sampleMean > 0
    print "Experimental probability: ", booleanArray.sum()/float(sampleTime)

    # Theoretical value with binomial distribution
    theoProp = np.sum([nCr(ss, i) * p**i * (1-p)**(ss-i) for i in xrange(110, 121)])
    print "Theoretical probability: ", theoProp

    pass

if __name__ == '__main__':
    main()