# 2024-04-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.656676 |       1.00887  |   0.064726 |
| solution-aron-mark |     0.654278 |       0.110013 |   0.164002 |
| solution-pl        |     5.77864  |       0.112502 |   0.167133 |
| solution-1-flask   |     1.41847  |       1.0562   |   0.26653  |
| solution-1         |     7.87486  |       1e-06    |   0.614107 |
| solution-2         |     0.655611 |       0.417852 |   0.705111 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.660875 |       1.00886  |   0.163334 |
| solution-aron-mark |     0.659267 |       0.118841 |   0.260744 |
| solution-pl        |     0.662775 |       0.117985 |   0.260768 |
| solution-1-flask   |     0.6781   |       1.00869  |   0.800209 |
| solution-2         |     0.669158 |       0.427595 |   1.8359   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.675736 |       1.00885  |   0.712545 |
| solution-pl        |     0.668855 |       0.125936 |   0.829678 |
| solution-aron-mark |     0.67494  |       0.125058 |   0.831513 |
| solution-1-flask   |     0.675484 |       1.00858  |   5.6159   |
| solution-2         |     0.655466 |       0.48038  | 169.761    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.657248 |       1.00899  |    2.44839 |
| solution-aron-mark |     0.661138 |       0.160699 |    3.33424 |
| solution-pl        |     0.665537 |       0.181956 |    3.36883 |

## Inputs: 1000000, Queries 1000

| solution       |   setup_time |   preproc_time |   run_time |
|:---------------|-------------:|---------------:|-----------:|
| solution-flask |     0.657949 |        1.00909 |    15.5166 |