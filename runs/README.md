# 2024-03-31

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.64627  |       1.06267  |   0.065327 |
| solution-aron-mark |     0.667228 |       0.103072 |   0.159464 |
| solution-pl        |     0.654086 |       0.107377 |   0.160936 |
| solution-1-flask   |     0.654629 |       1.00882  |   0.258105 |
| solution-1         |     7.99743  |       1e-06    |   0.775331 |
| solution-2         |     4.65663  |       0.447599 |   1.30066  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.645219 |       1.00871  |   0.164966 |
| solution-aron-mark |     0.658609 |       0.110615 |   0.242893 |
| solution-pl        |     0.634462 |       0.112847 |   0.252004 |
| solution-1-flask   |     0.667358 |       1.009    |   0.800648 |
| solution-2         |     0.647556 |       0.434502 |   7.62124  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.649527 |       0.120368 |   0.779485 |
| solution-pl        |     0.650159 |       0.118177 |   0.795838 |
| solution-flask     |     0.651546 |       1.00897  |   0.886317 |
| solution-1-flask   |     0.653284 |       1.00914  |   5.46761  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.667208 |       0.150565 |    3.09804 |
| solution-aron-mark |     0.653673 |       0.151665 |    3.11603 |
| solution-flask     |     0.651231 |       1.00873  |    5.05285 |