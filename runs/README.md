# 2024-07-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.17318  |       1.10189  |   0.091387 |
| solution-aron-mark |     0.49629  |       0.101251 |   0.166474 |
| solution-pl        |     5.6901   |       0.101822 |   0.169794 |
| solution-1-flask   |     0.501696 |       1.00949  |   0.261449 |
| solution-1         |     7.75736  |       1e-06    |   0.655658 |
| solution-2         |     0.501386 |       0.481565 |   0.999613 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.496774 |       1.00893  |   0.22082  |
| solution-aron-mark |     0.501523 |       0.105465 |   0.286217 |
| solution-pl        |     0.505688 |       0.104304 |   0.291367 |
| solution-1-flask   |     0.510627 |       1.00865  |   0.783149 |
| solution-2         |     0.505358 |       0.471934 |   3.38376  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.503511 |       1.00908  |   0.893817 |
| solution-pl        |     0.508396 |       0.112556 |   1.00636  |
| solution-aron-mark |     0.500322 |       0.111339 |   1.02614  |
| solution-1-flask   |     0.507217 |       1.0089   |   5.6422   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.500127 |       1.00915  |    4.02037 |
| solution-pl        |     0.500555 |       0.145644 |    4.15873 |
| solution-aron-mark |     0.502711 |       0.144538 |    4.19184 |