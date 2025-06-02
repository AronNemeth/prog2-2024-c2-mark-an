# 2025-06-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.993    |       1.00832  |   0.101481 |
| solution-pl        |     0.511876 |       0.150498 |   0.239537 |
| solution-aron-mark |     0.515298 |       0.165017 |   0.24039  |
| solution-1-flask   |     5.57743  |       1.09965  |   0.276734 |
| solution-1         |     7.88204  |       1e-06    |   0.675979 |
| solution-2         |     0.514999 |       0.658736 |   0.942222 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.523282 |       0.157874 |   0.362607 |
| solution-pl        |     0.519413 |       0.157022 |   0.369284 |
| solution-flask     |     0.523941 |       1.00839  |   0.377607 |
| solution-1-flask   |     0.524574 |       1.0086   |   0.809742 |
| solution-2         |     0.520562 |       0.52905  |   3.8184   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.540691 |       0.163667 |    1.04442 |
| solution-pl        |     0.577706 |       0.163743 |    1.06184 |
| solution-flask     |     0.546942 |       1.00866  |    1.56543 |
| solution-1-flask   |     0.541407 |       1.00866  |    5.57564 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.530951 |       0.192347 |    3.30862 |
| solution-pl        |     0.522124 |       0.194285 |    3.36374 |
| solution-flask     |     0.535295 |       1.0087   |    5.19227 |