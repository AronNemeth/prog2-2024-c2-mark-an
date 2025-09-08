# 2025-09-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.487086 |       1.00808  |   0.100208 |
| solution-aron-mark |     0.48485  |       0.154181 |   0.241653 |
| solution-pl        |     5.81335  |       0.197811 |   0.243733 |
| solution-1-flask   |     1.18037  |       1.04265  |   0.268884 |
| solution-1         |     7.89892  |       1e-06    |   0.665091 |
| solution-2         |     0.493453 |       0.632854 |   0.937877 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.500715 |       0.156723 |   0.366462 |
| solution-pl        |     0.484603 |       0.156571 |   0.367207 |
| solution-flask     |     0.48374  |       1.00854  |   0.380305 |
| solution-1-flask   |     0.492434 |       1.00853  |   0.805449 |
| solution-2         |     0.48627  |       0.511118 |   2.96799  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.487983 |       0.162312 |    1.0749  |
| solution-aron-mark |     0.488391 |       0.161501 |    1.07625 |
| solution-flask     |     0.482137 |       1.00851  |    1.57474 |
| solution-1-flask   |     0.494312 |       1.00859  |    5.69658 |
| solution-2         |     0.495047 |       0.563986 |  169.25    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.487489 |       0.194808 |    3.27975 |
| solution-pl        |     0.487015 |       0.196513 |    3.32156 |
| solution-flask     |     0.484076 |       1.00879  |    5.16346 |