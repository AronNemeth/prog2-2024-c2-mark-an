# 2026-07-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.951    |       1.05575  |   0.100758 |
| solution-1-flask   |     0.444272 |       1.00921  |   0.226024 |
| solution-pl        |     0.437936 |       0.153741 |   0.230406 |
| solution-aron-mark |     0.438994 |       0.15908  |   0.231066 |
| solution-1         |     7.2921   |       1e-06    |   0.625494 |
| solution-2         |     4.44775  |       0.640887 |   1.13035  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.42805  |       0.152966 |   0.355321 |
| solution-aron-mark |     0.429116 |       0.153291 |   0.357991 |
| solution-flask     |     0.431859 |       1.00905  |   0.394109 |
| solution-1-flask   |     0.434544 |       1.0093   |   0.726645 |
| solution-2         |     0.448211 |       0.508867 |   3.16582  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.432156 |       0.159592 |    1.0327  |
| solution-aron-mark |     0.430176 |       0.158706 |    1.03405 |
| solution-flask     |     0.43067  |       1.00931  |    1.65549 |
| solution-1-flask   |     0.440714 |       1.00918  |    5.72404 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.427135 |       0.186961 |    3.89952 |
| solution-aron-mark |     0.433236 |       0.186228 |    3.90346 |
| solution-flask     |     0.432919 |       1.00939  |    5.35276 |