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
    ItemKNN:
      meta:
        verbose: True
        save_recs: True
        validation_metric: nDCGRendle2020@10
        hyper_opt_alg: tpe
        hyper_max_evals: 10
      neighbors: [uniform, 5, {max_items}]
      similarity: ['cosine', 'jaccard']
      implementation: standard
      """
