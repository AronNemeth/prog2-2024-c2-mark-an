# 2024-07-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.520304 |       1.00886  |   0.076202 |
| solution-pl        |     0.491321 |       0.102533 |   0.168113 |
| solution-aron-mark |     5.81137  |       0.102593 |   0.169161 |
| solution-1-flask   |     1.09766  |       1.06242  |   0.267495 |
| solution-1         |     7.83402  |       1e-06    |   0.594231 |
| solution-2         |     0.493103 |       0.513208 |   0.888135 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.509854 |       1.00899  |   0.193545 |
| solution-aron-mark |     0.504926 |       0.10429  |   0.288076 |
| solution-pl        |     0.513487 |       0.104343 |   0.291639 |
| solution-1-flask   |     0.508805 |       1.00907  |   0.78373  |
| solution-2         |     0.525135 |       0.480419 |   2.74913  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.511807 |       1.00937  |   0.872444 |
| solution-pl        |     0.497332 |       0.110762 |   0.979595 |
| solution-aron-mark |     0.504708 |       0.110367 |   0.9874   |
| solution-1-flask   |     0.508844 |       1.00896  |   5.49378  |
| solution-2         |     0.516691 |       0.531113 |  46.5938   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.496147 |       1.00928  |    4.16982 |
| solution-aron-mark |     0.502716 |       0.150844 |    4.30081 |
| solution-pl        |     0.501126 |       0.151018 |    4.36749 |