# 2025-01-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.93585  |       1.00857  |   0.102179 |
| solution-aron-mark |     0.531367 |       0.107491 |   0.186063 |
| solution-pl        |     0.530366 |       0.116142 |   0.205069 |
| solution-1-flask   |     5.58643  |       1.16593  |   0.265794 |
| solution-1         |     7.80507  |       1e-06    |   0.592947 |
| solution-2         |     0.528284 |       0.579844 |   0.951239 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.527682 |       0.110376 |   0.31572  |
| solution-aron-mark |     0.537779 |       0.112316 |   0.322794 |
| solution-flask     |     0.527546 |       1.00878  |   0.488299 |
| solution-1-flask   |     0.530381 |       1.00848  |   0.814867 |
| solution-2         |     0.528646 |       0.486972 |   4.11487  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.541649 |       0.119742 |    1.07347 |
| solution-pl        |     0.528276 |       0.118459 |    1.07352 |
| solution-flask     |     0.534916 |       1.00894  |    2.19724 |
| solution-1-flask   |     0.533071 |       1.00909  |    5.85096 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.527994 |       0.147637 |    4.51935 |
| solution-pl        |     0.530388 |       0.146091 |    4.65737 |
| solution-flask     |     0.528624 |       1.0091   |    8.70329 |