# 2026-10-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.57919  |       1.06496  |   0.112089 |
| solution-aron-mark |     6.20591  |       0.166351 |   0.237472 |
| solution-pl        |     0.416601 |       0.153457 |   0.243242 |
| solution-1-flask   |     0.423772 |       1.00832  |   0.268095 |
| solution-1         |     7.71262  |       1e-06    |   0.623828 |
| solution-2         |     0.413426 |       0.580281 |   0.898839 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.42571  |       0.148109 |   0.365638 |
| solution-aron-mark |     0.412472 |       0.153353 |   0.372646 |
| solution-flask     |     0.414656 |       1.00831  |   0.396906 |
| solution-1-flask   |     0.432855 |       1.00866  |   0.820063 |
| solution-2         |     0.419615 |       0.494239 |   3.66342  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.415296 |       0.157938 |    1.11864 |
| solution-aron-mark |     0.438482 |       0.159195 |    1.13295 |
| solution-flask     |     0.419936 |       1.00831  |    1.64001 |
| solution-1-flask   |     0.422107 |       1.00846  |    5.67801 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.423146 |       0.1849   |    3.52229 |
| solution-aron-mark |     0.41876  |       0.182283 |    3.53073 |
| solution-flask     |     0.423789 |       1.00834  |    5.27986 |