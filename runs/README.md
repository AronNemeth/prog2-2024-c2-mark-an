# 2026-06-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.15787  |       1.04645  |   0.103637 |
| solution-pl        |     6.07414  |       0.189167 |   0.231739 |
| solution-aron-mark |     0.442977 |       0.148061 |   0.236332 |
| solution-1-flask   |     0.426853 |       1.00815  |   0.315649 |
| solution-1         |     7.71723  |       1e-06    |   0.758417 |
| solution-2         |     0.41512  |       0.946154 |   0.928405 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.427243 |       0.14935  |   0.359044 |
| solution-pl        |     0.420194 |       0.150715 |   0.360905 |
| solution-flask     |     0.424956 |       1.00833  |   0.38797  |
| solution-1-flask   |     0.428528 |       1.00842  |   0.813843 |
| solution-2         |     0.423292 |       0.526235 |   9.24207  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.420935 |       0.156735 |    1.09189 |
| solution-aron-mark |     0.427045 |       0.157484 |    1.11239 |
| solution-flask     |     0.422401 |       1.00843  |    1.6541  |
| solution-1-flask   |     0.430461 |       1.00847  |    5.60037 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.426524 |       0.181791 |    3.80847 |
| solution-pl        |     0.423553 |       0.179677 |    3.81084 |
| solution-flask     |     0.428095 |       1.00838  |    5.25795 |