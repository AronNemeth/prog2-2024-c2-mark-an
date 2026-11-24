# 2026-11-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.254318 |       1.00882  |   0.044624 |
| solution-1-flask   |     0.778848 |       1.05499  |   0.117857 |
| solution-pl        |     4.69057  |       0.104365 |   0.135736 |
| solution-aron-mark |     0.264767 |       0.105728 |   0.142454 |
| solution-1         |     4.91578  |       1e-06    |   0.367233 |
| solution-2         |     0.281223 |       0.356948 |   0.739241 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.268788 |       1.00881  |   0.100947 |
| solution-aron-mark |     0.255218 |       0.10145  |   0.196254 |
| solution-pl        |     0.267038 |       0.101481 |   0.199781 |
| solution-1-flask   |     0.260828 |       1.00864  |   0.359838 |
| solution-2         |     0.265632 |       0.335077 |   2.25712  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.245366 |       1.00863  |   0.434398 |
| solution-pl        |     0.264001 |       0.108297 |   0.514987 |
| solution-aron-mark |     0.257758 |       0.112864 |   0.572224 |
| solution-1-flask   |     0.254108 |       1.00852  |   2.75124  |
| solution-2         |     0.272502 |       0.372194 |  91.7732   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.249812 |       0.134859 |    1.77721 |
| solution-aron-mark |     0.26302  |       0.128966 |    1.7947  |
| solution-flask     |     0.248497 |       1.00861  |    2.03389 |
| solution-1-flask   |     0.25956  |       1.00884  |   23.5398  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.252627 |       0.184547 |    11.9146 |
| solution-aron-mark |     0.258808 |       0.190841 |    12.2088 |
| solution-flask     |     0.266799 |       1.00899  |    16.0475 |