# 2025-12-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.00417  |       1.04435  |   0.100771 |
| solution-pl        |     0.923926 |       0.157991 |   0.242417 |
| solution-aron-mark |     0.918785 |       0.15585  |   0.243767 |
| solution-1-flask   |     0.92438  |       1.00814  |   0.265214 |
| solution-1         |     8.10469  |       1e-06    |   0.758736 |
| solution-2         |     5.26027  |       0.741017 |   0.899447 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.473028 |       0.159467 |   0.368565 |
| solution-pl        |     0.473542 |       0.158255 |   0.372379 |
| solution-flask     |     0.469317 |       1.00846  |   0.378057 |
| solution-1-flask   |     0.472205 |       1.0084   |   0.789774 |
| solution-2         |     0.801467 |       0.50159  |   2.78883  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.470204 |       0.166667 |    1.07374 |
| solution-pl        |     0.47009  |       0.172745 |    1.08408 |
| solution-flask     |     0.4776   |       1.00848  |    1.56351 |
| solution-1-flask   |     0.475768 |       1.00845  |    5.61197 |
| solution-2         |     0.464816 |       0.561329 |  176.599   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.473379 |       0.194077 |    3.22405 |
| solution-aron-mark |     0.470506 |       0.196979 |    3.22429 |
| solution-flask     |     0.476496 |       1.00863  |    5.09138 |