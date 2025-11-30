# 2025-11-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |      2.75318 |       1.09389  |   0.104247 |
| solution-aron-mark |      0.47839 |       0.161367 |   0.247417 |
| solution-pl        |      0.48433 |       0.161211 |   0.24838  |
| solution-1-flask   |      0.48126 |       1.00882  |   0.265703 |
| solution-1         |      7.58284 |       1e-06    |   0.703252 |
| solution-2         |      5.04031 |       0.667078 |   0.889694 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.484739 |       0.163289 |   0.370965 |
| solution-aron-mark |     0.510252 |       0.165828 |   0.3745   |
| solution-flask     |     0.476173 |       1.00926  |   0.389546 |
| solution-1-flask   |     0.486097 |       1.00869  |   0.807671 |
| solution-2         |     0.480977 |       0.515345 |   3.4381   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.490191 |       0.170904 |    1.07746 |
| solution-aron-mark |     0.480871 |       0.176382 |    1.07758 |
| solution-flask     |     0.48628  |       1.00951  |    1.61157 |
| solution-1-flask   |     0.484529 |       1.00975  |    5.66495 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.473449 |       0.205587 |    3.29709 |
| solution-aron-mark |     0.486763 |       0.202643 |    3.32418 |
| solution-flask     |     0.483007 |       1.00941  |    5.10666 |