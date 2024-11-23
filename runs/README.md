# 2024-11-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.30851  |       1.05844  |   0.112844 |
| solution-aron-mark |     0.581183 |       0.111278 |   0.185283 |
| solution-pl        |     6.25208  |       0.111991 |   0.192141 |
| solution-1-flask   |     0.581642 |       1.00889  |   0.262813 |
| solution-1         |     7.90297  |       1e-06    |   0.590758 |
| solution-2         |     0.571052 |       0.524633 |   1.01321  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.574172 |       0.112472 |   0.305139 |
| solution-aron-mark |     0.573    |       0.11073  |   0.321843 |
| solution-flask     |     0.582888 |       1.00885  |   0.486226 |
| solution-1-flask   |     0.585841 |       1.00897  |   0.780338 |
| solution-2         |     0.577559 |       0.494597 |   3.74441  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.598784 |       0.118111 |    1.02688 |
| solution-aron-mark |     0.574877 |       0.120074 |    1.0283  |
| solution-flask     |     0.58001  |       1.00923  |    2.16105 |
| solution-1-flask   |     0.584202 |       1.0092   |    5.39607 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.578702 |       0.147539 |    4.32047 |
| solution-pl        |     0.574154 |       0.151962 |    4.3961  |
| solution-flask     |     0.582528 |       1.00923  |    8.64661 |