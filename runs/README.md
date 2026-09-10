# 2026-09-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.59045  |       1.04107  |   0.113711 |
| solution-pl        |     2.28883  |       0.216971 |   0.237003 |
| solution-aron-mark |     0.426717 |       0.154854 |   0.239531 |
| solution-1-flask   |     0.4271   |       1.00822  |   0.264243 |
| solution-1         |     7.75756  |       1e-06    |   0.706981 |
| solution-2         |     4.56992  |       0.591256 |   1.73399  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.428248 |       0.15675  |   0.378632 |
| solution-pl        |     0.4259   |       0.162421 |   0.383133 |
| solution-flask     |     0.426709 |       1.00815  |   0.408015 |
| solution-1-flask   |     0.432677 |       1.00839  |   0.81387  |
| solution-2         |     0.423252 |       0.50299  |   3.35129  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.426349 |       0.160669 |    1.14401 |
| solution-aron-mark |     0.418893 |       0.159429 |    1.14584 |
| solution-flask     |     0.424173 |       1.00878  |    1.67047 |
| solution-1-flask   |     0.425348 |       1.00822  |    5.69909 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.429054 |       0.181245 |    3.52341 |
| solution-pl        |     0.424786 |       0.186642 |    3.53508 |
| solution-flask     |     0.425488 |       1.00874  |    5.31846 |