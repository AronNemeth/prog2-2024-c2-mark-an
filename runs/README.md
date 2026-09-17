# 2026-09-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.18717  |       1.0618   |   0.150777 |
| solution-pl        |     2.17891  |       0.167167 |   0.253991 |
| solution-aron-mark |     0.428935 |       0.157741 |   0.257243 |
| solution-1-flask   |     0.450458 |       1.00851  |   0.273362 |
| solution-1         |     8.15082  |       1e-06    |   0.756081 |
| solution-2         |     5.73467  |       0.63497  |   0.950066 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.437576 |       0.157075 |   0.387124 |
| solution-aron-mark |     0.435243 |       0.158667 |   0.389409 |
| solution-flask     |     0.438583 |       1.00857  |   0.412192 |
| solution-1-flask   |     0.442786 |       1.0089   |   0.818665 |
| solution-2         |     0.438784 |       0.516446 |   3.33928  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.434646 |       0.168118 |    1.16612 |
| solution-aron-mark |     0.430211 |       0.162117 |    1.17273 |
| solution-flask     |     0.43102  |       1.00906  |    1.70693 |
| solution-1-flask   |     0.443652 |       1.00899  |    5.74818 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.448448 |       0.189455 |    3.78828 |
| solution-pl        |     0.441864 |       0.185956 |    3.80121 |
| solution-flask     |     0.43432  |       1.00876  |    5.40413 |