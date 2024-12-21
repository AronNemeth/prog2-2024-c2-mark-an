# 2024-12-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.77157  |       1.00884  |   0.104366 |
| solution-pl        |     0.520557 |       0.10823  |   0.183481 |
| solution-aron-mark |     0.529801 |       0.107316 |   0.184085 |
| solution-1-flask   |     4.81285  |       1.06333  |   0.273686 |
| solution-1         |     7.3274   |       1e-06    |   0.621973 |
| solution-2         |     0.526882 |       0.537032 |   1.05779  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.547871 |       0.108788 |   0.316235 |
| solution-aron-mark |     0.523214 |       0.108138 |   0.318391 |
| solution-flask     |     0.527488 |       1.00876  |   0.502882 |
| solution-1-flask   |     0.551301 |       1.00901  |   0.828026 |
| solution-2         |     0.524396 |       0.466818 |   4.28089  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.525482 |       0.11583  |    1.07452 |
| solution-aron-mark |     0.530622 |       0.116103 |    1.09687 |
| solution-flask     |     0.544411 |       1.00868  |    2.27298 |
| solution-1-flask   |     0.540793 |       1.00887  |    5.86399 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.528805 |       0.143061 |    4.26588 |
| solution-pl        |     0.524742 |       0.14378  |    4.28021 |
| solution-flask     |     0.527314 |       1.00901  |    8.70955 |