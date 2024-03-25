# 2024-03-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.95     |       1.04653  |   0.064793 |
| solution-pl        |     0.652562 |       0.112181 |   0.162662 |
| solution-aron-mark |     0.672319 |       0.110888 |   0.167576 |
| solution-1-flask   |     0.659494 |       1.00866  |   0.263813 |
| solution-2         |     5.05323  |       0.666269 |   0.784739 |
| solution-1         |     9.20614  |       1e-06    |   0.855284 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.655852 |       1.00875  |   0.179992 |
| solution-pl        |     0.662643 |       0.115142 |   0.25194  |
| solution-aron-mark |     0.654045 |       0.114697 |   0.252734 |
| solution-1-flask   |     0.663918 |       1.00887  |   0.78543  |
| solution-2         |     0.65119  |       0.454041 |   2.04346  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.648099 |       0.120584 |   0.810058 |
| solution-pl        |     0.651201 |       0.120865 |   0.821656 |
| solution-flask     |     0.658461 |       1.0086   |   0.972494 |
| solution-1-flask   |     0.664932 |       1.00877  |   5.4821   |
| solution-2         |     0.657704 |       0.503675 | 154.809    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.64803  |       0.155221 |    3.27489 |
| solution-pl        |     0.650675 |       0.153082 |    3.31811 |
| solution-flask     |     0.657176 |       1.00886  |    5.4206  |