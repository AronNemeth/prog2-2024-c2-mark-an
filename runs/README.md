# 2024-05-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.42197  |       1.08327  |   0.074516 |
| solution-pl        |     0.651563 |       0.102534 |   0.160897 |
| solution-aron-mark |     6.86436  |       0.102592 |   0.163527 |
| solution-1-flask   |     0.674867 |       1.00891  |   0.263401 |
| solution-1         |     8.99126  |       1e-06    |   0.962909 |
| solution-2         |     1.21075  |       0.430151 |   1.2086   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.680137 |       1.00934  |   0.161935 |
| solution-aron-mark |     0.663494 |       0.103493 |   0.257675 |
| solution-pl        |     0.663647 |       0.103489 |   0.265164 |
| solution-1-flask   |     0.672986 |       1.00918  |   0.791135 |
| solution-2         |     0.662873 |       0.429158 |   5.28233  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661657 |       1.00928  |   0.7214   |
| solution-pl        |     0.660857 |       0.113695 |   0.806261 |
| solution-aron-mark |     0.662467 |       0.111428 |   0.813289 |
| solution-1-flask   |     0.680715 |       1.0095   |   5.5502   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.664365 |       1.00949  |    2.48087 |
| solution-pl        |     0.659678 |       0.148989 |    2.60304 |
| solution-aron-mark |     0.662719 |       0.148144 |    2.60324 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.660667 |       1.00917  |    16.1219 |
| solution-pl        |     0.660284 |       0.271844 |    20.7388 |
| solution-aron-mark |     0.660627 |       0.276645 |    22.2737 |