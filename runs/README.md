# 2025-06-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.495185 |       1.00825  |   0.101444 |
| solution-pl        |     0.492995 |       0.151974 |   0.237077 |
| solution-aron-mark |     5.52033  |       0.19181  |   0.237437 |
| solution-1-flask   |     1.12344  |       1.10647  |   0.264552 |
| solution-1         |     7.41111  |       1e-06    |   0.668852 |
| solution-2         |     0.510835 |       0.618643 |   1.46711  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.496262 |       0.156475 |   0.368848 |
| solution-aron-mark |     0.528694 |       0.165665 |   0.370031 |
| solution-flask     |     0.505461 |       1.0085   |   0.387204 |
| solution-1-flask   |     0.504398 |       1.00839  |   0.870288 |
| solution-2         |     0.50725  |       0.512894 |   2.7115   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.50871  |       0.159125 |    1.06971 |
| solution-aron-mark |     0.500299 |       0.155987 |    1.07455 |
| solution-flask     |     0.506612 |       1.00886  |    1.59753 |
| solution-1-flask   |     0.505475 |       1.00821  |    5.43002 |
| solution-2         |     0.509437 |       0.567485 |  154.607   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.499039 |       0.188601 |    3.23517 |
| solution-pl        |     0.501528 |       0.185946 |    3.23619 |
| solution-flask     |     0.497717 |       1.00849  |    5.16353 |