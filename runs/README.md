# 2026-03-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.11441  |       1.08556  |   0.107058 |
| solution-pl        |     4.58953  |       0.152272 |   0.233932 |
| solution-aron-mark |     0.443277 |       0.14905  |   0.242207 |
| solution-1-flask   |     0.451259 |       1.00854  |   0.269083 |
| solution-1         |     7.89109  |       1e-06    |   0.690461 |
| solution-2         |     0.444975 |       0.652418 |   1.07081  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.447973 |       0.151849 |   0.368438 |
| solution-aron-mark |     0.447553 |       0.149317 |   0.37289  |
| solution-flask     |     0.446144 |       1.00862  |   0.388243 |
| solution-1-flask   |     0.449111 |       1.00885  |   0.789591 |
| solution-2         |     0.444405 |       0.515642 |   2.40644  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.443927 |       0.154368 |    1.10447 |
| solution-pl        |     0.445213 |       0.156385 |    1.14835 |
| solution-flask     |     0.444129 |       1.00883  |    1.64518 |
| solution-1-flask   |     0.453959 |       1.00874  |    5.55256 |
| solution-2         |     0.44526  |       0.57507  |   30.2343  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.451512 |       0.183105 |    3.99481 |
| solution-aron-mark |     0.449582 |       0.18146  |    3.99827 |
| solution-flask     |     0.446346 |       1.0089   |    5.19644 |