# 2026-10-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.467963 |       1.00871  |   0.09551  |
| solution-pl        |     0.425231 |       0.164009 |   0.251678 |
| solution-aron-mark |     2.3929   |       0.172183 |   0.253922 |
| solution-1-flask   |     1.58028  |       1.12201  |   0.267542 |
| solution-1         |     7.96235  |       1e-06    |   0.592645 |
| solution-2         |     5.41742  |       0.553793 |   0.910544 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.446498 |       1.00901  |   0.227506 |
| solution-aron-mark |     0.442972 |       0.170954 |   0.388333 |
| solution-pl        |     0.436989 |       0.17239  |   0.390079 |
| solution-1-flask   |     0.445292 |       1.00917  |   0.789917 |
| solution-2         |     0.437364 |       0.521326 |   4.16118  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.435109 |       1.0088   |    1.02101 |
| solution-aron-mark |     0.438546 |       0.180136 |    1.14639 |
| solution-pl        |     0.444735 |       0.178197 |    1.1505  |
| solution-1-flask   |     0.448102 |       1.00898  |    5.57176 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.429182 |       0.208722 |    3.59029 |
| solution-aron-mark |     0.433816 |       0.21265  |    3.61549 |
| solution-flask     |     0.425521 |       1.00865  |    4.34727 |