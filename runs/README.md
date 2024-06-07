# 2024-06-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.5059   |       1.10265  |   0.077494 |
| solution-aron-mark |     6.80817  |       0.102784 |   0.158609 |
| solution-pl        |     0.681488 |       0.103554 |   0.163188 |
| solution-1-flask   |     0.717844 |       1.00931  |   0.263053 |
| solution-1         |     8.21786  |       1e-06    |   0.715602 |
| solution-2         |     0.661147 |       0.42849  |   1.12442  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.679952 |       1.00905  |   0.16011  |
| solution-pl        |     0.671088 |       0.104883 |   0.252561 |
| solution-aron-mark |     0.684449 |       0.105986 |   0.253468 |
| solution-1-flask   |     0.683354 |       1.00863  |   0.779906 |
| solution-2         |     0.676934 |       0.440008 |  11.3226   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.672467 |       1.00926  |   0.712194 |
| solution-pl        |     0.711235 |       0.113629 |   0.802288 |
| solution-aron-mark |     0.681703 |       0.114271 |   0.808126 |
| solution-1-flask   |     0.687209 |       1.00898  |   5.66517  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.666059 |       1.00924  |    2.5044  |
| solution-pl        |     0.701725 |       0.147906 |    2.65458 |
| solution-aron-mark |     0.692498 |       0.155325 |    2.76608 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.67694  |       1.00912  |    16.1004 |
| solution-aron-mark |     0.671425 |       0.282227 |    21.1414 |
| solution-pl        |     0.682923 |       0.279929 |    21.5698 |