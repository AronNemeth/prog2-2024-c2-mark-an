# 2026-09-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.16791  |       1.06763  |   0.130827 |
| solution-aron-mark |     0.429269 |       0.153099 |   0.242277 |
| solution-pl        |     2.38856  |       0.167733 |   0.243043 |
| solution-1-flask   |     0.435614 |       1.00841  |   0.270488 |
| solution-1         |     7.90029  |       1e-06    |   0.742746 |
| solution-2         |     5.50891  |       0.642149 |   0.861073 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.428571 |       0.15649  |   0.372051 |
| solution-aron-mark |     0.431231 |       0.156313 |   0.372943 |
| solution-flask     |     0.432554 |       1.00835  |   0.397165 |
| solution-1-flask   |     0.438757 |       1.00863  |   0.807303 |
| solution-2         |     0.433903 |       0.50982  |  16.2931   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.431471 |       0.161788 |    1.12258 |
| solution-pl        |     0.427494 |       0.163119 |    1.12402 |
| solution-flask     |     0.439075 |       1.00853  |    1.6444  |
| solution-1-flask   |     0.438125 |       1.00865  |    5.68859 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.432172 |       0.183591 |    3.55991 |
| solution-pl        |     0.428995 |       0.184072 |    3.62156 |
| solution-flask     |     0.431262 |       1.0085   |    5.36637 |