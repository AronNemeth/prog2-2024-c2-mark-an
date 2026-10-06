# 2026-10-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.57272  |       1.0618   |   0.109278 |
| solution-aron-mark |     5.9405   |       0.178303 |   0.240489 |
| solution-pl        |     0.42493  |       0.15614  |   0.243606 |
| solution-1-flask   |     0.428886 |       1.00839  |   0.277822 |
| solution-1         |     8.32299  |       1e-06    |   1.08159  |
| solution-2         |     0.42158  |       0.733796 |   1.09632  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.427801 |       0.155317 |   0.380287 |
| solution-aron-mark |     0.431796 |       0.155579 |   0.382641 |
| solution-flask     |     0.423926 |       1.00859  |   0.407651 |
| solution-1-flask   |     0.430175 |       1.00857  |   0.815399 |
| solution-2         |     0.426293 |       0.505013 |   5.48574  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.42463  |       0.159698 |    1.13316 |
| solution-pl        |     0.42598  |       0.160954 |    1.14041 |
| solution-flask     |     0.43097  |       1.00875  |    1.67225 |
| solution-1-flask   |     0.436278 |       1.00835  |    5.72383 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.430326 |       0.185462 |    3.62834 |
| solution-pl        |     0.427619 |       0.185534 |    3.64612 |
| solution-flask     |     0.434479 |       1.00886  |    5.36405 |