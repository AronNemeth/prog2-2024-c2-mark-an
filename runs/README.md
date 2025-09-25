# 2025-09-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.41398  |       1.36588  |   0.101866 |
| solution-aron-mark |     0.485262 |       0.15127  |   0.238912 |
| solution-pl        |     0.521435 |       0.159558 |   0.240924 |
| solution-1-flask   |     0.484296 |       1.00817  |   0.270064 |
| solution-1         |     7.32152  |       1e-06    |   0.751862 |
| solution-2         |     4.31764  |       0.8244   |   1.26722  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.491217 |       0.153594 |   0.364957 |
| solution-aron-mark |     0.480747 |       0.155403 |   0.367347 |
| solution-flask     |     0.477432 |       1.00814  |   0.378392 |
| solution-1-flask   |     0.482839 |       1.00844  |   0.806902 |
| solution-2         |     0.479154 |       0.498263 |   5.96789  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.479508 |       0.162268 |    1.07609 |
| solution-aron-mark |     0.482055 |       0.162467 |    1.07786 |
| solution-flask     |     0.483005 |       1.0087   |    1.59012 |
| solution-1-flask   |     0.4856   |       1.00837  |    5.60006 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.48113  |       0.196216 |    3.24009 |
| solution-pl        |     0.478586 |       0.19133  |    3.25728 |
| solution-flask     |     0.477094 |       1.00833  |    5.11883 |