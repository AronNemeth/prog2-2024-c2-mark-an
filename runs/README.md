# 2026-09-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.79511  |       1.18425  |   0.115338 |
| solution-1-flask   |     0.453191 |       1.00891  |   0.234571 |
| solution-aron-mark |     0.433806 |       0.156534 |   0.235224 |
| solution-pl        |     2.51398  |       0.159234 |   0.235971 |
| solution-1         |     8.32796  |       1e-06    |   0.806288 |
| solution-2         |     5.46446  |       0.639226 |   0.849331 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.436574 |       0.158768 |   0.360793 |
| solution-aron-mark |     0.436206 |       0.159124 |   0.364741 |
| solution-flask     |     0.439175 |       1.00905  |   0.392247 |
| solution-1-flask   |     0.439795 |       1.00916  |   0.728083 |
| solution-2         |     0.441274 |       0.52688  |   7.66603  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.438096 |       0.167557 |    1.06593 |
| solution-aron-mark |     0.438323 |       0.163956 |    1.08694 |
| solution-flask     |     0.439257 |       1.00916  |    1.65166 |
| solution-1-flask   |     0.44101  |       1.00923  |    5.66322 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.449306 |       0.191434 |    3.54448 |
| solution-aron-mark |     0.442954 |       0.192621 |    3.56614 |
| solution-flask     |     0.427657 |       1.00893  |    5.16861 |