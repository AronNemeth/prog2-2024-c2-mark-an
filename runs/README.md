# 2026-09-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.16874  |       1.06039  |   0.112412 |
| solution-aron-mark |     6.26766  |       0.179573 |   0.248054 |
| solution-pl        |     0.454562 |       0.176578 |   0.253827 |
| solution-1-flask   |     0.480618 |       1.0087   |   0.270439 |
| solution-1         |     9.0796   |       2e-06    |   1.05709  |
| solution-2         |     0.443028 |       0.783269 |   1.25259  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.46323  |       0.164385 |   0.391601 |
| solution-flask     |     0.474272 |       1.00888  |   0.412779 |
| solution-aron-mark |     0.466661 |       0.161834 |   0.425063 |
| solution-1-flask   |     0.454909 |       1.00913  |   0.840746 |
| solution-2         |     0.448834 |       0.549876 |   2.15178  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.458335 |       0.166419 |    1.15753 |
| solution-aron-mark |     0.477537 |       0.170792 |    1.16148 |
| solution-flask     |     0.465845 |       1.00896  |    1.72086 |
| solution-1-flask   |     0.461857 |       1.00857  |    5.95032 |
| solution-2         |     0.470641 |       0.604701 |  166.712   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.489605 |       0.192451 |    3.80076 |
| solution-pl        |     0.471798 |       0.194668 |    3.80617 |
| solution-flask     |     0.452461 |       1.00977  |    5.65414 |