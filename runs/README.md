# 2024-09-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.17164  |       1.08083  |   0.082087 |
| solution-pl        |     0.546386 |       0.100314 |   0.174603 |
| solution-aron-mark |     1.89416  |       0.099835 |   0.175528 |
| solution-1-flask   |     0.562505 |       1.00802  |   0.250792 |
| solution-1         |     7.68096  |       1e-06    |   0.911124 |
| solution-2         |     4.37843  |       0.683056 |   1.25097  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.5284   |       1.00795  |   0.204664 |
| solution-aron-mark |     0.546531 |       0.099129 |   0.297231 |
| solution-pl        |     0.538714 |       0.102761 |   0.297553 |
| solution-1-flask   |     0.542097 |       1.00788  |   0.743829 |
| solution-2         |     0.543685 |       0.462131 |   3.76684  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.543817 |       1.00813  |   0.912117 |
| solution-aron-mark |     0.546467 |       0.109406 |   1.01451  |
| solution-pl        |     0.542862 |       0.107376 |   1.06391  |
| solution-1-flask   |     0.543928 |       1.00779  |   5.3216   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.549309 |       1.00848  |    4.07933 |
| solution-aron-mark |     0.548522 |       0.136255 |    4.14799 |
| solution-pl        |     0.558662 |       0.135254 |    4.17707 |