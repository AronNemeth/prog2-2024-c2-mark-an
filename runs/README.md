# 2025-07-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.61658  |       1.03686  |   0.099349 |
| solution-pl        |     0.506218 |       0.1511   |   0.234934 |
| solution-aron-mark |     4.48575  |       0.150161 |   0.240695 |
| solution-1-flask   |     0.514    |       1.00846  |   0.267111 |
| solution-1         |     8.23445  |       1e-06    |   0.856533 |
| solution-2         |     0.501381 |       0.666299 |   1.65689  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.512893 |       0.152565 |   0.359565 |
| solution-flask     |     0.502423 |       1.00843  |   0.383749 |
| solution-aron-mark |     0.505879 |       0.151864 |   0.389323 |
| solution-1-flask   |     0.532933 |       1.00862  |   0.802969 |
| solution-2         |     0.50567  |       0.522295 |   2.42231  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.517323 |       0.158628 |    1.06149 |
| solution-pl        |     0.517487 |       0.158024 |    1.0631  |
| solution-flask     |     0.502975 |       1.00813  |    1.57313 |
| solution-1-flask   |     0.509598 |       1.0088   |    5.666   |
| solution-2         |     0.508896 |       0.601762 |  328.807   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.508853 |       0.188546 |    3.28188 |
| solution-pl        |     0.503331 |       0.188729 |    3.32761 |
| solution-flask     |     0.510331 |       1.00842  |    5.23117 |