# 2026-08-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.36158  |       1.05866  |   0.139381 |
| solution-pl        |     0.482457 |       0.161062 |   0.247432 |
| solution-aron-mark |     4.5786   |       0.160763 |   0.253968 |
| solution-1-flask   |     0.493319 |       1.00901  |   0.280905 |
| solution-1         |     7.79033  |       1e-06    |   0.731532 |
| solution-2         |     0.456295 |       0.704778 |   1.74301  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.438513 |       0.155907 |   0.384928 |
| solution-aron-mark |     0.492627 |       0.162297 |   0.386549 |
| solution-flask     |     0.4556   |       1.00876  |   0.399134 |
| solution-1-flask   |     0.491096 |       1.00867  |   0.816672 |
| solution-2         |     0.434434 |       0.536094 |  13.306    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.494374 |       0.179703 |    1.1696  |
| solution-pl        |     0.469257 |       0.172492 |    1.17215 |
| solution-flask     |     0.503769 |       1.00943  |    1.74321 |
| solution-1-flask   |     0.46087  |       1.00898  |    6.15006 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.444024 |       0.183637 |    3.95094 |
| solution-pl        |     0.472222 |       0.198481 |    4.07391 |
| solution-flask     |     0.483123 |       1.00885  |    5.63309 |