# 2025-04-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.511735 |       1.00868  |   0.082207 |
| solution-pl        |     0.50417  |       0.119467 |   0.184703 |
| solution-aron-mark |     1.76075  |       0.12074  |   0.184778 |
| solution-1-flask   |     5.14083  |       1.0437   |   0.27047  |
| solution-1         |     7.44653  |       1e-06    |   0.655298 |
| solution-2         |     0.50536  |       0.573048 |   0.917682 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.505858 |       0.122014 |   0.290713 |
| solution-pl        |     0.501108 |       0.122371 |   0.292081 |
| solution-flask     |     0.503468 |       1.00896  |   0.298539 |
| solution-1-flask   |     0.511317 |       1.00881  |   0.822802 |
| solution-2         |     0.502694 |       0.497706 |   2.11622  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.506855 |       0.129202 |   0.905368 |
| solution-pl        |     0.505924 |       0.128521 |   0.905728 |
| solution-flask     |     0.509194 |       1.00887  |   1.25217  |
| solution-1-flask   |     0.507973 |       1.00914  |   5.688    |
| solution-2         |     0.499328 |       0.548623 | 179.142    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.502706 |       0.157993 |    2.7969  |
| solution-aron-mark |     0.505753 |       0.162663 |    2.80612 |
| solution-flask     |     0.501673 |       1.00895  |    4.27159 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.506109 |       0.271319 |    16.7705 |
| solution-pl        |     0.505451 |       0.264771 |    17.097  |