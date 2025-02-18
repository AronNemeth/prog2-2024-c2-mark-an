# 2025-02-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.524374 |       1.00893  |   0.080675 |
| solution-pl        |     1.74621  |       0.152559 |   0.203602 |
| solution-aron-mark |     0.537561 |       0.140935 |   0.206215 |
| solution-1-flask   |     4.87143  |       1.13742  |   0.268139 |
| solution-1         |     7.22298  |       1e-06    |   0.814064 |
| solution-2         |     0.537649 |       0.63572  |   1.17114  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.533831 |       1.00893  |   0.291355 |
| solution-aron-mark |     0.537083 |       0.143714 |   0.308193 |
| solution-pl        |     0.541696 |       0.14301  |   0.309855 |
| solution-1-flask   |     0.547008 |       1.00905  |   0.802363 |
| solution-2         |     0.535299 |       0.507509 |   3.17351  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.549398 |       0.151805 |   0.909087 |
| solution-aron-mark |     0.550495 |       0.154002 |   0.945185 |
| solution-flask     |     0.539527 |       1.00877  |   1.2329   |
| solution-1-flask   |     0.540812 |       1.00882  |   5.6991   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.553668 |       0.179292 |    2.89613 |
| solution-aron-mark |     0.548644 |       0.181986 |    2.90451 |
| solution-flask     |     0.561054 |       1.00878  |    4.28487 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.556867 |       0.284789 |    17.9347 |
| solution-aron-mark |     0.541801 |       0.282099 |    18.3492 |