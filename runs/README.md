# 2024-10-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.08255  |       1.08168  |   0.092438 |
| solution-pl        |     5.66207  |       0.104162 |   0.168348 |
| solution-aron-mark |     0.54486  |       0.101697 |   0.183926 |
| solution-1-flask   |     0.558755 |       1.00893  |   0.254589 |
| solution-1         |     7.35363  |       1e-06    |   0.847414 |
| solution-2         |     0.545225 |       0.597758 |   0.963419 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.546529 |       1.00936  |   0.222484 |
| solution-aron-mark |     0.555764 |       0.103467 |   0.288559 |
| solution-pl        |     0.549097 |       0.103832 |   0.29427  |
| solution-1-flask   |     0.555158 |       1.00869  |   0.75412  |
| solution-2         |     0.555797 |       0.466517 |  12.0697   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.586128 |       1.00884  |   0.885403 |
| solution-pl        |     0.550439 |       0.11055  |   0.993039 |
| solution-aron-mark |     0.546931 |       0.112564 |   1.0005   |
| solution-1-flask   |     0.558604 |       1.0088   |   5.28169  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.546665 |       1.00886  |    3.99192 |
| solution-pl        |     0.551772 |       0.143416 |    4.06915 |
| solution-aron-mark |     0.543965 |       0.145213 |    4.11958 |