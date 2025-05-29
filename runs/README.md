# 2025-05-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.90507  |       1.00816  |   0.096318 |
| solution-pl        |     0.523505 |       0.153455 |   0.236009 |
| solution-aron-mark |     0.528229 |       0.157976 |   0.238588 |
| solution-1-flask   |     5.09541  |       1.04878  |   0.284378 |
| solution-1         |     7.60222  |       1e-06    |   0.719707 |
| solution-2         |     0.56223  |       0.711909 |   1.97177  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.538897 |       0.152346 |   0.360027 |
| solution-aron-mark |     0.514447 |       0.150849 |   0.360555 |
| solution-flask     |     0.537035 |       1.00849  |   0.379095 |
| solution-1-flask   |     0.54483  |       1.00873  |   0.818336 |
| solution-2         |     0.546765 |       0.5406   |   2.63196  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.522382 |       0.160582 |    1.0603  |
| solution-pl        |     0.510209 |       0.160267 |    1.06685 |
| solution-flask     |     0.511568 |       1.00866  |    1.57066 |
| solution-1-flask   |     0.520228 |       1.00863  |    5.4381  |
| solution-2         |     0.513068 |       0.57515  |   37.266   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.522248 |       0.192589 |    3.3754  |
| solution-aron-mark |     0.522986 |       0.204277 |    3.38511 |
| solution-flask     |     0.51492  |       1.00865  |    5.19702 |