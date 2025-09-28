# 2025-09-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.11656  |       1.07638  |   0.112184 |
| solution-pl        |     0.944684 |       0.15541  |   0.240415 |
| solution-aron-mark |     0.947758 |       0.156698 |   0.245609 |
| solution-1-flask   |     0.951596 |       1.00819  |   0.265007 |
| solution-1         |     7.8747   |       1e-06    |   0.994685 |
| solution-2         |     5.04606  |       0.945065 |   1.32674  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.938732 |       0.155218 |   0.369818 |
| solution-pl        |     0.485549 |       0.155401 |   0.39062  |
| solution-flask     |     0.936016 |       1.00844  |   0.401772 |
| solution-1-flask   |     0.490617 |       1.00847  |   0.807875 |
| solution-2         |     0.934288 |       0.51048  |   3.78837  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.485389 |       0.163239 |    1.08871 |
| solution-aron-mark |     0.485316 |       0.163451 |    1.11729 |
| solution-flask     |     0.481086 |       1.00865  |    1.58592 |
| solution-1-flask   |     0.489828 |       1.00858  |    5.64455 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.488986 |       0.200356 |    3.34104 |
| solution-aron-mark |     0.493251 |       0.196149 |    3.35002 |
| solution-flask     |     0.483485 |       1.00841  |    5.27232 |