# 2024-09-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.34538  |       1.07543  |   0.091954 |
| solution-aron-mark |     5.97608  |       0.113466 |   0.181165 |
| solution-pl        |     0.612796 |       0.108524 |   0.218401 |
| solution-1-flask   |     0.600252 |       1.00941  |   0.259729 |
| solution-1         |     8.10392  |       1e-06    |   0.807181 |
| solution-2         |     0.577749 |       0.638912 |   1.55503  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.573905 |       1.00926  |   0.192539 |
| solution-aron-mark |     0.57839  |       0.107411 |   0.293483 |
| solution-pl        |     0.589935 |       0.108913 |   0.303922 |
| solution-1-flask   |     0.619709 |       1.00903  |   0.794131 |
| solution-2         |     0.579946 |       0.49533  |   3.59874  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.570843 |       1.00915  |   0.901323 |
| solution-pl        |     0.580796 |       0.119931 |   0.996742 |
| solution-aron-mark |     0.594021 |       0.113077 |   0.998797 |
| solution-1-flask   |     0.576416 |       1.00893  |   5.60056  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.598501 |       0.143777 |    4.28867 |
| solution-flask     |     0.570458 |       1.00911  |    4.30066 |
| solution-aron-mark |     0.579636 |       0.147363 |    4.33983 |