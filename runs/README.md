# 2026-07-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.07386  |       1.00868  |   0.104492 |
| solution-pl        |     0.430449 |       0.151209 |   0.237047 |
| solution-aron-mark |     0.438592 |       0.15232  |   0.238115 |
| solution-1-flask   |     1.12003  |       1.03696  |   0.273785 |
| solution-1         |     8.19788  |       1e-06    |   0.647015 |
| solution-2         |     4.44451  |       0.698324 |   0.775822 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.43977  |       0.156857 |   0.373825 |
| solution-aron-mark |     0.458391 |       0.157375 |   0.376562 |
| solution-flask     |     0.444646 |       1.00872  |   0.391699 |
| solution-1-flask   |     0.464791 |       1.00888  |   0.811013 |
| solution-2         |     0.424197 |       0.513056 |  11.9983   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.46338  |       0.170918 |    1.11714 |
| solution-aron-mark |     0.47689  |       0.164812 |    1.11923 |
| solution-flask     |     0.448007 |       1.00859  |    1.63396 |
| solution-1-flask   |     0.446589 |       1.0087   |    5.67969 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.429934 |       0.196177 |    3.48891 |
| solution-pl        |     0.426028 |       0.180239 |    3.50112 |
| solution-flask     |     0.467308 |       1.00862  |    5.26258 |