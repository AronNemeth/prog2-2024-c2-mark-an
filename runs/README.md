# 2024-11-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |      1.62612 |       1.07203  |   0.113812 |
| solution-pl        |      6.57406 |       0.119204 |   0.192847 |
| solution-aron-mark |      1.04904 |       0.109021 |   0.193663 |
| solution-1-flask   |      1.08149 |       1.00965  |   0.267921 |
| solution-1         |      8.60224 |       1e-06    |   0.81219  |
| solution-2         |      1.08021 |       0.801114 |   0.87207  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.759413 |       0.115929 |   0.304064 |
| solution-aron-mark |     0.622986 |       0.114955 |   0.312077 |
| solution-flask     |     0.621118 |       1.00956  |   0.496286 |
| solution-1-flask   |     0.644582 |       1.0093   |   0.801383 |
| solution-2         |     0.606428 |       0.528697 |   3.47741  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.612419 |       0.123155 |    1.02321 |
| solution-aron-mark |     0.607383 |       0.121622 |    1.03128 |
| solution-flask     |     0.607788 |       1.0092   |    2.22043 |
| solution-1-flask   |     0.608068 |       1.00992  |    5.6702  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.589591 |       0.151896 |    4.99144 |
| solution-aron-mark |     0.61231  |       0.149407 |    5.05032 |
| solution-flask     |     0.614321 |       1.00964  |    9.44355 |