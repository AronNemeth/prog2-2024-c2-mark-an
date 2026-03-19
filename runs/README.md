# 2026-03-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.88912  |       1.05365  |   0.109487 |
| solution-pl        |     4.69341  |       0.153009 |   0.240505 |
| solution-aron-mark |     0.451755 |       0.15073  |   0.24075  |
| solution-1-flask   |     0.456789 |       1.00875  |   0.2715   |
| solution-1         |     9.13428  |       1e-06    |   0.752093 |
| solution-2         |     0.45195  |       0.663622 |   0.820576 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.447656 |       0.151745 |   0.375912 |
| solution-flask     |     0.45746  |       1.00903  |   0.38716  |
| solution-aron-mark |     0.483018 |       0.15889  |   0.390612 |
| solution-1-flask   |     0.459528 |       1.00897  |   0.796647 |
| solution-2         |     0.459856 |       0.538163 |  22.2397   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.455262 |       0.166497 |    1.15731 |
| solution-pl        |     0.450423 |       0.157848 |    1.16519 |
| solution-flask     |     0.476403 |       1.00969  |    1.65107 |
| solution-1-flask   |     0.456077 |       1.01034  |    5.75555 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.452634 |       0.18231  |    4.17124 |
| solution-pl        |     0.462084 |       0.198637 |    4.27398 |
| solution-flask     |     0.457917 |       1.00895  |    5.36624 |