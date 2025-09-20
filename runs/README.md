# 2025-09-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.47988  |       1.00825  |   0.10174  |
| solution-aron-mark |     0.469386 |       0.150723 |   0.235656 |
| solution-pl        |     6.20807  |       0.369742 |   0.243331 |
| solution-1-flask   |     1.50098  |       1.04477  |   0.272418 |
| solution-1         |     7.52474  |       1e-06    |   0.872053 |
| solution-2         |     0.483093 |       0.737624 |   0.981683 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.482706 |       0.153084 |   0.364193 |
| solution-pl        |     0.478425 |       0.1544   |   0.368017 |
| solution-flask     |     0.480061 |       1.0084   |   0.381119 |
| solution-1-flask   |     0.486259 |       1.0083   |   0.791013 |
| solution-2         |     0.483626 |       0.500243 |   2.09358  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.480278 |       0.161371 |    1.07664 |
| solution-aron-mark |     0.477396 |       0.161785 |    1.0772  |
| solution-flask     |     0.478884 |       1.00837  |    1.59399 |
| solution-1-flask   |     0.487632 |       1.00856  |    5.64877 |
| solution-2         |     0.48471  |       0.549648 |  163.985   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.478248 |       0.192741 |    3.21357 |
| solution-aron-mark |     0.480758 |       0.191774 |    3.23007 |
| solution-flask     |     0.475783 |       1.00843  |    5.06767 |