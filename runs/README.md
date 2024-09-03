# 2024-09-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.05514  |       1.04385  |   0.09183  |
| solution-pl        |     0.544319 |       0.103186 |   0.171559 |
| solution-aron-mark |     5.59338  |       0.102964 |   0.172056 |
| solution-1-flask   |     0.554853 |       1.00913  |   0.257978 |
| solution-1         |     7.52614  |       1e-06    |   0.758307 |
| solution-2         |     0.547828 |       0.692658 |   0.95543  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.547039 |       1.00877  |   0.223346 |
| solution-aron-mark |     0.548136 |       0.103914 |   0.29294  |
| solution-pl        |     0.546979 |       0.104302 |   0.295238 |
| solution-1-flask   |     0.553779 |       1.00903  |   0.777596 |
| solution-2         |     0.548063 |       0.471045 |   2.42002  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.547282 |       1.00929  |   0.886204 |
| solution-pl        |     0.555895 |       0.110468 |   0.989593 |
| solution-aron-mark |     0.547337 |       0.111925 |   0.989781 |
| solution-1-flask   |     0.553112 |       1.00911  |   5.57057  |
| solution-2         |     0.546283 |       0.524401 | 169.979    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.546623 |       1.0091   |    4.12647 |
| solution-aron-mark |     0.551753 |       0.144918 |    4.15075 |
| solution-pl        |     0.553494 |       0.141903 |    4.20064 |