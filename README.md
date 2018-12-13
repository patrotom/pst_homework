# PST homework #

## Overview ##

Data file: case0101

Description: Creativity score based on type of motivation

### Tasks ###

1. Load the data file, find two observed data groups and separate them. Describe these two data groups. For each group find expected value, variance and median.
2. For each group try to find probability density function (based on histogram) and distribution function (based on ecdf).
3. For each group find probability distribution.
   1. Approximate parameters of normal, exponential and uniform distribution.
   2. Add appropriate probability density functions (PDF) with estimated parameters to the histogram graphs.
   3. Discuss which of the distribution is best to reflect observed data.
4. For each group separately generate probability sample of 100 values from distribution with parameters estimated in the previous point which you have chosen as the best one.
5. For each group separately compute 95 % confidence interval for the expected value.


## Python representation ##

* Each group from data file will be represented as separate variable with data type list containing particular values

**Preview:**

``` python

fe3 = []
fe4 = []

fe3 = [1.6599999666214, 2.00999999046326, 2.16000008583069, 2.42000007629395]
fe4 = [3.82999992370605, 4.07999992370605, 4.26999998092651, 4.53000020980835]

```
