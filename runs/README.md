# 2024-12-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.18403  |       1.00882  |   0.103862 |
| solution-aron-mark |     0.606586 |       0.108879 |   0.18744  |
| solution-pl        |     0.535961 |       0.111356 |   0.188642 |
| solution-1-flask   |     5.14792  |       1.10096  |   0.265809 |
| solution-1         |     7.93369  |       1e-06    |   0.805089 |
| solution-2         |     0.532715 |       0.56386  |   1.094    |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.534162 |       0.112078 |   0.317138 |
| solution-aron-mark |     0.535858 |       0.112414 |   0.320056 |
| solution-flask     |     0.535568 |       1.00898  |   0.477601 |
| solution-1-flask   |     0.538764 |       1.00889  |   0.813836 |
| solution-2         |     0.529982 |       0.489981 |   2.75725  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.526977 |       0.119402 |    1.08235 |
| solution-aron-mark |     0.535861 |       0.117506 |    1.08765 |
| solution-flask     |     0.532573 |       1.00921  |    2.20999 |
| solution-1-flask   |     0.535666 |       1.00995  |    5.75702 |
| solution-2         |     0.533188 |       0.527348 |   54.2429  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.530537 |       0.147245 |    4.39929 |
| solution-pl        |     0.530298 |       0.146521 |    4.41078 |
| solution-flask     |     0.527811 |       1.00904  |    8.69407 |