# 2026-04-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.06562  |       1.04461  |   0.099274 |
| solution-pl        |     4.7094   |       0.149315 |   0.227073 |
| solution-1-flask   |     0.413804 |       1.00882  |   0.228115 |
| solution-aron-mark |     0.410033 |       0.149709 |   0.228202 |
| solution-1         |     8.86861  |       1e-06    |   0.610931 |
| solution-2         |     0.404876 |       0.556327 |   0.763383 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.407256 |       0.148105 |   0.348801 |
| solution-flask     |     0.407607 |       1.00898  |   0.383705 |
| solution-aron-mark |     0.40944  |       0.15076  |   0.386037 |
| solution-1-flask   |     0.423955 |       1.00938  |   0.714624 |
| solution-2         |     0.409398 |       0.523514 |   4.51615  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.415776 |       0.160565 |    1.03586 |
| solution-aron-mark |     0.416654 |       0.155772 |    1.04207 |
| solution-flask     |     0.419206 |       1.00905  |    1.62926 |
| solution-1-flask   |     0.419375 |       1.00975  |    5.57018 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.423343 |       0.181818 |    3.90408 |
| solution-pl        |     0.420256 |       0.183752 |    3.92336 |
| solution-flask     |     0.425285 |       1.00894  |    5.25415 |