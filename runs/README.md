# 2025-07-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.19232  |       1.10393  |   0.101509 |
| solution-aron-mark |     4.30122  |       0.145209 |   0.233346 |
| solution-pl        |     0.498553 |       0.148833 |   0.237522 |
| solution-1-flask   |     0.502596 |       1.00825  |   0.266415 |
| solution-1         |     7.13994  |       1e-06    |   0.698782 |
| solution-2         |     0.486432 |       0.546467 |   1.03436  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.495473 |       0.148631 |   0.360466 |
| solution-aron-mark |     0.495593 |       0.150022 |   0.360878 |
| solution-flask     |     0.49245  |       1.00826  |   0.383778 |
| solution-1-flask   |     0.501715 |       1.00828  |   0.803293 |
| solution-2         |     0.491573 |       0.498615 |   1.72982  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.498845 |       0.156434 |    1.06982 |
| solution-aron-mark |     0.496811 |       0.156116 |    1.07153 |
| solution-flask     |     0.492574 |       1.00825  |    1.6108  |
| solution-1-flask   |     0.503854 |       1.00842  |    5.6776  |
| solution-2         |     0.493217 |       0.556965 |  193.119   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.497363 |       0.186685 |    3.21448 |
| solution-aron-mark |     0.501485 |       0.188485 |    3.22151 |
| solution-flask     |     0.495306 |       1.00907  |    5.16057 |