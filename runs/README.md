# 2026-04-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.29227  |       1.0701   |   0.107998 |
| solution-aron-mark |     4.8523   |       0.155917 |   0.233826 |
| solution-pl        |     0.426579 |       0.149233 |   0.237632 |
| solution-1-flask   |     0.538399 |       1.0081   |   0.265853 |
| solution-1         |     7.8574   |       1e-06    |   0.955277 |
| solution-2         |     0.421327 |       0.758483 |   1.23122  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.413763 |       0.148749 |   0.366832 |
| solution-pl        |     0.43099  |       0.157459 |   0.374611 |
| solution-flask     |     0.43009  |       1.0085   |   0.406285 |
| solution-1-flask   |     0.420825 |       1.00957  |   0.811449 |
| solution-2         |     0.430118 |       0.52143  |   2.23156  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.430951 |       0.158962 |    1.12488 |
| solution-aron-mark |     0.433169 |       0.160962 |    1.15328 |
| solution-flask     |     0.423113 |       1.00878  |    1.69369 |
| solution-1-flask   |     0.444175 |       1.00868  |    5.75521 |
| solution-2         |     0.433822 |       0.626192 |  172.564   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.468046 |       0.191349 |    4.14347 |
| solution-aron-mark |     0.457713 |       0.191781 |    4.57417 |
| solution-flask     |     0.445428 |       1.00863  |    5.63653 |