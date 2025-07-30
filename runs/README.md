# 2025-07-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.72945  |       1.19826  |   0.105851 |
| solution-aron-mark |     4.85773  |       0.149761 |   0.236258 |
| solution-pl        |     0.518706 |       0.153158 |   0.237954 |
| solution-1-flask   |     0.553228 |       1.00847  |   0.2685   |
| solution-2         |     0.507164 |       0.777465 |   0.849015 |
| solution-1         |     8.28196  |       1e-06    |   0.992481 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.504934 |       0.151257 |   0.36356  |
| solution-aron-mark |     0.521005 |       0.153791 |   0.372167 |
| solution-flask     |     0.513582 |       1.00877  |   0.379095 |
| solution-1-flask   |     0.50608  |       1.00843  |   0.797519 |
| solution-2         |     0.502271 |       0.518593 |   2.46217  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.509125 |       0.160698 |    1.09688 |
| solution-pl        |     0.512023 |       0.160785 |    1.09702 |
| solution-flask     |     0.50421  |       1.0085   |    1.60313 |
| solution-1-flask   |     0.509275 |       1.00852  |    5.76913 |
| solution-2         |     0.511818 |       0.579433 |   34.0194  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.529697 |       0.192102 |    3.33624 |
| solution-pl        |     0.51442  |       0.196315 |    3.36859 |
| solution-flask     |     0.521586 |       1.00869  |    5.23051 |