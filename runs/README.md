# 2025-12-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.66078  |       1.04694  |   0.101095 |
| solution-pl        |     0.488219 |       0.169242 |   0.249891 |
| solution-aron-mark |     0.496422 |       0.169101 |   0.253117 |
| solution-1-flask   |     0.500061 |       1.00864  |   0.267677 |
| solution-1         |     7.96424  |       2e-06    |   0.708784 |
| solution-2         |     4.72475  |       0.665319 |   0.905462 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.498966 |       1.00854  |   0.376325 |
| solution-aron-mark |     0.491757 |       0.170836 |   0.377548 |
| solution-pl        |     0.489753 |       0.169556 |   0.378184 |
| solution-1-flask   |     0.490504 |       1.00866  |   0.801729 |
| solution-2         |     0.490722 |       0.537793 |   2.28825  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.486383 |       0.174656 |    1.06932 |
| solution-pl        |     0.491621 |       0.179634 |    1.07493 |
| solution-flask     |     0.489715 |       1.0087   |    1.56484 |
| solution-1-flask   |     0.477694 |       1.00883  |    5.72643 |
| solution-2         |     0.495867 |       0.601331 |   54.8692  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.481994 |       0.201348 |    3.61064 |
| solution-pl        |     0.48036  |       0.193636 |    3.71375 |
| solution-flask     |     0.483266 |       1.00867  |    5.20281 |