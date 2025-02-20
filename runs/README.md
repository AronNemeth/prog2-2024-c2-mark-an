# 2025-02-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.534609 |       1.00914  |   0.082344 |
| solution-aron-mark |     0.535765 |       0.140467 |   0.206502 |
| solution-pl        |     1.84741  |       0.154461 |   0.208609 |
| solution-1-flask   |     5.032    |       1.08862  |   0.271593 |
| solution-1         |     7.26621  |       1e-06    |   0.62859  |
| solution-2         |     0.543122 |       0.641676 |   0.89975  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.545966 |       1.00904  |   0.295067 |
| solution-aron-mark |     0.538391 |       0.145563 |   0.310103 |
| solution-pl        |     0.544279 |       0.145172 |   0.313163 |
| solution-1-flask   |     0.564125 |       1.00897  |   0.809265 |
| solution-2         |     0.544425 |       0.511151 |   5.5257   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.550104 |       0.14994  |   0.915753 |
| solution-pl        |     0.563864 |       0.153884 |   0.973594 |
| solution-flask     |     0.5559   |       1.0091   |   1.27272  |
| solution-1-flask   |     0.542011 |       1.00907  |   5.75843  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.538662 |       0.180291 |    2.87267 |
| solution-aron-mark |     0.5333   |       0.179389 |    2.88554 |
| solution-flask     |     0.533991 |       1.00887  |    4.2809  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.550514 |       0.293108 |    18.179  |
| solution-pl        |     0.534302 |       0.28001  |    18.2204 |