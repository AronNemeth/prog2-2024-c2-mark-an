# 2025-04-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.520622 |       1.00879  |   0.082415 |
| solution-pl        |     0.525029 |       0.120482 |   0.185896 |
| solution-aron-mark |     2.01336  |       0.122208 |   0.18877  |
| solution-1-flask   |     4.93316  |       1.05885  |   0.289616 |
| solution-1         |     7.53145  |       1e-06    |   0.90695  |
| solution-2         |     0.523607 |       0.742615 |   1.06161  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.511467 |       0.122248 |   0.292847 |
| solution-aron-mark |     0.511565 |       0.122063 |   0.293241 |
| solution-flask     |     0.514416 |       1.00906  |   0.294782 |
| solution-1-flask   |     0.518734 |       1.00876  |   0.783711 |
| solution-2         |     0.509394 |       0.511604 |   3.92305  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.513244 |       0.128889 |   0.911278 |
| solution-pl        |     0.512857 |       0.127813 |   0.912288 |
| solution-flask     |     0.519247 |       1.00906  |   1.24757  |
| solution-1-flask   |     0.516401 |       1.00916  |   5.47639  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.520811 |       0.163674 |    2.84713 |
| solution-pl        |     0.507368 |       0.161283 |    2.85645 |
| solution-flask     |     0.520181 |       1.00893  |    4.19224 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.512321 |       0.266408 |    16.7711 |
| solution-pl        |     0.50763  |       0.262846 |    16.7796 |