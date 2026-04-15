# 2026-04-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.78454  |       1.03337  |   0.09265  |
| solution-1-flask   |     0.413625 |       1.00856  |   0.221497 |
| solution-pl        |     0.408161 |       0.147534 |   0.221985 |
| solution-aron-mark |     5.21122  |       0.14417  |   0.222303 |
| solution-1         |     8.54615  |       2e-06    |   0.619815 |
| solution-2         |     0.408462 |       0.584475 |   1.33841  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.408921 |       0.148787 |   0.336925 |
| solution-aron-mark |     0.417595 |       0.150076 |   0.339785 |
| solution-flask     |     0.409631 |       1.0088   |   0.370635 |
| solution-1-flask   |     0.415534 |       1.00859  |   0.715668 |
| solution-2         |     0.407139 |       0.500256 |   2.8409   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.417237 |       0.156721 |   0.983192 |
| solution-aron-mark |     0.417905 |       0.154176 |   1.00605  |
| solution-flask     |     0.417345 |       1.00891  |   1.54818  |
| solution-1-flask   |     0.415373 |       1.00894  |   5.61024  |
| solution-2         |     0.409011 |       0.559094 | 166.493    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.424437 |       0.178625 |    3.51712 |
| solution-pl        |     0.403763 |       0.178677 |    3.52037 |
| solution-flask     |     0.40964  |       1.0087   |    4.86428 |