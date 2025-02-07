# 2025-02-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.17054  |       1.05699  |   0.082323 |
| solution-aron-mark |     0.54458  |       0.13703  |   0.206555 |
| solution-pl        |     4.52854  |       0.143589 |   0.208339 |
| solution-1-flask   |     0.562114 |       1.00899  |   0.267459 |
| solution-1         |     7.32236  |       1e-06    |   0.622794 |
| solution-2         |     0.559751 |       0.578842 |   0.934114 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.544824 |       1.00907  |   0.300044 |
| solution-pl        |     0.554094 |       0.141541 |   0.308639 |
| solution-aron-mark |     0.545854 |       0.142996 |   0.315518 |
| solution-1-flask   |     0.554965 |       1.00901  |   0.808532 |
| solution-2         |     0.53452  |       0.496797 |   4.8066   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.548884 |       0.145968 |   0.889625 |
| solution-pl        |     0.547914 |       0.151241 |   0.914972 |
| solution-flask     |     0.540126 |       1.00926  |   1.24717  |
| solution-1-flask   |     0.550065 |       1.00891  |   5.72831  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.543161 |       0.178739 |    2.85033 |
| solution-aron-mark |     0.569117 |       0.177586 |    2.85441 |
| solution-flask     |     0.544355 |       1.00852  |    4.223   |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.550595 |       0.283495 |    17.5989 |
| solution-aron-mark |     0.542157 |       0.279541 |    17.6379 |