# 2026-08-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.65752  |       1.05012  |   0.110957 |
| solution-pl        |     0.441864 |       0.154904 |   0.240435 |
| solution-aron-mark |     4.5794   |       0.153731 |   0.242066 |
| solution-1-flask   |     0.447622 |       1.00885  |   0.273133 |
| solution-1         |     7.5573   |       1e-06    |   0.685969 |
| solution-2         |     0.440658 |       0.725208 |   0.860644 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.461693 |       0.159721 |   0.378463 |
| solution-pl        |     0.444249 |       0.156495 |   0.379161 |
| solution-flask     |     0.436747 |       1.00876  |   0.403624 |
| solution-1-flask   |     0.45301  |       1.00966  |   0.823009 |
| solution-2         |     0.437669 |       0.558592 |  15.9144   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.437925 |       0.163729 |    1.13619 |
| solution-pl        |     0.448042 |       0.166829 |    1.13811 |
| solution-flask     |     0.447597 |       1.01045  |    1.69176 |
| solution-1-flask   |     0.450918 |       1.00971  |    5.79258 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.44388  |       0.195302 |    3.80315 |
| solution-pl        |     0.441763 |       0.193827 |    3.8266  |
| solution-flask     |     0.441005 |       1.00917  |    5.46239 |