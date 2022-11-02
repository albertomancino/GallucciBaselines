TEMPLATE = """experiment:
  dataset: subdatasets_{sub}
  data_config:
    strategy: dataset
    dataset_path: {path}
  splitting:
    test_splitting:
      strategy: random_subsampling
      test_ratio: 0.2
      folds: 1
  top_k: 10
  evaluation:
    cutoffs: [10, 5, 1]
    simple_metrics: [nDCGRendle2020, HR, ItemCoverage, UserCoverage]
    relevance_threshold: 3
  gpu: 0
  models:
    NeuMF:
      meta:
        hyper_max_evals: 10
        hyper_opt_alg: tpe
        validation_rate: 5
        save_recs: True
        validation_metric: nDCGRendle2020@10
      lr: [loguniform, -10, -1]
      batch_size: 512
      epochs: 100
      mf_factors: [quniform, 8, 32, 1]
      mlp_factors: [8, 16]
      mlp_hidden_size: [(32, 16, 8), (64, 32, 16)]
      prob_keep_dropout: [uniform, 0.5, 1]
      is_mf_train: True
      is_mlp_train: True
       """
