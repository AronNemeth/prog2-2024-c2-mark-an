# 2024-05-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.649328 |       1.00895  |   0.065638 |
| solution-pl        |     5.9506   |       0.120911 |   0.174367 |
| solution-aron-mark |     0.652908 |       0.121873 |   0.186368 |
| solution-1-flask   |     1.40207  |       1.12204  |   0.261321 |
| solution-1         |     8.22332  |       1e-06    |   0.608167 |
| solution-2         |     0.650741 |       0.410978 |   1.09755  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.668884 |       1.00888  |   0.159671 |
| solution-pl        |     0.653634 |       0.12452  |   0.264848 |
| solution-aron-mark |     0.653207 |       0.12357  |   0.266978 |
| solution-1-flask   |     0.672795 |       1.0088   |   0.795345 |
| solution-2         |     0.652262 |       0.424952 |   5.44742  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.650157 |       1.00849  |   0.704718 |
| solution-aron-mark |     0.651338 |       0.131603 |   0.815234 |
| solution-pl        |     0.653045 |       0.131865 |   0.822502 |
| solution-1-flask   |     0.665987 |       1.00893  |   5.56082  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.670367 |       1.00899  |    2.44418 |
| solution-aron-mark |     0.653244 |       0.168224 |    2.59438 |
| solution-pl        |     0.649955 |       0.168874 |    2.60352 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.649407 |       1.00876  |    14.8365 |
| solution-aron-mark |     0.650723 |       0.296657 |    15.1778 |
| solution-pl        |     0.651081 |       0.296778 |    15.2672 |