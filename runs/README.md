# 2024-04-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.656594 |       1.00902  |   0.062449 |
| solution-pl        |     5.66341  |       0.109158 |   0.16301  |
| solution-aron-mark |     0.648924 |       0.10683  |   0.164825 |
| solution-1-flask   |     1.30008  |       1.04042  |   0.25631  |
| solution-1         |     7.85832  |       1e-06    |   0.580986 |
| solution-2         |     0.648731 |       0.413836 |   1.21587  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.660262 |       1.00909  |   0.170348 |
| solution-aron-mark |     0.657645 |       0.114882 |   0.256917 |
| solution-pl        |     0.662672 |       0.119267 |   0.257545 |
| solution-1-flask   |     0.67294  |       1.00854  |   0.779697 |
| solution-2         |     0.661969 |       0.426114 |   2.4151   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.654697 |       0.120635 |   0.808935 |
| solution-aron-mark |     0.657614 |       0.1199   |   0.832484 |
| solution-flask     |     0.651636 |       1.00869  |   0.91001  |
| solution-1-flask   |     0.666615 |       1.00908  |   5.46382  |
| solution-2         |     0.655738 |       0.476767 | 154.253    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.653958 |       0.156388 |    3.16694 |
| solution-pl        |     0.657005 |       0.156896 |    3.20394 |
| solution-flask     |     0.657409 |       1.00859  |    5.09054 |