# 2024-06-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.56236  |       1.13187  |   0.076573 |
| solution-aron-mark |     6.55164  |       0.120922 |   0.180243 |
| solution-pl        |     0.810294 |       0.122093 |   0.188619 |
| solution-1-flask   |     0.811833 |       1.0103   |   0.274733 |
| solution-1         |     9.19543  |       2e-06    |   1.05625  |
| solution-2         |     0.765956 |       1.08309  |   1.07934  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.761672 |       1.01203  |   0.175329 |
| solution-aron-mark |     0.804403 |       0.124849 |   0.280159 |
| solution-pl        |     0.782471 |       0.121742 |   0.285767 |
| solution-1-flask   |     0.757695 |       1.01091  |   0.817461 |
| solution-2         |     0.784395 |       0.584317 |   5.25292  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.770767 |       1.01124  |   0.802571 |
| solution-aron-mark |     0.769437 |       0.139622 |   0.875372 |
| solution-pl        |     0.786515 |       0.136377 |   0.879765 |
| solution-1-flask   |     0.845335 |       1.01127  |   5.94745  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.765686 |       0.168978 |    2.9926  |
| solution-pl        |     0.78457  |       0.168416 |    3.01702 |
| solution-flask     |     0.807049 |       1.0123   |    3.09707 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.738504 |       0.313263 |    38.0393 |