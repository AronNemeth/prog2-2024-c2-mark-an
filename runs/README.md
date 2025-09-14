# 2025-09-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.484915 |       1.00832  |   0.09954  |
| solution-pl        |     5.86531  |       0.285391 |   0.234675 |
| solution-aron-mark |     0.475569 |       0.152518 |   0.236068 |
| solution-1-flask   |     1.07471  |       1.0443   |   0.252992 |
| solution-1         |     8.04898  |       1e-06    |   0.669852 |
| solution-2         |     0.480605 |       0.679861 |   1.77468  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.478896 |       0.152595 |   0.364192 |
| solution-pl        |     0.477263 |       0.154716 |   0.369122 |
| solution-flask     |     0.481788 |       1.00811  |   0.384476 |
| solution-1-flask   |     0.483318 |       1.00827  |   0.793481 |
| solution-2         |     0.480942 |       0.514169 |   4.02579  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.490752 |       0.161707 |    1.08102 |
| solution-pl        |     0.482746 |       0.162311 |    1.08328 |
| solution-flask     |     0.516164 |       1.00865  |    1.58445 |
| solution-1-flask   |     0.498303 |       1.0086   |    5.73294 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.485652 |       0.195629 |    3.28168 |
| solution-pl        |     0.487571 |       0.194092 |    3.33777 |
| solution-flask     |     0.485649 |       1.0097   |    5.17188 |