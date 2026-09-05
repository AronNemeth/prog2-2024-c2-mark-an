# 2026-09-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.6099   |       1.06911  |   0.102025 |
| solution-1-flask   |     0.300564 |       1.00622  |   0.157229 |
| solution-pl        |     2.9193   |       0.164438 |   0.163355 |
| solution-aron-mark |     0.290997 |       0.11083  |   0.166326 |
| solution-2         |     3.38146  |       0.838184 |   0.737423 |
| solution-1         |     6.89634  |       1e-06    |   0.759863 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.293334 |       0.142878 |   0.237292 |
| solution-aron-mark |     0.29466  |       0.11375  |   0.251161 |
| solution-flask     |     0.292377 |       1.00583  |   0.292009 |
| solution-1-flask   |     0.326362 |       1.00562  |   0.478966 |
| solution-2         |     0.296132 |       0.368281 |   7.55554  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.303315 |       0.272382 |   0.816795 |
| solution-pl        |     0.297447 |       0.121474 |   0.829266 |
| solution-flask     |     0.287807 |       1.00678  |   1.27615  |
| solution-1-flask   |     0.296226 |       1.00761  |   4.02314  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.284164 |       0.234962 |    3.38685 |
| solution-pl        |     0.298491 |       0.224379 |    3.43477 |
| solution-flask     |     0.29237  |       1.00645  |    4.24251 |