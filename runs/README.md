# 2026-01-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.70199  |       1.14366  |   0.104075 |
| solution-aron-mark |     0.471232 |       0.163397 |   0.245128 |
| solution-pl        |     0.46542  |       0.163906 |   0.248002 |
| solution-1-flask   |     0.47384  |       1.00806  |   0.264012 |
| solution-1         |     7.85877  |       1e-06    |   0.674141 |
| solution-2         |     4.81755  |       0.614537 |   0.85257  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.474689 |       0.164861 |   0.366251 |
| solution-pl        |     0.464521 |       0.163118 |   0.367455 |
| solution-flask     |     0.479206 |       1.00844  |   0.376104 |
| solution-1-flask   |     0.480027 |       1.0085   |   0.78227  |
| solution-2         |     0.471533 |       0.503503 |  12.949    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.476728 |       0.170504 |    1.08375 |
| solution-aron-mark |     0.467264 |       0.170704 |    1.10142 |
| solution-flask     |     0.466102 |       1.00845  |    1.58157 |
| solution-1-flask   |     0.471359 |       1.00842  |    5.5505  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.469179 |       0.192288 |    3.46972 |
| solution-aron-mark |     0.466787 |       0.191712 |    3.50326 |
| solution-flask     |     0.466859 |       1.00886  |    5.05228 |