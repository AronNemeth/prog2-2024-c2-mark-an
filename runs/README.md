# 2026-02-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.76882  |       1.12424  |   0.101212 |
| solution-aron-mark |     0.452255 |       0.16851  |   0.252873 |
| solution-pl        |     0.460489 |       0.170661 |   0.253299 |
| solution-1-flask   |     0.455039 |       1.00813  |   0.269922 |
| solution-1         |     7.73238  |       1e-06    |   0.639611 |
| solution-2         |     4.64428  |       0.58232  |   1.04889  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.449128 |       0.17341  |   0.381073 |
| solution-flask     |     0.443184 |       1.00849  |   0.386914 |
| solution-aron-mark |     0.44734  |       0.172108 |   0.391329 |
| solution-1-flask   |     0.471458 |       1.00852  |   0.813283 |
| solution-2         |     0.457073 |       0.534941 |   2.73349  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.460148 |       0.173399 |    1.09892 |
| solution-pl        |     0.448191 |       0.175847 |    1.10136 |
| solution-flask     |     0.451046 |       1.00863  |    1.56938 |
| solution-1-flask   |     0.448706 |       1.00845  |    5.46971 |
| solution-2         |     0.452368 |       0.565848 |  164.24    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.452065 |       0.200669 |    3.74177 |
| solution-aron-mark |     0.458178 |       0.205366 |    3.91455 |
| solution-flask     |     0.448155 |       1.00848  |    5.11691 |