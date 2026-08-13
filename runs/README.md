# 2026-08-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.8861   |       1.18888  |   0.100919 |
| solution-1-flask   |     0.943287 |       1.01021  |   0.232523 |
| solution-aron-mark |     5.37877  |       0.155455 |   0.236109 |
| solution-pl        |     0.928685 |       0.155132 |   0.239934 |
| solution-1         |     8.78063  |       1e-06    |   0.628491 |
| solution-2         |     0.944158 |       0.735391 |   0.944757 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.456354 |       0.159728 |   0.353576 |
| solution-aron-mark |     0.447123 |       0.158113 |   0.363333 |
| solution-flask     |     0.53359  |       1.00932  |   0.392944 |
| solution-1-flask   |     0.464983 |       1.00936  |   0.731991 |
| solution-2         |     0.441625 |       0.529727 |   4.68678  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.45043  |       0.167149 |    1.05423 |
| solution-aron-mark |     0.457944 |       0.165476 |    1.06184 |
| solution-flask     |     0.447998 |       1.00936  |    1.67761 |
| solution-1-flask   |     0.457691 |       1.00933  |    5.79078 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.44474  |       0.200524 |    3.51987 |
| solution-aron-mark |     0.450397 |       0.185027 |    3.58802 |
| solution-flask     |     0.45758  |       1.0093   |    5.57103 |