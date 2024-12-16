# 2024-12-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.84377  |       1.00849  |   0.109482 |
| solution-pl        |     0.525092 |       0.10975  |   0.184709 |
| solution-aron-mark |     0.531307 |       0.107014 |   0.185848 |
| solution-1-flask   |     4.76619  |       1.17876  |   0.266008 |
| solution-1         |     7.46657  |       1e-06    |   0.584823 |
| solution-2         |     0.525305 |       0.546893 |   1.08461  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.529153 |       0.109569 |   0.317394 |
| solution-pl        |     0.53157  |       0.109548 |   0.3175   |
| solution-flask     |     0.529962 |       1.00875  |   0.506233 |
| solution-1-flask   |     0.530567 |       1.00907  |   0.811933 |
| solution-2         |     0.529574 |       0.468407 |   4.74629  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.531024 |       0.116363 |    1.06445 |
| solution-aron-mark |     0.529107 |       0.11509  |    1.11252 |
| solution-flask     |     0.529799 |       1.00909  |    2.23584 |
| solution-1-flask   |     0.530636 |       1.00907  |    5.71063 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.538157 |       0.146761 |    4.40369 |
| solution-pl        |     0.532562 |       0.149134 |    4.41368 |
| solution-flask     |     0.535597 |       1.00884  |    8.80672 |