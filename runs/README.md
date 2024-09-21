# 2024-09-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.29207  |       1.05922  |   0.082227 |
| solution-aron-mark |     1.84599  |       0.101444 |   0.175114 |
| solution-pl        |     0.546847 |       0.100702 |   0.177223 |
| solution-1-flask   |     0.565902 |       1.00786  |   0.264474 |
| solution-1         |     7.58489  |       1e-06    |   0.709081 |
| solution-2         |     4.47517  |       0.508378 |   0.871698 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.552568 |       1.00809  |   0.204983 |
| solution-aron-mark |     0.551268 |       0.103367 |   0.304069 |
| solution-pl        |     0.54821  |       0.10225  |   0.304274 |
| solution-1-flask   |     0.559494 |       1.00795  |   0.790465 |
| solution-2         |     0.549577 |       0.475739 |   4.1863   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.549343 |       1.00857  |   0.929067 |
| solution-aron-mark |     0.553136 |       0.109755 |   1.03777  |
| solution-pl        |     0.552734 |       0.109101 |   1.04323  |
| solution-1-flask   |     0.558233 |       1.00809  |   5.44863  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.549489 |       1.008    |    3.96518 |
| solution-pl        |     0.551    |       0.137615 |    4.12237 |
| solution-aron-mark |     0.54974  |       0.139244 |    4.12328 |