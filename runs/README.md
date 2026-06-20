# 2026-06-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.20908  |       1.08767  |   0.103048 |
| solution-pl        |     5.89897  |       0.141757 |   0.209655 |
| solution-aron-mark |     0.386297 |       0.137933 |   0.209889 |
| solution-1-flask   |     0.394793 |       1.00657  |   0.236547 |
| solution-1         |     7.11333  |       1e-06    |   0.631149 |
| solution-2         |     0.378952 |       0.638141 |   0.98081  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.386888 |       0.137327 |   0.317655 |
| solution-aron-mark |     0.387905 |       0.136081 |   0.323696 |
| solution-flask     |     0.388806 |       1.00669  |   0.410276 |
| solution-1-flask   |     0.389436 |       1.00678  |   0.716389 |
| solution-2         |     0.39229  |       0.475389 |   3.6726   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.390349 |       0.147247 |   0.993862 |
| solution-pl        |     0.390095 |       0.146161 |   1.0001   |
| solution-flask     |     0.392227 |       1.00734  |   1.75466  |
| solution-1-flask   |     0.392474 |       1.00677  |   5.34063  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.388426 |       0.173742 |    4.51908 |
| solution-aron-mark |     0.393419 |       0.1745   |    4.75995 |
| solution-flask     |     0.388808 |       1.00686  |    5.72085 |