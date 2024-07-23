# 2024-07-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.519247 |       1.00913  |   0.098126 |
| solution-aron-mark |     0.523623 |       0.102144 |   0.168047 |
| solution-pl        |     5.88651  |       0.105564 |   0.170626 |
| solution-1-flask   |     1.10416  |       1.09276  |   0.26378  |
| solution-1         |     7.99708  |       1e-06    |   0.601477 |
| solution-2         |     0.512513 |       0.582116 |   0.873577 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.505797 |       1.00909  |   0.227762 |
| solution-aron-mark |     0.525105 |       0.103989 |   0.291312 |
| solution-pl        |     0.535577 |       0.109143 |   0.293804 |
| solution-1-flask   |     0.540073 |       1.00959  |   0.783195 |
| solution-2         |     0.537106 |       0.485087 |   2.65446  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.511765 |       1.00922  |   0.903938 |
| solution-aron-mark |     0.511614 |       0.112734 |   0.998928 |
| solution-pl        |     0.542697 |       0.112882 |   1.00022  |
| solution-1-flask   |     0.511028 |       1.00907  |   5.61001  |
| solution-2         |     0.546004 |       0.546548 |  29.969    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.501122 |       1.00913  |    4.42017 |
| solution-aron-mark |     0.505085 |       0.145054 |    4.47258 |
| solution-pl        |     0.503082 |       0.146836 |    4.50265 |