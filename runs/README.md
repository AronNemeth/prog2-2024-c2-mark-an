# 2025-04-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.512949 |       1.0087   |   0.083647 |
| solution-aron-mark |     1.92144  |       0.121183 |   0.185791 |
| solution-pl        |     0.522489 |       0.12335  |   0.191234 |
| solution-1-flask   |     5.2237   |       1.10144  |   0.268783 |
| solution-1         |     7.57382  |       1e-06    |   0.594512 |
| solution-2         |     0.513929 |       0.559418 |   1.06663  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.515223 |       0.121886 |   0.291413 |
| solution-flask     |     0.509377 |       1.00917  |   0.295162 |
| solution-pl        |     0.509737 |       0.121964 |   0.301877 |
| solution-1-flask   |     0.519641 |       1.00905  |   0.791605 |
| solution-2         |     0.509906 |       0.51267  |   4.16059  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.506514 |       0.131367 |   0.89228  |
| solution-aron-mark |     0.510815 |       0.128275 |   0.896104 |
| solution-flask     |     0.509207 |       1.00936  |   1.25146  |
| solution-1-flask   |     0.519207 |       1.00895  |   5.65424  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.510201 |       0.162229 |    2.80452 |
| solution-pl        |     0.511549 |       0.15986  |    2.8077  |
| solution-flask     |     0.511361 |       1.01019  |    4.28281 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.513268 |       0.270997 |    17.4285 |
| solution-pl        |     0.517006 |       0.272586 |    17.5682 |