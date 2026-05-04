# 2026-05-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.70522  |       1.06086  |   0.096793 |
| solution-pl        |     0.417136 |       0.148233 |   0.223962 |
| solution-aron-mark |     4.85533  |       0.149615 |   0.22814  |
| solution-1-flask   |     0.427041 |       1.00877  |   0.228228 |
| solution-1         |     8.05481  |       1e-06    |   0.63711  |
| solution-2         |     0.414047 |       0.664367 |   0.943474 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.412681 |       0.149256 |   0.343596 |
| solution-pl        |     0.416262 |       0.168034 |   0.34779  |
| solution-flask     |     0.421974 |       1.00977  |   0.383416 |
| solution-1-flask   |     0.419506 |       1.00861  |   0.722592 |
| solution-2         |     0.420058 |       0.515691 |   4.34561  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.421341 |       0.156464 |    1.00819 |
| solution-aron-mark |     0.416579 |       0.154709 |    1.02326 |
| solution-flask     |     0.415271 |       1.009    |    1.60733 |
| solution-1-flask   |     0.41692  |       1.00867  |    5.60561 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.417514 |       0.180041 |    3.65934 |
| solution-aron-mark |     0.413582 |       0.180461 |    3.73353 |
| solution-flask     |     0.421922 |       1.00887  |    5.32738 |