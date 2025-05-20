# 2025-05-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.95297  |       1.00832  |   0.082267 |
| solution-aron-mark |     0.498426 |       0.122597 |   0.192539 |
| solution-pl        |     0.506393 |       0.122215 |   0.192778 |
| solution-1-flask   |     5.38047  |       1.08342  |   0.263368 |
| solution-1         |     7.91011  |       1e-06    |   0.829744 |
| solution-2         |     0.497056 |       0.702416 |   1.29291  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.500716 |       0.125278 |   0.292316 |
| solution-flask     |     0.50053  |       1.00833  |   0.293091 |
| solution-aron-mark |     0.499725 |       0.121907 |   0.293778 |
| solution-1-flask   |     0.526915 |       1.00814  |   0.778841 |
| solution-2         |     0.498197 |       0.515219 |  13.1665   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.507302 |       0.130766 |   0.889781 |
| solution-pl        |     0.5079   |       0.128497 |   0.904669 |
| solution-flask     |     0.503103 |       1.00859  |   1.25729  |
| solution-1-flask   |     0.505276 |       1.00851  |   5.45373  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.496243 |       0.163088 |    2.79014 |
| solution-aron-mark |     0.496585 |       0.159848 |    2.7957  |
| solution-flask     |     0.496304 |       1.00846  |    4.16121 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.501438 |       0.264927 |    16.2433 |
| solution-aron-mark |     0.497551 |       0.2695   |    16.3858 |