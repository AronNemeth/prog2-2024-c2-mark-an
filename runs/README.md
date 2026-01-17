# 2026-01-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.73109  |       1.1049   |   0.101267 |
| solution-aron-mark |     0.491995 |       0.165494 |   0.245346 |
| solution-pl        |     0.472969 |       0.165663 |   0.248246 |
| solution-1-flask   |     0.487341 |       1.00807  |   0.268569 |
| solution-1         |     7.44465  |       1e-06    |   0.624496 |
| solution-2         |     4.72891  |       0.715814 |   1.00615  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.482074 |       0.172187 |   0.36744  |
| solution-aron-mark |     0.500096 |       0.168124 |   0.373421 |
| solution-flask     |     0.488407 |       1.0086   |   0.381127 |
| solution-1-flask   |     0.496292 |       1.00967  |   0.798328 |
| solution-2         |     0.485888 |       0.542573 |   2.67043  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.506175 |       0.178851 |    1.08051 |
| solution-aron-mark |     0.536053 |       0.184598 |    1.09691 |
| solution-flask     |     0.508765 |       1.00875  |    1.60165 |
| solution-1-flask   |     0.536458 |       1.00949  |    5.8763  |
| solution-2         |     0.472679 |       0.59405  |   40.2161  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.485948 |       0.199519 |    3.6531  |
| solution-pl        |     0.487002 |       0.195876 |    3.66811 |
| solution-flask     |     0.502665 |       1.00866  |    5.17625 |