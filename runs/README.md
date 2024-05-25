# 2024-05-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.34492  |       1.12324  |   0.067572 |
| solution-pl        |     0.666612 |       0.104626 |   0.15887  |
| solution-aron-mark |     5.84601  |       0.10168  |   0.160157 |
| solution-1-flask   |     0.671549 |       1.00955  |   0.264854 |
| solution-1         |     8.96176  |       1e-06    |   0.697256 |
| solution-2         |     0.664611 |       0.426199 |   1.12735  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.674237 |       1.00942  |   0.159828 |
| solution-aron-mark |     0.667584 |       0.102547 |   0.253789 |
| solution-pl        |     0.667827 |       0.103545 |   0.257774 |
| solution-1-flask   |     0.682847 |       1.00896  |   0.797094 |
| solution-2         |     0.665405 |       0.44014  |   7.44044  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.671305 |       1.00914  |   0.693062 |
| solution-pl        |     0.662601 |       0.111896 |   0.80767  |
| solution-aron-mark |     0.663713 |       0.110982 |   0.812274 |
| solution-1-flask   |     0.702404 |       1.00906  |   5.50325  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.665468 |       1.00924  |    2.5645  |
| solution-aron-mark |     0.662768 |       0.151753 |    2.61246 |
| solution-pl        |     0.664624 |       0.148857 |    2.61449 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.667053 |       1.00887  |    15.6968 |
| solution-pl        |     0.6664   |       0.27906  |    21.4126 |
| solution-aron-mark |     0.666554 |       0.276699 |    22.1882 |