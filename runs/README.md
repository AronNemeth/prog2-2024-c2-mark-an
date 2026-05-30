# 2026-05-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.68745  |       1.09981  |   0.110175 |
| solution-aron-mark |     0.436195 |       0.154044 |   0.239249 |
| solution-pl        |     0.433605 |       0.155039 |   0.246622 |
| solution-1-flask   |     0.446538 |       1.00848  |   0.272026 |
| solution-1         |     7.69181  |       1e-06    |   0.646434 |
| solution-2         |     4.53548  |       0.703014 |   1.32524  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.432328 |       0.159112 |   0.376226 |
| solution-pl        |     0.436029 |       0.151852 |   0.377888 |
| solution-flask     |     0.433335 |       1.00827  |   0.408006 |
| solution-1-flask   |     0.435995 |       1.00843  |   0.827217 |
| solution-2         |     0.442516 |       0.519558 |   4.54609  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.434899 |       0.158128 |    1.13807 |
| solution-aron-mark |     0.441081 |       0.162208 |    1.13881 |
| solution-flask     |     0.430204 |       1.00881  |    1.69261 |
| solution-1-flask   |     0.445277 |       1.00836  |    5.6378  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.430878 |       0.183295 |    4.13498 |
| solution-aron-mark |     0.431809 |       0.185001 |    4.16976 |
| solution-flask     |     0.435331 |       1.00855  |    5.53082 |