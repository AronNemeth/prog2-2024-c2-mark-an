# 2026-07-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.47634  |       1.07709  |   0.127347 |
| solution-1-flask   |     0.449913 |       1.00924  |   0.229312 |
| solution-aron-mark |     0.442302 |       0.156456 |   0.237236 |
| solution-pl        |     7.59121  |       0.182754 |   0.237687 |
| solution-1         |     8.95852  |       1e-06    |   0.655368 |
| solution-2         |     0.429653 |       0.71172  |   1.24821  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.435013 |       0.155959 |   0.357373 |
| solution-pl        |     0.442577 |       0.157261 |   0.358656 |
| solution-flask     |     0.437632 |       1.00927  |   0.397549 |
| solution-1-flask   |     0.462881 |       1.00958  |   0.736861 |
| solution-2         |     0.434453 |       0.534022 |   4.24633  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.433236 |       0.161829 |    1.05333 |
| solution-pl        |     0.43848  |       0.164037 |    1.06108 |
| solution-flask     |     0.45411  |       1.00934  |    1.67138 |
| solution-1-flask   |     0.451559 |       1.00989  |    5.68643 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.522325 |       0.19277  |    4.02717 |
| solution-pl        |     0.448176 |       0.188574 |    4.04246 |
| solution-flask     |     0.44242  |       1.00955  |    5.43264 |