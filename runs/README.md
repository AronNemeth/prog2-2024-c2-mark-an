# 2024-05-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.67356  |       1.00908  |   0.069066 |
| solution-pl        |     7.70708  |       0.128623 |   0.177101 |
| solution-aron-mark |     0.682904 |       0.118446 |   0.181689 |
| solution-1-flask   |     1.60854  |       1.09894  |   0.259556 |
| solution-1         |     8.45399  |       1e-06    |   0.751153 |
| solution-2         |     0.664714 |       0.419185 |   1.00407  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.671977 |       1.00865  |   0.174222 |
| solution-aron-mark |     0.675474 |       0.124431 |   0.276282 |
| solution-pl        |     0.667851 |       0.127667 |   0.278227 |
| solution-1-flask   |     0.68393  |       1.00898  |   0.788891 |
| solution-2         |     0.660403 |       0.431075 |   3.42252  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661746 |       1.00896  |   0.710244 |
| solution-aron-mark |     0.663032 |       0.131801 |   0.828885 |
| solution-pl        |     0.663233 |       0.132348 |   0.836219 |
| solution-1-flask   |     0.674291 |       1.009    |   5.58312  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.660366 |       1.00917  |    2.5203  |
| solution-aron-mark |     0.662803 |       0.168664 |    2.61366 |
| solution-pl        |     0.666734 |       0.169036 |    2.62503 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.654925 |       0.298862 |    16.1535 |
| solution-aron-mark |     0.674275 |       0.299291 |    16.4074 |
| solution-flask     |     0.660031 |       1.00923  |    16.7212 |