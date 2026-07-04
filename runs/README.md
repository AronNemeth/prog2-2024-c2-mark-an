# 2026-07-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.1708   |       1.0964   |   0.116095 |
| solution-aron-mark |     0.446897 |       0.149082 |   0.237684 |
| solution-pl        |     5.81519  |       0.169762 |   0.240443 |
| solution-1-flask   |     0.439285 |       1.00841  |   0.310601 |
| solution-1         |     7.3042   |       1e-06    |   0.673105 |
| solution-2         |     0.414774 |       0.69822  |   0.950694 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.434247 |       0.151549 |   0.375754 |
| solution-pl        |     0.427497 |       0.153583 |   0.376824 |
| solution-flask     |     0.427584 |       1.00823  |   0.401983 |
| solution-1-flask   |     0.432754 |       1.00855  |   0.807595 |
| solution-2         |     0.426763 |       0.506827 |   3.13364  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.433197 |       0.162552 |    1.14164 |
| solution-pl        |     0.426253 |       0.156548 |    1.14271 |
| solution-flask     |     0.429142 |       1.00832  |    1.69488 |
| solution-1-flask   |     0.435768 |       1.00886  |    5.83834 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.44137  |       0.185153 |    4.03047 |
| solution-aron-mark |     0.437664 |       0.183706 |    4.07895 |
| solution-flask     |     0.429255 |       1.00838  |    5.49198 |