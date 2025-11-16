# 2025-11-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.8555   |       1.10756  |   0.090306 |
| solution-aron-mark |     0.426617 |       0.141064 |   0.217921 |
| solution-pl        |     0.420581 |       0.140743 |   0.218163 |
| solution-1-flask   |     0.428648 |       1.00665  |   0.233449 |
| solution-1         |     7.58727  |       1e-06    |   0.6856   |
| solution-2         |     4.85767  |       0.776835 |   0.785743 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.447081 |       0.143475 |   0.324629 |
| solution-aron-mark |     0.429392 |       0.145925 |   0.332306 |
| solution-flask     |     0.428008 |       1.00659  |   0.40232  |
| solution-1-flask   |     0.437178 |       1.00664  |   0.733966 |
| solution-2         |     0.424967 |       0.482171 |   3.24009  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.440527 |       0.154029 |   0.950909 |
| solution-aron-mark |     0.422696 |       0.152496 |   0.971479 |
| solution-flask     |     0.423042 |       1.00683  |   1.72808  |
| solution-1-flask   |     0.428145 |       1.00664  |   5.29854  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.426051 |       0.183789 |    3.80336 |
| solution-pl        |     0.42394  |       0.18187  |    3.8213  |
| solution-flask     |     0.424702 |       1.00698  |    5.60435 |