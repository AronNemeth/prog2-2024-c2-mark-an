# 2026-01-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.61055  |       1.05861  |   0.103801 |
| solution-aron-mark |     0.662691 |       0.162088 |   0.24738  |
| solution-1-flask   |     0.47243  |       1.00853  |   0.257582 |
| solution-pl        |     0.472624 |       0.162452 |   0.268059 |
| solution-1         |     8.27381  |       1e-06    |   0.723176 |
| solution-2         |     5.59197  |       0.648531 |   1.33708  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.472762 |       0.166215 |   0.380795 |
| solution-flask     |     0.469439 |       1.00838  |   0.385518 |
| solution-pl        |     0.478667 |       0.162386 |   0.405704 |
| solution-1-flask   |     0.476934 |       1.00824  |   0.803447 |
| solution-2         |     0.481498 |       0.512591 |   3.3913   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.476936 |       0.17019  |    1.09681 |
| solution-pl        |     0.474845 |       0.168079 |    1.10529 |
| solution-flask     |     0.474137 |       1.00833  |    1.60692 |
| solution-1-flask   |     0.484854 |       1.00844  |    5.68079 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.476891 |       0.196745 |    3.54794 |
| solution-pl        |     0.476223 |       0.193594 |    3.57288 |
| solution-flask     |     0.482749 |       1.00846  |    5.13393 |