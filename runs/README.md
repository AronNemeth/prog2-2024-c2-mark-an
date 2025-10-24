# 2025-10-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.91408  |       1.0463   |   0.098474 |
| solution-aron-mark |     0.478091 |       0.152059 |   0.238554 |
| solution-pl        |     0.48002  |       0.156673 |   0.241159 |
| solution-1-flask   |     0.482179 |       1.00804  |   0.261895 |
| solution-1         |     7.63935  |       1e-06    |   0.65187  |
| solution-2         |     4.51889  |       0.615671 |   0.889732 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.480078 |       0.154543 |   0.363883 |
| solution-pl        |     0.484601 |       0.157467 |   0.364    |
| solution-flask     |     0.484027 |       1.00826  |   0.372534 |
| solution-1-flask   |     0.483409 |       1.0082   |   0.785329 |
| solution-2         |     0.477757 |       0.496501 |   2.99534  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.48454  |       0.162499 |    1.06334 |
| solution-pl        |     0.481017 |       0.162653 |    1.06781 |
| solution-flask     |     0.480814 |       1.0084   |    1.55567 |
| solution-1-flask   |     0.485741 |       1.00838  |    5.56703 |
| solution-2         |     0.47469  |       0.555431 |   40.4691  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.479387 |       0.194568 |    3.20316 |
| solution-aron-mark |     0.482486 |       0.196613 |    3.21616 |
| solution-flask     |     0.484111 |       1.00814  |    5.08238 |