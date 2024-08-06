# 2024-08-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.25674  |       1.10899  |   0.086747 |
| solution-pl        |     1.88724  |       0.102882 |   0.16605  |
| solution-aron-mark |     0.55076  |       0.101662 |   0.168601 |
| solution-1-flask   |     0.555659 |       1.00903  |   0.259854 |
| solution-1         |     7.79842  |       1e-06    |   0.641047 |
| solution-2         |     4.49799  |       0.525661 |   0.99242  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.553923 |       1.00886  |   0.223635 |
| solution-aron-mark |     0.551305 |       0.103021 |   0.287445 |
| solution-pl        |     0.553411 |       0.105096 |   0.288952 |
| solution-1-flask   |     0.55606  |       1.0093   |   0.78075  |
| solution-2         |     0.55322  |       0.469298 |   1.75608  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.546171 |       1.00901  |   0.895176 |
| solution-pl        |     0.549564 |       0.112438 |   0.986544 |
| solution-aron-mark |     0.545334 |       0.110393 |   0.992611 |
| solution-1-flask   |     0.554055 |       1.00886  |   5.52638  |
| solution-2         |     0.552443 |       0.523425 | 295.418    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.550866 |       1.00898  |    4.00109 |
| solution-pl        |     0.549421 |       0.149022 |    4.12878 |
| solution-aron-mark |     0.548109 |       0.15028  |    4.15402 |